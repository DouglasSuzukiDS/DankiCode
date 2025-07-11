import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone() as source:
   mic.adjust_for_ambient_noise(source) # Ajusta o audio conforme o ambiente
   print("Vamos começar, fale alguma coisa ...")

   audio = mic.listen(source)

   try:
      frase = mic.recognize_google(audio, language='pt-BR')
      print(f"Você disse: {frase}")
   except sr.unknownValueError:
      print("Ops. algo deu errado ...")
