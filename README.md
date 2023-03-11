# ChAI

## Introduzione ##
Un'interfaccia testuale per tenere in una finestra di terminale ChatGPT di OpenAI tramite l'API.

## Vantaggi ##
 * Utilizzo essenziale della API Key di OpenAI, niente frozoli o interfacce web.
 * Imposta la chiave API OpenAI in una variabile d'ambiente (OPENAI_API_KEY) o come parametro.
 * Comando `clear` per iniziare una nuova chat salvando la precende te in un JSON.
 * Inserire `quit` per salvare la chat in un JSON e tornare al terminale.
 * Ripristinare una precedente chat impostando il parametro con il nome del file JSON di una precedente chat!

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
  --importa IMPORTA  Importare un file json con i messaggi
  
ChAI un client python per usare ChatGPT a terminale
```
         
## Installazione ##
Per installare ed utilizzare lo script eseguire i seguenti comandi:

```bash
$ git clone https://github.com/r1cc4rd0m4zz4/chAI
$ cd chAI
$ pip install -r requirements.txt
$ python ch.py
```

![visitors](https://visitor-badge.glitch.me/badge?page_id=r1cc4rd0m4zz4/chAI&left_color=green&right_color=red)
