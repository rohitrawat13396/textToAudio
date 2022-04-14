from gtts import gTTS
from playsound import playsound


audio = "demo_speech.mp3"
language = "en"

sp = gTTS(text = "Hi Rohit! Have a beautiful day.", lang = language, slow = False)

sp.save(audio)
playsound(audio)