from PIL import Image 
import cv2
from pytesseract import pytesseract 


def camImagem(img):
    print(img)
    imagem = cv2.imread(img)
    caminho = r"C:/Users/santo/AppData/Local/Programs/Tesseract-OCR"
    pytesseract.tesseract_cmd = caminho + r'/tesseract.exe'
    texto = pytesseract.image_to_string(imagem)
    print(texto)
    return texto
#print( pytesseract.image_to_string( Image.open('C:/Users/santo/OneDrive/Imagens/Saved Pictures/teste.jpg'), lang='por') )