from gtts import gTTS
tts = gTTS('Hallo, wie geht es dir', lang='de')
tts.save('german.mp3')