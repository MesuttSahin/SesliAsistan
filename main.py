import speech_recognition as sr
import pyttsx3
from datetime import datetime


engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)  
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Dinliyor... (Konuşun!)")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source, timeout=None,phrase_time_limit=10)  

        try:
            command = recognizer.recognize_google(audio, language="tr-TR")
            print("Sen:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sesini anlayamadım.")
            return ""
        except sr.RequestError:
            speak("Google servisine bağlanılamıyor.")
            return ""
        except Exception as e:
            speak("Bir hata oluştu: " + str(e))
            return ""

def process_command(command):
    if not command:
        return

    if "merhaba" in command:
        speak("Merhaba! Nasılsın?")
    elif "saat kaç" in command:
        speak("Saat " + datetime.now().strftime("%H:%M"))
    elif "adın ne" in command:
        speak("Ben basit bir sesli asistanım.")
    elif "kapat" in command:
        speak("Görüşürüz!")
        exit()
    else:
        speak("Bu komutu anlamadım.")

while True:
    komut = listen()
    if komut:
        process_command(komut)
