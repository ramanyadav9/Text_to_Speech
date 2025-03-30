import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def save_text_audio(text, file_name):
    engine = pyttsx3.init()
    # Join all entered texts into a single string
    full_text = " ".join(texts)

    engine.save_to_file(full_text, file_name + ".mp3")
    engine.runAndWait()

if __name__ == '__main__':
        print("-----------------------------------")
        print("\033[1m*****Welcome to Text Talking!*****\033[0m")

        print("\033[1m****Created By: Raman Yadav****\033[0m")
        print("-----------------------------------")
        print("\033[1m [If want quit, Type File Name 'Q']  \033[0m")
        file_name = input("Enter the FIle name:")
        texts = []  # List to store entered texts
        while True:
            x = input("Enter the text: ")

            if x.lower() == "q":
                break

            texts.append(x)
            text_to_speech(x)
        save_text_audio(texts, file_name)
        text_to_speech("Goodbye!")

