import pyttsx3


def text_to_speech(text, file_name ):
    engine = pyttsx3.init()
    engine.say(text)
    engine.save_to_file(text, file_name + ".mp3")
    engine.runAndWait()

def get_and_setvoices(engine, voice_id):
    voices = engine.getProperty('voices')

    if 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        print("Invalid voice selection. Using the default voice.")


if __name__ == '__main__':
    print("-----------------------------------")
    print("\033[1m*****Welcome to Text to Audio!*****\033[0m")

    print("\033[1m  ****Created By: Raman Yadav****\033[0m")
    print("-----------------------------------")

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')


    print("Available voices:")
    for i, voice in enumerate(voices):
        print(f"{i}. {voice.name}")


    while True:
        try:
            voice_id = int(input("Enter the voice number (0, 1): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        get_and_setvoices(engine, voice_id)

        file_name = input("Enter the FIle name:")
        x = input("Enter the text: ")
        text_to_speech(x, file_name)
        continue_input = input('Do you want to continue?(yes/no): ')
        if continue_input.lower() == "no":
            break
