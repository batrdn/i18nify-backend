from flask import Flask, request, json
from api.word_checker import check_word
from api.translation_key_generator import generate_translation_key

app = Flask(__name__)

@app.route('/get-valid-words', methods=['POST'])
def get_valid_words():
    if request.method == 'POST':
        data = request.get_json()
        result = []
        for word in data['words']:
            is_word = check_word(word)
            if is_word:
                result.append(word)
        return json.dumps({
            "validWords": list(set(result))
        })

@app.route('/translation-key-generator')
def translation_key():
    return json.dumps({
        "translationKey": generate_translation_key(request.args.get("word"))
    })
