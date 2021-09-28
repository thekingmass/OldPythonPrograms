from gtts import gTTS
from playsound import playsound


def play_sound(path_audio):
    playsound(path_audio)


def audio_save(text):
    tts = gTTS(text)
    print("Generating audio file..... \n connecting to google text to speech module....")
    tts.save('abc.mp3')
    print('audio saved successfully')

    print("playing  the text as audio:\n")
    print(text)
    play_sound('abc.mp3')
    print("finished")

text = input("enter the message to speak")

audio_save(text)
