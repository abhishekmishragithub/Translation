'''
Application  : Language Translation
Author: Abhishek Mishra
Version : 1.0
'''

from flask import Flask, request, jsonify
from googletrans import Translator

translator = Translator()

app = Flask(__name__)

@app.route('/')
def index():
    return "You get nothing here ! Hit request to -> /translation"


@app.route('/translation', methods=['POST'])
def translate_text():
    response = dict()
    data = request.get_json()
    origin_lang = data['input']
    dest_lang = data['dest']
    detect_type = translator.detect(origin_lang).lang
    detect_confidence = translator.detect(origin_lang).confidence
    trans_lang = translator.translate(origin_lang, dest=dest_lang).text

    response['original text'] = origin_lang
    response['detected language'] = detect_type
    response['confidence'] = detect_confidence
    response['translated text'] = trans_lang
    print(response)
    return jsonify(response) #'{"title":12}'

if __name__ == '__main__':
    app.run(debug=True)