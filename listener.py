#Listner=> Listens from microphone
import speech_recognition as sr
import pyaudio


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        # print(e)
        print("Say that again please...")
        takeCommand()


    return query


print(takeCommand())