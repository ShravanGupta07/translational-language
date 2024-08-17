import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import playsound
import os

# Initialize the translator object
translator = Translator()


# Function to translate English text to Tamil
def translate_to_tamil(input_text):
    translation = translator.translate(input_text, src='en', dest='ta')
    return translation.text


# Function to convert translated Tamil text to speech and play it
def play_tamil_audio(tamil_text):
    tts = gTTS(text=tamil_text, lang='ta', slow=False)
    audio_file = "temporary_audio.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


# Main loop to continuously listen, translate, and convert text to speech
while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.pause_threshold = 1
        captured_audio = recognizer.listen(source, phrase_time_limit=10)

    try:
        print("Converting speech to text...")
        recognized_text = recognizer.recognize_google(captured_audio, language='en')

        print("Translating text to Tamil...")
        tamil_translation = translate_to_tamil(recognized_text)

        print("Generating Tamil speech...")
        play_tamil_audio(tamil_translation)

    except Exception as error:
        print(f"Error occurred: {error}")
