# pyrefly: ignore [missing-import]
import pyttsx3

def speak_text(text, rate=150, volume=1.0):
    engine = pyttsx3.init()
    
    # Properties
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    # Voices
    voices = engine.getProperty('voices')
    # Use the first voice by default
    engine.setProperty('voice', voices[0].id)
    
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def main():
    print("--- Python Text-to-Speech ---")
    while True:
        text = input("\nEnter text to speak (or 'q' to quit): ")
        if text.lower() == 'q':
            break
        
        try:
            speak_text(text)
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure 'pyttsx3' is installed: pip install pyttsx3")

if __name__ == "__main__":
    main()
