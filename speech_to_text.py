import speech_recognition as sr


def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        print("Listening to audio...")
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Error with the service: {e}")

if __name__ == "__main__":
    file_path = "sample.wav"
    transcribe_audio(file_path)
