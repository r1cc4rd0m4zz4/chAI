import openai
import argparse
import sys
import os
import platform
import json
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

parser = argparse.ArgumentParser(description='Conversare con ChatGPT API')
parser.add_argument('--key', type=str, help='OpenAI API key')
parser.add_argument('--importa', type=str, help='Importa i messaggi di conversazione da un file json (.json)', default=None, required=False)
parser.add_argument('--sistema', type=str, help='imposta il contesto della conversazione da un file di testo (.system)', default=None, required=False)

openai.api_key = os.getenv('OPENAI_API_KEY')

def main(args):
    if not openai.api_key and not args.key:
        parser.error('È richiesta la variabile d\'ambiente OPENAI_API_KEY o il parametro --key.')
    elif not openai.api_key:
        openai.api_key = args.key
    
    messages = []

    if args.importa and os.path.exists(args.importa) and os.path.isfile(args.importa) and args.importa.endswith('.json') and os.path.getsize(args.importa) > 0:
        file_name = os.path.basename(args.importa)
        with open(file_name, "r", encoding="utf-8") as file:
            json_string = file.read()
            messages = json.loads(json_string, strict=False)

    if args.sistema and os.path.exists(args.sistema) and os.path.isfile(args.sistema) and args.sistema.endswith('.system') and os.path.getsize(args.sistema) > 0:
        file_name = os.path.basename(args.sistema)
        with open(file_name, "r", encoding="utf-8") as file:            
            testo = file.read()
            messages.append({"role": "system", "content": testo})
    
    main_prompt(messages)

def main_prompt(messages):
    history = FileHistory('.my_history_file')
    text = prompt('> ', history=history)
    if text == 'quit':
        save_chat(messages)
        sys.exit(1)
    elif text == 'clear':
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        save_chat(messages)
        messages = []
        main_prompt(messages)
    elif text == 'system':
        text = prompt('\nsystem> ', history=history)
        print(f'')
        messages.append({"role": "system", "content": text})
        main_prompt(messages)
    else:
        messages.append({"role": "user", "content": text})
        query_chatgpt(messages)

def query_chatgpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.9,
            messages=messages
        )
        response = response.choices[0]['message']['content'].strip()
    except openai.error.APIError as e:
        response = "APIError " + str(e)
    messages.append({"role": "assistant", "content": response})
    print(f'\n{response}\n')
    main_prompt(messages)
    
def save_chat(messages):
    # se il messages è vuoto non effettuare il salvataggio
    if len(messages) == 0:
        return
    
    messages.append({"role": "user", "content": "Dai un breve titolo alla conversazione, massimo 24 caratteri"})
    # intercetta l'errore http 4xx/5xx e aggiungi un try/except
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.9,
            messages=messages
        )
        response = response.choices[0]['message']['content'].strip()
    except openai.error.APIError as e:
        response = "APIError " + str(e)
    response = response.strip('"')
    response = response.strip(".")
    # rimuovi caratteri speciali da response connuna funzione di sistema
    response = response.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_").replace ("'", "_").replace ("`", "_").replace ("~", "_").replace ("!", "_").replace ("@", "_").replace ("#", "_").replace ("$", "_").replace ("%", "_").replace ("^", "_").replace ("&", "_").replace ("(", "_").replace (")", "_").replace ("-", "_").replace ("=", "_").replace ("+", "_").replace ("[", "_").replace ("]", "_").replace ("{", "_").replace ("}", "_").replace (";", "_").replace (",", "_").replace (".", "_")
    # rimuovi l'ultimo messaggio
    messages.remove(messages[-1])
    
    # Save the chat
    file_name = f"{response}.json"
    if os.path.exists(file_name):
        for i in range(2, 100):
            file_name = f"{response} ({i}).json"
            if not os.path.exists(file_name):
                break
    print(f'\nchat_name> {file_name}\n')
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json.dumps(messages, ensure_ascii=False, indent=0).replace('\\n', '\n'))

if __name__ == '__main__':
    args = parser.parse_args()
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    main(args)