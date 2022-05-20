from winsound import PlaySound
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import pyfirmata2

r = sr.Recognizer()

def getAudioFromMicrophone():
   with sr.Microphone() as source:
      
      tts = gTTS('Hola ¿Qué buscas?', lang='es')
      tts.save("audio.mp3")
      playsound("audio.mp3")
      audio = r.listen(source)

      try:

         text = r.recognize_google(audio, language='es')
         tts2 = gTTS("Ejecutar {}".format(text), lang='es')
         tts2.save("audio2.mp3")
         playsound("audio2.mp3")
         print(text)

         if "Google" in text:
             webbrowser.open('https://www.google.com')

         if "encender" in text:
             tts3 = gTTS("encendiendo", lang='es')
             tts3.save("audio3.mp3")
             playsound("audio3.mp3")

             PORT = pyfirmata2.Arduino.AUTODETECT

             board = pyfirmata2.Arduino(PORT)

             board.digital[13].write(1)
             board.digital[12].write(1)

      except:
         ttsfail = gTTS('No te entiendo', lang='es')
         ttsfail.save("audiofail.mp3")
         playsound("audiofail.mp3")

   return audio

getAudioFromMicrophone()