import language_tool_python

class Corretor():

    def __init__(self, frase):
        self.__frase = frase
        self.tool = language_tool_python.LanguageToolPublicAPI('pt-BR')


    def corrigir(self):
        # Verificação e correção da entrada do usuário
        self.__correcao = self.tool.correct(self.__frase)
        print(self.__frase)
        print(self.__correcao)
        
        return self.__correcao