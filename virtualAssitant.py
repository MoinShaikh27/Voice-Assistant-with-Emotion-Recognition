from deepface import DeepFace
import cv2
import pyttsx3#python text to speech

import pyaudio
import os
import wikipedia#for wikipedia search
import datetime
import randfacts
import random
import smtplib#for emails sending
import webbrowser#for open browser-build in module
import requests #for news reading
from requests import get


import speech_recognition as sr
# print(sr.__version__ )
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)#female voice-voices[1].id
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
#print(rate)#rate of speed of assistent is 200 here
engine.setProperty('rate',180)#we slow speed of assistent here
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello! i am your your Chotu please tell me how may i help you")


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('moinshaikhabc0@gmail.com', 'eryjmupkvvmydzlg')
    server.sendmail('moinshaikhabc0@gmail.com', to, content)
    server.close()

def takecommand():#it takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        #r.adjust_for_ambient_noise(source)
        #r.pause_threshold=1#1 sec ka time diya gya h sunne k liye assistent ko
        r.energy_threshold=20000#it can detect very low voice too
        audio= r.listen(source,timeout=10,phrase_time_limit=8)


        try:
            print("Recognizing......")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")
            return query


        except Exception as e:
            print(e)
            print("say that again please....")
            return "None"#return a simple stament of word name
        



if __name__ == '__main__':
    wishme()
    while True:
        query=takecommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)
        elif 'facts' and 'fact' in query:
            speak("sure mam...")
            x=randfacts.get_fact()
            print(x)
            speak(f"did you know{x}")
            y = randfacts.get_fact()
            print(y)
            speak(y)
            z = randfacts.get_fact()
            print(z)
            speak(z)
        
        elif "gate result" in query:
            doc_dr='C:\\Users\\moink\\OneDrive\\Desktop\\Gate result'
            result=os.listdir(doc_dr)
            os.startfile(os.path.join(doc_dr,result[0]))
            

        elif 'ip address' in query:
            print("MOIN")
            ip=get('https://api.ipify.org').text
            print(f"your ip address is{ip}")
            speak(f"your ip address is {ip}")
        elif 'date of today' in query:
            today_date=datetime.datetime.now()#%d-day of month,%B-month,%y=year
            speak("today is"+today_date.strftime("%d")+"of"+today_date.strftime("%B")+"and its currently"+today_date.strftime("%Y"))
            print(today_date.strftime("%d %B %Y"))
        elif 'current time' in query:
            today_time=datetime.datetime.now()
            speak("currently time is "+today_time.strftime("%H")+"hours "+today_time.strftime("%M")+"minutes and "+today_time.strftime("%S")+"seconds at "+today_time.strftime("%p"))
            print("currently time is "+today_time.strftime("%H")+"hours "+today_time.strftime("%M")+"minutes and "+today_time.strftime("%S")+"seconds at "+today_time.strftime("%p"))
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open college official site' and 'college website' in query:
            webbrowser.open("https://aith.ac.in/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'facebook'in  query:
            webbrowser.open("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C550525804791%7Ce%7Cfacebook%7C&placement=&creative=550525804791&keyword=facebook&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696220912%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-1001394929%26loc_physical_ms%3D9040189%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAjwopWSBhB6EiwAjxmqDZlRNQW0fRxd27uOYsZHK5NGvXEZ60ZYJpcO50wPXMysEd23tpVDNBoCTUkQAvD_BwE")
        elif 'open linkedin' in query:
            webbrowser.open("https://in.linkedin.com/?trk=IN-SEM_google-adwords_Jordan-brand-sign-up&mcid=6844056167778418688&trk2=ga_campid=14650114791_asid=127961666580_crid=545833659352_kw=linkedin_d=c_tid=kwd-285981853_n=g_mt=p_geo=9040189_slid=&gclid=CjwKCAjwopWSBhB6EiwAjxmqDVkOqmg8aINBYpxw1Y2V53is2jjBTH2jDSnfzQr_EwTk7LTWEet8nBoC_w4QAvD_BwE&gclsrc=aw.ds")
        elif 'audio songs' in query:
            music_dr='C:\\Users\\moink\\OneDrive\\Desktop\\Songs\\Songs'
            songs=os.listdir(music_dr)
            os.startfile(os.path.join(music_dr,songs[0]))
        # elif ' time' in query:
        #     strTime=datetime.datetime.now().strftime("%H:%M:%S")
        #     print(strTime)
        #     speak(f"the time is {strTime}")
        elif 'video songs' in query:
            music_vid_dr='C:\\Users\\moink\\OneDrive\\Desktop\\Movies'
            video_songs = os.listdir(music_vid_dr)
            os.startfile(os.path.join(music_vid_dr,video_songs[0]))
        elif 'temp' and 'temperature' in query:
            url = "http://api.weatherapi.com/v1/forecast.json?key=440aeb0539ea418eb1734341220204&q=bareilly&days=1&aqi=yes&alerts=yes"
            json_data = requests.get(url).json()
            temp = (json_data["current"]["temp_c"])
            last_up = json_data["current"]["last_updated"]
            description = json_data["current"]["condition"]["text"]
            print(f"Current temperature of Bareilly is:{temp} degree celcius and day is {description}.(last updated at: {last_up})")
            speak(f"Current temperature of Bareilly is:{temp} degree celcius and day is {description}.(last updated at: {last_up})")
        elif 'news'  in query:
            speak("sure sir ,now i will read some news for you.")
            news_api_address="https://newsapi.org/v2/top-headlines?country=in&apiKey=0b631146289b487f95ec9e3fe92b6f64"
            ar=[]
            json_data=requests.get(news_api_address).json()#converting api data to json file

            def news():
                for i in range(3):
                    ar.append("Number"+str(i+1)+","+json_data["articles"][i]["title"]+".")
                return ar
            arr=news()

            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif 'send email' in query:
            try:
                speak("what should i say")
                content=takecommand()
                to="sachinkannojiya990@gmail.com"
                send_email(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry email is not able to send")
        # elif 'play a game' in query:
        #     print("aarfu")
        #     speak("which game do you want to play")
        #     print("1:snake game\n2:alien bullet game")
        #     game_choice=takecommand()
        #     if 'snake game' and 'first choice' in query:
        #         codePath = "C:\\Users\\Lenovo\\non\\snake_game\\main.py"
        #         os.startfile(codePath)
        #     elif 'alien bullet game' and 'second game' in query:
        #         codePath = "C:\\Users\\Lenovo\\non\\satellite_game\\main.py"
        #         os.startfile(codePath)
        #     speak("all the best and enjoy your game")
        elif 'my mood' in query:
            #import cv2

            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                cap = cv2.VideoCapture(1)
            if not cap.isOpened():
                raise IOError("Cannot open webcam")
            t = []
            while True:
                ret, frame = cap.read()
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                # print(result)
                # print(result[0]['dominant_emotion'])
                t.append(result[0]['dominant_emotion'])  # all emotions are stored in a list t
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.1, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,
                            result[0]['dominant_emotion'],
                            (50, 50),
                            font, 3,
                            (0, 0, 255),
                            2,
                            cv2.LINE_4)
                cv2.imshow('demo video', frame)
                #print(t)
                if cv2.waitKey(2) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            print("your emotion is :", max(set(t), key=t.count))  # line to find dominant emotion in the given time
            speak("Hey you are looking. I can suggest you this song to listen ")
            required_emotion = max(set(t), key=t.count)
            print(required_emotion)
            if required_emotion=='neutral':
                music_vid_dr = 'C:\\Users\\moink\\OneDrive\\Desktop\\Songs\\Songs'
                video_songs = os.listdir(music_vid_dr)
                os.startfile(os.path.join(music_vid_dr, video_songs[0]))
            elif required_emotion=='happy':
                music_vid_dr = 'C:\\Users\\moink\\OneDrive\\Desktop\\Songs\\Songs'
                video_songs = os.listdir(music_vid_dr)
                os.startfile(os.path.join(music_vid_dr, video_songs[4]))
            elif required_emotion=='sad':
                music_vid_dr = 'C:\\Users\\moink\\OneDrive\\Desktop\\Songs\\Songs'
                video_songs = os.listdir(music_vid_dr)
                os.startfile(os.path.join(music_vid_dr, video_songs[10]))
            elif required_emotion=='surprised':
                music_vid_dr = 'C:\\Users\\moink\\OneDrive\\Desktop\\Songs\\Songs'
                video_songs = os.listdir(music_vid_dr)
                os.startfile(os.path.join(music_vid_dr, video_songs[20]))
            elif required_emotion=='angry':
                music_vid_dr = 'C:\\Users\\moink\\OneDrive\\Desktop\\Songs\\Songs'
                video_songs = os.listdir(music_vid_dr)
                os.startfile(os.path.join(music_vid_dr, video_songs[12]))



        elif 'quit' in query:
                exit()
        # elif 'none' in query:
        #     speak("Please say that again")
speak("Thank you for using this assistent.have a good day")



