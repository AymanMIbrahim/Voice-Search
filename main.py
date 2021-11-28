from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import time

def TextToSpeech(command):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-80)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command) 
    engine.runAndWait()

def SpeechToText():
	r = sr.Recognizer()
	while(1):
		try:
			with sr.Microphone() as source2:
				r.adjust_for_ambient_noise(source2, duration=0.1)
				TextToSpeech("START")
				audio2 = r.listen(source2)
				MyText = r.recognize_google(audio2)
				MyText = MyText.lower()
				return(MyText)
		except sr.RequestError as e:
			TextToSpeech("Sorry, Didn't catch that.")
		except sr.UnknownValueError:
			TextToSpeech("Sorry, Didn't catch that.")





TextToSpeech("Welcome To Google Search By Voice")

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
time.sleep(1)
TextToSpeech("Please, Say what you want to search for, Three Seconds after Hearing the word Start")
Search = driver.find_element_by_name("q")
Text = SpeechToText()
Search.send_keys(Text)
Search.send_keys(Keys.RETURN)
TextToSpeech("Thanks for using our services")


