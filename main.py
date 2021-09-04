# Import Dependencies
import speech_recognition as sr
from pywinauto.application import Application

# Speech Recogniser
def speech_recognizer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Recognize
    try:
        speech = r.recognize_google(audio, language="en-in")
        print(speech)
        # Pywinauto Process
        app = Application(backend='uia').start("notepad.exe")
        # Notepad Window
        notepad_window = app.UntitledNotepad
        notepad_window.type_keys(speech, with_spaces=True)

    except Exception as e:
        print("Unable to recognize, please say that again.")

speech_recognizer()