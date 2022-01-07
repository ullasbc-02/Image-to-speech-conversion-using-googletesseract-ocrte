# Import the Gtts module for text
# to speech conversion
from gtts import gTTS

# import os module to start the audio file
import os

mytext = 'Ullas Good boi'

# Language we want to use
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("output.mp3")

# Play the converted file
os.system("start output.mp3")