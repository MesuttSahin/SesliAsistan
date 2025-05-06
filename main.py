import speech_recognition as sr
import pyttsx3
import os
import subprocess
from datetime import datetime

# Sesli yanıt motoru
engine = pyttsx3.init()


def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()


# Ses tanıma
recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Dinliyor... (Konuşun!)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        try:
            command = recognizer.recognize_google(audio, language="tr-TR")
            print("Sen:", command)
            return command.lower()
        except Exception as e:
            print("Hata:", str(e))
            return ""


def open_program(program_name):
    """Program açma fonksiyonu"""
    program_map = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": r"C:\Windows\system32\notepad.exe",
        "spotify": r"C:\Users\Kullanıcı\AppData\Roaming\Spotify\Spotify.exe",
        "hesap makinesi": "calc"
    }

    if program_name in program_map:
        try:
            path = program_map[program_name]
            if path == "calc":  # Windows hesap makinesi
                os.system("calc")
            else:
                subprocess.Popen(path)
            speak(f"{program_name} açılıyor...")
        except Exception as e:
            speak(f"{program_name} açılırken hata oluştu: {str(e)}")
    else:
        speak("Bu programı açmayı henüz bilmiyorum.")


def process_command(command):
    if not command:
        return

    # Program açma komutları
    if "chrome aç" in command:
        open_program("chrome")
    elif "notepad aç" in command:
        open_program("notepad")
    elif "spotify aç" in command:
        open_program("spotify")
    elif "hesap makinesi aç" in command:
        open_program("hesap makinesi")

    # Diğer komutlar
    elif "merhaba" in command:
        speak("Merhaba! Sana nasıl yardımcı olabilirim?")
    elif "saat kaç" in command:
        speak("Saat " + datetime.now().strftime("%H:%M"))
    elif "kapat" in command:
        speak("Görüşürüz!")
        exit()
    else:
        speak("Bu komutu anlamadım.")


# Ana döngü
if __name__ == "__main__":
    speak("Sesli asistan başlatıldı. Komutlarınızı bekliyorum...")
    while True:
        command = listen()
        if command:
            process_command(command)