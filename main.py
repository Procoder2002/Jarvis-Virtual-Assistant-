import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()



def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link  = music_library.music[song]
        webbrowser.open(link)
        
    else:
        #Let open ai handle the request
        pass
        
if __name__ == "__main__":
    speak("Initializing Jarvis..")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from microphone
        
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = r.listen(source, timeout = 3, phrase_time_limit = 3)
                word = r.recognize_google(audio)
                
            if(word.lower() == "jarvis"):
                speak("Yes ")
                #listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Jarvis Active")
                    audio = r.listen(source, timeout = 3, phrase_time_limit = 3)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
        
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as s:
            print(f"Could not request results; {s}")
        except Exception as e:
            print(f"Error: {e}")
        