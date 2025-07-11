import speech_recognition as sr
import re

while True:
   mic = sr.Recognizer()

   with sr.Microphone() as source:
      mic.adjust_for_ambient_noise(source) # Ajusta o audio conforme o ambiente
      print("Vamos começar, fale alguma coisa ...")

      audio = mic.listen(source)

      try:
         frase = mic.recognize_google(audio, language='pt-BR')

         if(re.search(r'\b' + 'ajudar' + r'\b', format(frase))):
            print('Algo relacionado a ajuda.')


         print(f"Você disse: {frase}")
      except sr.unknownValueError:
         print("Ops. algo deu errado ...")
