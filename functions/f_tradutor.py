from translate import Translator
import translate
import gtts
from playsound import playsound
from langdetect import detect
import time
import sys
#sys.path.insert(1, "./functions")
import functions.f_corretor as ct

class Tradutor():


    def __init__(self, from_lang, to_lang, frase):
        self.__from_lang = from_lang
        self.__to_lang = to_lang
        self.__frase = frase

    @staticmethod 
    def verifica_idioma(e):
      
      cd_idioma = {"Inglês":"en", "Português":"pt", "Chinês":"zh-hk",
                   "Espanhol":"es", "Francês":"fr-ch", "Árabe":"ar-sa",
                   "Russo":"ro-mo"}

      idioma_selected = e.value 

      idioma = cd_idioma[idioma_selected]

      return idioma



    def traduzir(self):
        #detecta de qual lingua pertence essa frase
        print(self.__from_lang)

        #passa os parametros da linha que será traduzida para a que se quer traduzir
        s=Translator(from_lang=self.__from_lang, to_lang=self.__to_lang)

        #Corrigi a frase

        objeto = ct.Corretor(self.__frase)

        frase_corrigida = objeto.corrigir()

        self.__frase = frase_corrigida

        #traduz a frase
        res = s.translate(self.__frase)
        print(s.from_lang, s.to_lang)
        #imprime a mensagem traduzida
        return res.capitalize()
        #passa os parametros para o audia...
   