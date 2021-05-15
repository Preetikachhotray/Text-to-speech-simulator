from gtts import gTTS
import os
friend = "there are infinite number of trees. i cant count them. sorry."

language = 'en'

output = gTTS(text=friend, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")