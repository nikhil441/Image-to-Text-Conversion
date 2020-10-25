# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract
#translates into the mentioned language
from googletrans import Translator
# opening an image from the source path
pytesseract.pytesseract.tesseract_cmd = #Location of tesseract-ocr installation in system    
img=Image.open("Enter input image path here")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
p = Translator()
# translates the text into any language
k = p.translate(result, dest='any language of your choice')
#converts the result into string format
translated = str(k.text)
print (translated)
