# i18nify-backend

This is the backend service of [i18nify](https://github.com/batrdn/i18nify),
providing the endpoints to check if a word is valid and generate translation key.

### Word validation

`/get-valid-words` endpoint provides the capability to check if a word is valid. 
In the body of the POST request, an array of words are sent, by which the backend service returns the valid words from that array.

To check if a word is valid, `pyenchant` library is used, which checks a word against a dictionary.
By default, `pyenchant` comes with English dictionaries, and dictionaries in other languages can also be imported.

#### Current supported languages:
- English
- German
- Mongolian
- Russian

### How to run?
`docker-compose up`. The service will run at the port 5000.

