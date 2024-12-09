import speech_recognition as sr

def listen_for_keyword():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for the activation keyword...")

        while True:
            try:
                activationkeyword = "ok google"
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                text = recognizer.recognize_google(audio)
                if activationkeyword in text.lower():
                    print("Activation keyword detected! Now listening...")
                    start_transcription()
                    
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")

def start_transcription():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something, I'm listening...")

        while True:
            try:
                # Listen for audio after the activation keyword
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                transcribe = open("transcript.csv", "w")
                transcribe.write(text)
                transcribe.close()
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start.")
            break  # Stop after one phrase or make this loop for continuous transcription

# Start by listening for the keyword
listen_for_keyword()

