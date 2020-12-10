# Responds to a greeting
# https://pypi.org/project/SpeechRecognition/

import speech_recognition
import pyttsx3

# setting google voice	
engine = pyttsx3.init()
voice_id = "com.apple.speech.synthesis.voice.alex" 
engine.setProperty('voice', voice_id)

# Obtain audio from the microphone
def obtainAudio():
	recognizer = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as source:
		text = "Say Something!"
		print(text)
		engine.say(text)
		engine.runAndWait()
		print('now!')
		audio = recognizer.listen(source)
		try:
			words = recognizer.recognize_google(audio)
		except speech_recognition.UnknownValueError:
			print("Hun?")
			return []
		else:
			return words

words = obtainAudio()
# Recognize speech using Google Speech Recognition

print(f"you said: {words}")

# Respond to speech
if "hello" in words:
	text = "Hello to you too!"
	
	print(text)
	engine.say(text)
	engine.runAndWait()

elif "how are you" in words:
	text = "I am well, thanks!"
	
	print(text)
	engine.say(text)
	engine.runAndWait()

elif "goodbye" in words:
	text = "Goodbye to you too!"
	
	print(text)
	engine.say(text)
	engine.runAndWait()

elif "brother" in words:
	text = "Ugly!!"
	print(text)
	engine.say(text)
	engine.runAndWait()
else:
	text = "You are cool!!"
	print(text)
	engine.say(text)
	engine.runAndWait()