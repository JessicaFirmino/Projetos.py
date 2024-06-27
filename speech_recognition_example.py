import speech_recognition as sr

# Configurar a codificação do stdout para UTF-8
import sys
sys.stdout.reconfigure(encoding='utf-8')

r = sr.Recognizer()

# Inicialização do microfone
with sr.Microphone() as source:
    print("Diga alguma palavra:")
    audio = r.listen(source)

try:
    # Tenta reconhecer o áudio
    text = r.recognize_google(audio, language='pt-BR')
    print(f"Você disse: {text}")
except sr.UnknownValueError:
    print("Não entendi o que você disse!")
except sr.RequestError as e:
    print("Erro de requisição: {0}".format(e))
