import speech_recognition as sr
import random
import time
import re



level = input("Zorluk seviyesini seçin (kolay, orta, zor): ").lower()
def sesi_yakala():
    # Sesi mikrofondan yakala
    mic = sr.Microphone()
    # Sesi tanıma için hazırla
    recognizer = sr.Recognizer()
    # Sesi tanıma
    with mic as audio_file:
        print("konuş🥀🙏😭")
        # Ortam gürültüsünü ayarla
        recognizer.adjust_for_ambient_noise(audio_file, duration=1)
        # Sesi dinle
        audio_data = recognizer.listen(audio_file)
        time.sleep(3)
        print("Sesin elon musk'a iletiliyor🥀🙏😭")
        recognizer.recognize_google(audio_data, language="en-GB")
        try:
            audio_text = recognizer.recognize_google(audio_data, language="en-GB").lower()
            print(f"Telafuzunuz: {audio_text}")
        except sr.UnknownValueError:
            print("Ses anlaşılamadı, lütfen tekrar deneyin.")
        except sr.WaitTimeoutError:
            print("Ses dinleme süresi doldu, lütfen tekrar deneyin.")
        return recognizer.recognize_google(audio_data, language="en-GB").lower()



seviyeler = {
    "kolay": ["what","hello","green","white","cash"],
    "orta": ["what's up","hello there","green light","white house","money bag"],
    "zor": ["what's going on","hello there my friend","green light means go","white house is the president's residence","money bag is full of cash"]
}


def oyun(level):
    global audio_text
    if level in seviyeler:
        kelimeler = seviyeler[level]
        kelime = random.choice(kelimeler)
        print(f"Kelime: {kelime}")
        if kelime == sesi_yakala():
            print("Doğru telafuz ettiniz! 🥳")
        else:
            print(f"Yanlış telafuz ettiniz!")
    else:
        print("Sen sistemden falan kaçmaya çalışıyon heralde?")



oyun(level)
    

        
