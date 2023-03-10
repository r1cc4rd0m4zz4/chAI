import openai
import argparse
import sys
import os
import json
#import simplejson as json
from prompt_toolkit import prompt

parser = argparse.ArgumentParser(description='Chattare con ChatGPT API')
parser.add_argument('--key', type=str, help='OpenAI API key')
parser.add_argument('--importa', type=str, help='Importare un file json con i messaggi', default=None, required=False)

openai.api_key = os.getenv('OPENAI_API_KEY')

def main(args):
    if not openai.api_key and not args.key:
        parser.error('È richiesta la variabile d\'ambiente OPENAI_API_KEY o il parametro --key.')
    elif not openai.api_key:
        openai.api_key = args.key
    
    if args.importa and os.path.exists(args.importa) and os.path.isfile(args.importa) and args.importa.endswith('.json') and os.path.getsize(args.importa) > 0:
        file_name = os.path.basename(args.importa)
        with open(file_name, "r", encoding="utf-8") as file:
            json_string = file.read()
            messages = json.loads(json_string, strict=False)
    else:
        messages = []
    main_prompt(messages)

def main_prompt(messages):
    text = prompt('> ')
    if text == 'quit':
        save_chat(messages)
        sys.exit(1)
    elif text == 'clear':
        save_chat(messages)
        os.system('clear')
        messages = []
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
    # Ask for a title
    messages.append({"role": "user", "content": "Dai un breve titolo alla conversazione"})
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
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json.dumps(messages, ensure_ascii=False, indent=0).replace('\\n', '\n'))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)