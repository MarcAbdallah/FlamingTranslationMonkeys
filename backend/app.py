from flask import Flask, request, send_from_directory
from flask_cors import CORS
from google.cloud import translate_v2 as translate
import Caption_Conversion
import google.cloud.texttospeech as tts
import six
# from Caption_Conversion import SRT_to_API
app = Flask(__name__)
cors = CORS(app)

DOWNLOAD='/download'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/audio")
def audio():
    try:
        return send_from_directory(DOWNLOAD, "test.txt", as_attachment=True)
    except:
        return "bye"

@app.route("/SRTtoAPI",methods = ["POST","GET"])
def SRTtoAPI(in_file, target_lang):
    text = Caption_Conversion.SRT_to_API(in_file)
    
    translate_client = translate.Client()
    
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
        
    result = translate_client.translate(text, target_language=target_lang)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    # in_file is the SRT file from yo marc 
    # in_file = request.form['formData'] # get's formData field from FileUpload.js line 27
    # API_text = SRT_to_API(in_file) # get text for API
    # TODO: now call G-Cloud API for text to voice with input = API_text
    # TODO: we will probably have to make a dictionary with the language we want to translate to as
    # the keys and the language code as the value (ex. english -> en, korean -> ko, 'auto' can be
    # used as the src, but the dest needs to be specified) 

    # googletrans.languages returns a library with the key to value language codes
    
    # https://py-googletrans.readthedocs.io/en/latest/
    # from googletrans import Translator
    # translator = Translator(service_urls=['translate.google.com',]))
    # translation = translator.translate(text, dest='en', src='auto', **kwargs)
    
    #code for translation
    

    #code for text to speech
    #dictionary for each conversion
    lang_dict = {"Male":"en-US-Standard-A",
                 "Female":"en-US-Standard-C",
                 "Female_Arabic":"ar-XA-Standard-A",
                 "Male_Arabic":"ar-XA-Standard-B"}
    text_to_wav(voice_name=lang_dict['Female_Arabic'],<output_from_translation>)
    #send speech to front end
    return "Hello"


# Helper Functions (no app routes)
# From: https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#8
def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )

    filename = f"{language_code}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)