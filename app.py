from flask import Flask, request, json
from utils.word_checker import check_word

app = Flask(__name__)

@app.route('/get-valid-words', methods=['POST'])
def get_valid_words():
    if request.method == 'POST':
        data = request.get_json()
        result = []
        for word in data['words']:
            word_length = len(word.split())
            
            if word_length > 1:
                is_valid = False
                for sentence_word in word.split():
                    is_valid_word = check_word(sentence_word)

                    # If it's a sentence contains a valid word, then return the whole sentence,
                    # because it may be a word with a variable placeholder.

                    if is_valid_word:
                        is_valid = True
                        break

                if is_valid:
                    result.append(word)
                    continue

            is_word = check_word(word)
            if is_word:
                result.append(word)

        return json.dumps({
            "validWords": list(set(result))
        })
