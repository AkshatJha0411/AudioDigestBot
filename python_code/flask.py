from flask import Flask, request, jsonify
import os
import speech_recognition as sr

app = Flask(__name__)

def convert_to_text(filename):
    if not os.path.isfile(filename):
        return None
    
    # Initialize recognizer
    r = sr.Recognizer()

    try:
        # Open the audio file
        with sr.AudioFile(filename) as source:
            audio = r.record(source)  # Record the entire audio file

            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source, duration=0.5)

        # Recognize speech using Google Speech Recognition
        results = r.recognize_google(audio, show_all=True)

        if "alternative" in results:
            # Get transcriptions
            transcriptions = [alternative["transcript"] for alternative in results["alternative"]]
            # Choose the transcription with the highest confidence
            best_transcription = max(transcriptions, key=len)  # Choose the longest transcription
            return best_transcription
        else:
            return None

    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None

@app.route('/convert-audio', methods=['POST'])
def convert_audio():
    file = request.files['audio']
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    filename = file.filename
    file.save(filename)
    text = convert_to_text(filename)
    os.remove(filename)

    if text:
        return jsonify({'text': text}), 200
    else:
        return jsonify({'error': 'Conversion failed'}), 400

if __name__ == '_main_':
    app.run(debug=True)