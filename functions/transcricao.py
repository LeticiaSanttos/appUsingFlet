import gtts
from playsound import playsound
import speech_recognition as sr

def transcrever():
   rec = sr.Recognizer()
   with sr.Microphone() as mic:
       rec.adjust_for_ambient_noise(mic)
       audio = rec.listen(mic)
       with open('testeaudio.wav', 'wb') as f:
           f.write(audio.get_wav_data())
       
       texto = rec.recognize_google(audio, language='pt-br')
       return texto

def ouvir():
    playsound('testeaudio.wav')