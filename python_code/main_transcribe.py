import os
import speech_recognition as sr

def convert_to_text(filename):
    if not os.path.isfile(filename):
        print("File does not exist.")
        return None
    
    # Initialize recognizer
    r = sr.Recognizer()

    try:
        # Open the audio file
        with sr.AudioFile(filename) as source:
            print("Reading audio file...")
            audio = r.record(source)  # Record the entire audio file

            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.5)

        # Recognize speech using Google Speech Recognition
        print("Converting speech to text...")
        results = r.recognize_google(audio, show_all=True)

        if "alternative" in results:
            # Get transcriptions
            transcriptions = [alternative["transcript"] for alternative in results["alternative"]]
            # Choose the transcription with the highest confidence
            best_transcription = max(transcriptions, key=len)  # Choose the longest transcription
            return best_transcription
        else:
            print("No transcription found.")
            return None

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")

    return None

filename = "./backend/uploads/audio.wav"  # directory where .wav audio file is stored
text = convert_to_text(filename)

if text:
    print("Transcription:", text)
else:
    print("Conversion failed.")