from gtts import gTTS
from io import BytesIO
from PyPDF2 import PdfReader

path =open("k.pdf",'rb')
file = PdfReader(path)

text = ""
for page in file.pages:
    text += page.extract_text() + "\n"

stream = BytesIO()
voice = gTTS(text=text, lang='en', slow=False)
voice.save("test.wav")