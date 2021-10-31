from flask import Flask, request, send_from_directory, abort
from flask_cors import CORS
from google.cloud import translate_v2 as translate
import Caption_Conversion
import google.cloud.texttospeech as tts
import six
import wave
import os
# from Caption_Conversion import SRT_to_API
app = Flask(__name__)
cors = CORS(app)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/joshi/Documents/programming-files/gcp_private_keys/flaming-translation-monkeys-6eddfb9bf8c5.json'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/SRTtoAPI",methods = ["POST"])
def SRTtoAPI():
    in_file = request.files['file']
    target_lang = request.form['lang']
    gender = int(request.form['voice'])

    text = Caption_Conversion.SRT_to_API(in_file)
    
    translate_client = translate.Client()
    
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    #code for translation
    result = translate_client.translate(text, target_language=target_lang)
    print(result)
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

    #dictionary for each conversion
    #key is language
    # value is list of [voice female,voice male]
    lang_dict = {"en":["en-US-Standard-C","en-US-Standard-A"],
                 "ar":["ar-XA-Standard-A","ar-XA-Standard-B"],
                 "hi":["hi-IN-Standard-A","hi-IN-Standard-B"],
                 "fr":["fr-FR-Standard-A","	fr-FR-Standard-B"]}
    # if target_lang=='ar':
    #     key = "Arabic"
    # else:
    #     key = "Male" # no longer needed since keys and target language is the same
    text_to_wav(voice_name=lang_dict[target_lang][gender],text=result['translatedText'])

    # now a file will be saved on our side called "translated.wav"
    #send speech to front end


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
    return "Hello"


def valid_breakpoint(text, index):
    if text[index] != " ":
        return False
    breakcheck = text[index - 5:index]
    if breakcheck == "break":
        return False
    return True


def break_apart(text):
    print
    tags = len("<speak>  </speak>")
    
    if len(text) < 5000 - tags:
        return ["<speak> " + text + "</speak>"]
    texts = list()
    while(len(text) > 5000 - tags):
        index = 5000 - tags
        while not valid_breakpoint(text, index):
            index -= 1
        texts.append("<speak> " + text[0:index + 1] + "</speak>")
        text = text[index+1:]
    texts.append("<speak> " + text + "</speak>")
    return texts


# Helper Functions (no app routes)
# From: https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#8
def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    # test_text = "<speak>Testing the text to speech and then testing it again and then testing it again and then testing it a third time and how about we test it one more time just to be sure. <break time=\"1s\"/> Please work, and if you don't I will be very upset with you. </speak>"
    texts = break_apart(text)
    counter = 0
    file_list = list()
    outfile = "sounds.wav"
    for txt in texts:
        text_input = tts.SynthesisInput(ssml=txt)
        voice_params = tts.VoiceSelectionParams(
            language_code=language_code, name=voice_name
        )
        audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)
        # Linear16 for wav files
        client = tts.TextToSpeechClient()
        response = client.synthesize_speech(
            input=text_input, voice=voice_params, audio_config=audio_config
        )

        filename = f"text_{counter}.wav"
        counter+=1
        # filename = "translation.mp3"
        with open(filename, "wb") as out:
            out.write(response.audio_content)
            print(f'Generated speech saved to "{filename}"')
        file_list.append(filename)
    # now combine wav files
    data = []
    for infile in file_list:
        w = wave.open(infile,'rb')
        data.append([w.getparams(),w.readframes(w.getnframes())])
        w.close()
    output = wave.open(outfile,'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

# https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
UPLOAD_DIRECTORY = "/download"

@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file."""

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201

if __name__ == '__main__':    
    # text = Caption_Conversion.SRT_to_API("Caption_File/Adi.srt")
    # # txts = break_apart(text)
    # # print(len(txts[1]))
    # # print(txts[1])
    # translate_client = translate.Client()
    
    # if isinstance(text, six.binary_type):
    #     text = text.decode("utf-8")
    # result = translate_client.translate(text, target_language="ar")
    # print(result.keys())
    # text_to_wav("ar-XA-Standard-A",text=result['translatedText'])
    # # # text = SRTtoAPI("Caption_File/Adi.srt", "en")
    app.run(host='0.0.0.0', port=8081)