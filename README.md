# ChAI 

## Introduzione ##
Un'interfaccia testuale per tenere in una finestra di terminale ChatGPT di OpenAI tramite l'API.
![Vista da](https://visitor-badge.glitch.me/badge?page_id=r1cc4rd0m4zz4/chAI&left_color=green&right_color=red)

## Vantaggi ##
 * Utilizzo essenziale della API Key di OpenAI, niente frozoli o interfacce web
 * Imposta la chiave API OpenAI in una variabile d'ambiente (OPENAI_API_KEY) o come parametro
 * Importa i messaggi di conversazione da un file json (.json)
 * Imposta il contesto della conversazione da un file di testo (.system) o con il comando `system`
 * Comando `clear` per iniziare una nuova chat salvando la precendente conversazione in un JSON
 * Inserire `quit` per salvare la chat in un JSON e tornare al terminale

## Avviso di non responsabilità ##
 * Non sono responsabile della vostra dipendenza da quello che farete con ChatGPT.
 * Consilgio di non interrogare ChatGPT con informazioni sensibili, riservate, personali, finanziarie e sanitarie.

## Utilizzo ##
### Richiede una OpenAI API key
```
Uso: ch.py [-h] [--key KEY] [--importa IMPORTA]

Chattare con ChatGPT API

options:
  -h, --help         show this help message and exit
  --key KEY          OpenAI API key
  --importa IMPORTA  Importa i messaggi di conversazione da un file json (.json)
  --sistema SISTEMA  Imposta il contesto della conversazione da un file di testo (.system)
  
ChAI un client python per usare ChatGPT a terminale
```
         
## Installazione ##
Per installare lo script eseguire i seguenti comandi:

```bash
$ git clone https://github.com/r1cc4rd0m4zz4/chAI
$ cd chAI
$ pip install -r requirements.txt
```
