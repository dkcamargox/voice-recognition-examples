# Responds to a name
# https://pypi.org/project/SpeechRecognition/
from sys import exit
import re
import speech_recognition
import pyttsx3

# setting google voice	
engine = pyttsx3.init()
voice_id = "com.apple.speech.synthesis.voice.alex" 
engine.setProperty('voice', voice_id)

# setting recognizer 


quit = False


while quit == False:
	understood = False
	while understood == False:
		with speech_recognition.Microphone() as source:
			print("What's your name?")
			engine.say("What's your name?")
			engine.runAndWait()
			print('now!')
			recognizer = speech_recognition.Recognizer()
			audio = recognizer.listen(source)

		# Recognize speech using Google Speech Recognition
		try:
			words = recognizer.recognize_google(audio)
			print(f"you said: {words}")
		except speech_recognition.UnknownValueError:
			print("Hun? Can you repeat?")
			engine.say("Hun? Can you repeat?")
			engine.runAndWait()
		else:
			understood = True


	# Respond to speech
	matches = re.search("my name is (.*)", words)
	if matches:
		print(f"Hey, {matches[1]}.")
		engine.say(f"Hey, {matches[1]}.")
		engine.runAndWait()
	else:
		print("Hey, you.")
		engine.say("Hey you.")
		engine.runAndWait()

	understood = False
	while understood == False:
		with speech_recognition.Microphone() as source:
			print("Go again?")
			engine.say("Go again?")
			engine.runAndWait()

			print('now!')

			recognizer = speech_recognition.Recognizer()
			audio2 = recognizer.listen(source)

			# Recognize speech using Google Speech Recognition
			try:
				words = recognizer.recognize_google(audio2)
				print(f'you said: {words}')
			except speech_recognition.UnknownValueError:
				print("Hun? Can you repeat?")
				engine.say("Hun? Can you repeat?")
				engine.runAndWait()
			else:
				understood = True

		matches = re.search("no", words.lower())
		if matches:
			print("Ok, bye!")
			engine.say("Ok, bye!")
			engine.runAndWait()
			quit = True
		else:
			print('Ok, then!')
			engine.say("Ok, then!")
			engine.runAndWait()