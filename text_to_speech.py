from gtts import gTTS
import os


fh = open("text.txt", "r")
friend = fh.read().replace("\n", " ")
language = 'en'

output = gTTS(text=friend, lang=language, slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")