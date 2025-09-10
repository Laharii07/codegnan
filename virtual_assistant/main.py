#import required libraries
import pyttsx3
import os
import webbrowser
import speech_recognition as sr
import datetime
import urllib.parse

#create engine for text to speech
engine = pyttsx3.init()
engine.setProperty('rate',175)

# speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# command taking function
def take_command()->str:
    listner = sr.Recognizer()
    with sr.Microphone() as source:
        print("adjusting for ambient noise.....")
        listner.adjust_for_ambient_noise(source,duration=1)
        print("Listening..........")
        try :
            audio = listner.listen(source,timeout=5,phrase_time_limit= 20)
            command  = listner.recognize_google(audio) # speech to text
            command = command.lower()
            print("You Said: ",command)
            return command 
        except sr.WaitTimeoutError:
            print("Listening time out while waiting for phrase to start")
            return ""
        except sr.UnknownValueError:
            print("Sorry,I could not understand your speech")
            return ""
        except sr.RequestError:
            print("Could not request results from google speech services")
            return ""
        
#create run assistant function
def run_assistant():
    command = take_command()

    #in command it have time word
    if "time"  in command:
        time = datetime.datetime.now().strftime("%I : %M %p")
        speak(f"The current time is {time}")

    # date in command , it returns the current date
    elif "date" in command:
        date = datetime.date.today()
        speak(f"Today date is {date}")

    # open notepad command
    elif "open notepad" in command:
        speak("opening notepad")
        os.system('notepad')

    # open youtube command
    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://youtube.com/")
    
    #search for any query 
    elif "hey lucky" in command:
        query = command.replace("hey lucky","").strip()
        if query:
            encoded_query = urllib.parse.quote(query)  # encode special characters
            url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open(url)
    # stop command or bye
    elif "bye" in command or "stop"  in command:
        speak("Okay bye bye")
        exit()
    else:
        speak("I am here to assist you, ask commands like opening youtube, notepad, chrome and about date or time ")


# main function
if __name__ == "__main__":
    user_name = input("Enter your name")
    speak(f" Hello {user_name}, I am here to assist you with basic things. Tell me, how can I assist you? ") 
    while True:
        run_assistant()





