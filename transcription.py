from vosk import Model, KaldiRecognizer
import wave
import json

def transcribe_audio(audio_file):
    # Load the Vosk model
    model = Model("vosk-model-small-en-in-0.4")
    
    # Open the audio file
    wf = wave.open(audio_file, "rb")
    
    # Check if the audio file has the correct format
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        return None
    
    # Create a Vosk recognizer
    recognizer = KaldiRecognizer(model, wf.getframerate())
    recognizer.SetWords(True)
    
    # Process the audio file
    transcription = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcription.append(result.get("text", ""))
    
    # Get the final result
    final_result = json.loads(recognizer.FinalResult())
    transcription.append(final_result.get("text", ""))
    
    # Join all parts of the transcription
    full_transcription = " ".join(transcription)
    
    return full_transcription

# Example usage
if __name__ == "__main__":
    audio_file_path = "path/to/your/audio/file.wav"
    transcribed_text = transcribe_audio(audio_file_path)
    print("Transcribed Text:")
    print(transcribed_text)