import gtts
from playsound import playsound
#from langdetect import detect

import os

#passa os parametros para o audia
def audiodescricao(resp, idioma):
   
   fala = gtts.gTTS(resp, lang=idioma)
#salva o audio
   
   caminho = r"assets/audio/fala.mp3"
   fala.save(caminho)
#executa o audio

   playsound(caminho)
   os.remove(caminho)