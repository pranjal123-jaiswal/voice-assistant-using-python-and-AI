
import pyttsx3 as p                                                         # module text to speech
import speech_recognition as sr                                             # sppech recogination module
from pyttsx3 import driver                                                  # use to run driver
from selenium import webdriver                                              # import webdriver for opening chrome because it allows several function
import requests                                                             # module for impoert information from news.api
import json                                                                 # for conversion into json file
import randfacts                                                            # used for random facts
import pyjokes                                                              # module for random joke
import time                                                                 # module for date and time
from playsound import playsound                                             # module for music


engine =p.init()                                                            # constructor

rate=engine.getProperty('rate')                                             #reading rate
engine.setProperty('rate',180)                                              # set reading speed
#print(rate)


voices=engine.getProperty('voices')                                         #print the types of voices
engine.setProperty('voices',voices[1].id)                                   # change voice
#print(voices)


def speak(text):
    engine.say(text)                                                        #read sentence
    engine.runAndWait()                                                     # wait until next command

speak("Hello sir i am your voice assistant . How are you")                  # function call


r=sr.Recognizer()                                                           # helps to rettrive audio from  microphone

with sr.Microphone() as source:                                             # mainly work as ear to listen voice 
    r.energy_threshold= 10000                                               #increase the amplitude of upto 1k times for better uderstsnding 
    r.adjust_for_ambient_noise(source,1.2)                                  # cancel the unneccesry noice
    print("Listenning")
    audio=r.listen(source)                                                  # work as a brain to recozine voice
    text=r.recognize_google(audio)                                          #sends audio to GOOGLE  api system and converted into text form  (APPLICATION PROGRAM SERVICES)
    print(text)                                                             # print the reconize text   


if "what" and "about" and "you" in text:                                    # audio response
    speak("i also having a very good day sir ")
speak("How can i help you")                                                 # mandatiory line   




with sr.Microphone() as source:                                             # used to get what to open in the browser 
    r.energy_threshold= 10000                                               
    r.adjust_for_ambient_noise(source,1.2)                                  
    print("Listenning")
    audio=r.listen(source)                                                  
    text2=r.recognize_google(audio)                                          
    print(text2)                                                              






class infow():
    if "information" in text2:                                                      # check wheyher the voice condition is true or not 
        speak(" you need information on which topic?")
        

        with sr.Microphone() as source:                                             # used to search information on wikipedia
            r.energy_threshold= 10000                                               
            r.adjust_for_ambient_noise(source,1.2)                                  
            print("Listenning")
            audio=r.listen(source)                                                  
            infor=r.recognize_google(audio)                                          
            print(infor)
            speak(" searching{}  on wikipedia.".format(infor))    
        
        class wiki():    
            def __init__ (self):
                self.driver= webdriver.Chrome() 
    
            def wikipedia(self, query):     
                self.query= query                                                                    # collect query from user
                self.driver.get(r'https://www.wikipedia.org/')                                       # search query on driver which is chrome on (wikipedia)
                search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')                   # triggered search bar 
                search.click()                                                                       # click on search bar 
                search.send_keys(query)                                                     
                enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')    # triggered on search button
                enter.click()                                                                        # click on search button
                self.driver.say
            
        assist=wiki()                                                                                # instance of wiki class 
        assist.wikipedia(infor)                                                                      # call wikipedia class


    







    elif "play" or "video" or "youtube" in text2:                                                                 # used for youtude access
        speak(" which video you want to play?")
            # self.driver= webdriver.Chrome()  
        with sr.Microphone() as source:                                             
            r.energy_threshold= 10000                                               
            r.adjust_for_ambient_noise(source,1.2)                                  
            print("Listenning")
            audio=r.listen(source)                                                  
            vid=r.recognize_google(audio)
            print(vid)


        class you():                                                                               # youtube class
            def __init__ (self):
       
                self.driver= webdriver.Chrome() 
                                                           
       
    
            def youtube(self, query):                                                                 # used to take query for youtube
                self.query= query                                                                    
                self.driver.get(r'https://www.youtube.com/')                                       
                search=self.driver.find_element_by_xpath('//*[@id="search"]')                         # addressing (pointing to) different parts of an XML document
                search.click()                                                                       
                search.send_keys(query)                                                     
                enter=self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')    
                enter.click()                                                                        
                
                video=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')                   # play top most video on search page
                video.click()
        assist=you()
        assist.youtube(vid)

    
    
         
       

    elif "news" in text2:                                                                                            # NEWS
        speak(" sure sir i will read NEWS for you ")  
        def news():
            api_address='https://newsapi.org/v2/top-headlines?country=in&apiKey=3120d7646d5e45229c3ee97005056cf4'    # key address of news api

            json_data=requests.get(api_address).json()                                                               # convert news into json format

            ar=[]                                                                                                    # empty list
            
            for i in range(3):
                ar.append(  "number"+ str(i+1) +"   "  + json_data["articles"][i]["title"] + ".")                    # read the articles of news

            return ar                                                                                                # read only top 3 news
        
        arr=news()

        for i in range (len(arr)):
            
            print(arr[i])                                                                                            # print the news 
            speak(arr[i])                                                                                            # read the news
        
    elif "facts" or "fact" in text2:                                                                            
        x=randfacts.get_fact()                                                                                       # generate random facts 
        print(x)
        speak(" Did you know" + x)    

    elif "jokes" or "joke" in text2: 
        speak("sure sir get ready for some chuckles")    
        j=(pyjokes.get_joke())                                                                                       # generate random joke (❁´◡`❁)
        print(j)
        speak("" + j)      

    elif "temperature" or "temp" or "weather" in text2:                                                              # genearte temperature and weather
        def weather():
            api_address='http://api.openweathermap.org/data/2.5/weather?q=aligarh&appid=06f255a8974698ab31edd4da768a1b5f'   # apk link of open weather .apk

            json_data=requests.get(api_address).json()

            def temp():                                                                                                     # function for temperature
                tepmerature=round(json_data["main"]["temp"]-273,1 )
                return tepmerature

            def des():                                                                                                       # function for description
                description= json_data  ["weather"][0]["description"]    
                return description
            
            t=str(temp() )
            print(t)
            speak("the temperature is" +t + " degree celcius")
            
            
            d=des()
            print(d)
            speak("and condition is " +d)
        
        a=weather()


    elif "date" or "time" in text2:                                                                                           # generate date and time
        a=time.localtime()
        c=time.asctime(a)

        print(c)
        speak(" present date and time is " + c)

    elif "music" or "sound" in text2:                                                                                          # generate music
        def play():
            playsound(r'C:\Users\HP\Music\Lukas Graham - 7 Years _OFFICIAL MUSIC VIDEO_ ( 256kbps cbr ).mp3')                  # music file path  
        
        print("ok sir " +"  "+ "now playing   seven years by lukas graham")
        speak("ok sir " +"  "+ "now playing   seven years by lukas graham")
        a=play()


assist=infow()                                                                                                       #  instance of infow class to proceed program

