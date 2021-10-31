from flask import Flask, request, send_from_directory, abort
from flask_cors import CORS
from google.cloud import translate_v2 as translate
import Caption_Conversion
import google.cloud.texttospeech as tts
import six
import wave
import os
import contextlib
# from Caption_Conversion import SRT_to_API
app = Flask(__name__)
cors = CORS(app)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:/joshi/Documents/programming-files/gcp_private_keys/flaming-translation-monkeys-942679b86bf1.json"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/SRTtoAPI",methods = ["POST"])
def SRTtoAPI():
    in_file = request.files['file']
    target_lang = request.form['lang']
    gender = int(request.form['voice'])
    # sync = int(request.form['sync'])
    # endtime = int(request.form['duration'])*1000 # in ms
    text,caption_end = Caption_Conversion.SRT_to_API(in_file)
    # we don't use caption_end; kept as legacy
    translate_client = translate.Client()
    
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    #code for translation
    result = translate_client.translate(text, target_language=target_lang)
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

    #dictionary for each conversion
    #key is language
    # value is list of [voice female,voice male]
    lang_dict = {"en":["en-US-Standard-C","en-US-Standard-A"],
                 "ar":["ar-XA-Standard-A","ar-XA-Standard-B"],
                 "hi":["hi-IN-Standard-A","hi-IN-Standard-B"],
                 "fr":["fr-FR-Standard-A","fr-FR-Standard-B"]}
    # if target_lang=='ar':
    #     key = "Arabic"
    # else:
    #     key = "Male" # no longer needed since keys and target language is the same
    text_to_wav(voice_name=lang_dict[target_lang][gender],text=result['translatedText'],sync=sync,endtime=caption_end)

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
    return send_from_directory(FILE_DIR, "sounds1.wav", as_attachment=True)
    # if sync:
    #     return send_from_directory(FILE_DIR, "sounds1.wav", as_attachment=True)
    # else:
    #     return send_from_directory(FILE_DIR, "sounds.wav", as_attachment=True)


def sync(wave_file,ratio):
    # sync wave file by speeding up the video
    CHANNELS = 1
    swidth = 2
    Change_RATE = ratio

    spf = wave.open(wave_file, 'rb')
    RATE=spf.getframerate()
    signal = spf.readframes(-1)
    spf.close()

    wf = wave.open(FILE_DIR+"sounds1.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(swidth)
    wf.setframerate(RATE*Change_RATE)
    wf.writeframes(signal)
    wf.close()

def valid_breakpoint(text, index):
    if text[index] != " ":
        return False
    breakcheck = text[index - 5:index]
    if breakcheck == "break":
        return False
    return True


def break_apart(text):
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

# https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
FILE_DIR = "files/"

# Helper Functions (no app routes)
# From: https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#8
# TODO: Option to convert each subtitle into its own wav and merge all of them together
def text_to_wav(voice_name: str, text: str,sync:int,endtime: int):
    language_code = "-".join(voice_name.split("-")[:2])
    # test_text = "<speak>Testing the text to speech and then testing it again and then testing it again and then testing it a third time and how about we test it one more time just to be sure. <break time=\"1s\"/> Please work, and if you don't I will be very upset with you. </speak>"
    texts = break_apart(text)
    counter = 0
    file_list = list()
    outfile = FILE_DIR + "sounds.wav"
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

        filename = FILE_DIR + f"text_{counter}.wav"
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
        # Remove unnecessary wav files
        try: 
            os.remove(infile)
        except:
            print("Unknown error...")
    output = wave.open(outfile,'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
    with contextlib.closing(wave.open(outfile,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        audio_time = frames / float(rate)
    
    
    ratio = (audio_time*1000)/endtime
    print(ratio)
    sync(wave_file=outfile,ratio=ratio)

@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(FILE_DIR, path, as_attachment=True)

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