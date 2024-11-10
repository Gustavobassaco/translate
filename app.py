from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    target_lang = data.get('target_lang', 'en')  # Define inglês como padrão

    try:
        translation = translator.translate(text, dest=target_lang)
        return jsonify({'translated_text': translation.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "API de Tradução com Flask e Googletrans"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
