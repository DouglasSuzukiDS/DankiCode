import speech_recognition as sr
import re
import pyttsx3 # Faz a maquina esconder a gente

nome = ''

while True:
   mic = sr.Recognizer()

   with sr.Microphone() as source:
      engine = pyttsx3.init()
      engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana') # Define uma voz

      mic.adjust_for_ambient_noise(source) # Ajusta o audio conforme o ambiente
      print("Vamos começar, fale alguma coisa ...")

      audio = mic.listen(source)

      try:
         frase = mic.recognize_google(audio, language='pt-BR')

         if(re.search(r'\b' + 'ajudar' + r'\b', format(frase))):
            engine.say('Ajuda')
            engine.runAndWait()

            print('Algo relacionado a ajuda.')
         elif(re.search(r'\b' + 'meu nome é' + r'\b', format(frase))):
            t = re.search('meu nome é (.*)', format(frase))

            nome = t.group(1)

            print(f"Seu nome é {nome}")

            engine.say(f'Seu nome é {nome}')
            engine.runAndWait()

         print(f"Você disse: {nome}")

         engine.say(f"Onome falado foi: {nome}")
      except sr.unknownValueError:
         print("Ops. algo deu errado ...")
