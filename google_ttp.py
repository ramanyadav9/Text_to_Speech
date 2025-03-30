from google.cloud import texttospeech

def get_google_voices():
    client = texttospeech.TextToSpeechClient()
    voices = client.list_voices().voices
    return voices

def text_to_speech_google(text, file_name, voice_name):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Set the voice based on the provided voice_name
    voice = texttospeech.VoiceSelectionParams(
        name=voice_name,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(file_name + ".wav", "wb") as out_file:
        out_file.write(response.audio_content)

if __name__ == '__main__':
    print("-----------------------------------")
    print("\033[1m*****Welcome to Text to Audio!*****\033[0m")
    print("\033[1m****Created By: Raman Yadav****\033[0m")
    print("-----------------------------------")

    voices = get_google_voices()

    print("Available Google Cloud voices:")
    for i, voice in enumerate(voices[:10]):  # Display the first 10 voices
        print(f"{i}. {voice.name}")

    while True:
        try:
            voice_id = int(input("Enter the voice number (0, 1, 2, ...): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= voice_id < len(voices):
            voice_name = voices[voice_id].name
        else:
            print("Invalid voice selection. Using the default voice.")
            voice_name = "en-US-Wavenet-D"

        file_name = input("Enter the File name:")
        text = input("Enter the text: ")
        text_to_speech_google(text, file_name, voice_name)

        continue_input = input('Do you want to continue? (yes/no): ')
        if continue_input.lower() == "no":
            break
