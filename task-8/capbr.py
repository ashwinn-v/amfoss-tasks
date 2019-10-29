from PIL import Image
import pytesseract                                   #used to import pytesseract library

expression = pytesseract.image_to_string(Image.open('plus2.png'), config='--psm 7')
print(expression) 
print(eval(expression))