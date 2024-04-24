#import numpy as np
import datetime
from datetime import date
import webbrowser
import calendar
import requests
import json
import os
import csv
#import pylab as pl
import subprocess
from subprocess import call
import urllib.request
from googlesearch import *
from googlesearch import search
import geocoder 
#import bs4 as bs
from sys import exit
import pyttsx3
import pywhatkit as kit
import time
import turtle
import winsound
import pyjokes
import wikipedia

current_date = datetime.datetime.now().date()
current_time = datetime.datetime.today().time()
engine = pyttsx3.init()

while(1):
    print("Hi! User ID please")
    engine.say('Hi , User ID please')
    engine.runAndWait()
    login = input('')
    
    engine.runAndWait()
    engine.say('Password please!!')
    engine.runAndWait()
    password = input('Password please!!\n')
    
    if(login == '1234' and password == 'chatbot'):
        print(' Hello! My name is AI-BOT ,  How can I assist you')
        engine.say("Hello! My name is AI-BOT ,  How can I assist you")
        engine.runAndWait()
        break

    elif(login != '1234' and password != 'chatbot'):
        print("Both User id and password is Incorrect!!!")
        engine.say("Both User id and password is Incorrect")
        engine.runAndWait()

    elif(login != '1234'):
        print("User id is Incorrect!!!")
        engine.say("User id is Incorrect")
        engine.runAndWait()

    elif(password != 'chatbot'):
        print("Password is Incorrect!!!")
        engine.say("Password is Incorrect")
        engine.runAndWait()

while(1):
    phrase = input("> ")
    phrase = phrase.lower()

    if 'location' in phrase:
        g = geocoder.ip('me')
        lat = g.lat
        lon = g.lng
        print('Latitude is',lat,'Lonitude is',lon)
        engine.say("Your current location is")
        engine.runAndWait()
        webbrowser.open('https://mycurrentlocation.net/')


    elif 'music' in phrase:
        music = "What music would you like to listen to?"
        engine.say("What music would you like to listen to")
        engine.runAndWait()
        ip1 = input("What music would you like to listen to?")
        kit.playonyt(ip1)

    elif 'timer' in phrase:
        time_sec = int(input("Enter the time you want to set the timer for"))
        def countdown(time_sec):
            while time_sec:
                mins, secs = divmod(time_sec, 60)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                print(timeformat, end='\r')
                time.sleep(1)
                time_sec -= 1
            print("Bzzzt! The countdown is at zero seconds!")
        countdown(time_sec)

    elif 'time' in phrase:
        print(current_time)

    elif 'date' in phrase:
        print(current_date)
        
    elif 'weather' in phrase:
        print("Welcome to the Weather Forecaster!\n")
        engine.say("Welcome to the Weather Forecaster")
        engine.runAndWait()
        print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n")
        engine.say("Just Enter the City you want the weather report for and click on the button! It's that simple")
        engine.runAndWait()
        city_name = input("Enter the name of the City : ")
        print("\n\n")
 
        def Gen_report(C):
            url = 'https://wttr.in/{}'.format(C)
            try:
                data = requests.get(url)
                T = data.text
            except:
                T = "Error Occurred"
            print(T)
     
        Gen_report(city_name)

    elif 'calculator' in phrase:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    elif 'calendar' in phrase:
        yy = int(input("Enter year: "))
        mm = int(input("Enter month number: "))
        print(calendar.month(yy, mm))
    
    elif 'age' in phrase:
        def age(birthdate):
            today = date.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        
        try:
            year = int(input("Enter your birth year: "))
            month = int(input("Enter your birth month: "))
            day = int(input("Enter your birth day: "))
            result = age(date(year,month,day))
            print(f'You are {result} years old')
        except:
            print('Failed to calculate age, either day or month or year is invalid')

    elif 'search'in phrase:
        query = str(input("Enter your query: "))
        n = int(input("How many sentences of information do you want? "))
        print(wikipedia.summary(query, sentences = n))
        num=5
        for j in search(query,num):
            print(j)

    elif 'joke' in phrase:
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        print(My_joke)
        engine.say(My_joke)
        engine.runAndWait()
        
    elif 'bored' or 'game' in phrase:
        print("Which game do you want to play?\n1.Quiz\n2.Pong")
        count = int(input("Enter your choice: "))
        if(count==1):
            print('Welcome to Python Quiz')
            answer=input('Are you ready to play the Quiz ? (yes/no) :')
            score=0
            total_questions=3
    
            if answer.lower()=='yes':
                answer=input('Question 1: What is your Favourite programming language?')
                if answer.lower()=='python':
                    score += 1
                    print('correct')
                else:
                    print('Wrong Answer :(')
    
    
                answer=input('Question 2: Who invented Python? ')
                if answer.lower()=='Guido van rossum':
                    score += 1
                    print('correct')
                else:
                    print('Wrong Answer :(')
    
                answer=input('Question 3: What is a correct syntax to output "Hello World" in Python?')
                if answer.lower()=='print("Hello World")':
                    score += 1
                    print('correct')
                else:
                    print('Wrong Answer :(')
    
            print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
            mark=(score/total_questions)*100
            print('Marks obtained:',mark)
            print('BYE!')
        
        elif(count==2):
            pong = turtle.Screen()
            pong.title("Pong by @LeeshmaAdari")
            pong.bgcolor("black")
            pong.setup(width=800, height=600) #400-left,400-right,300-up,300-down
            pong.tracer(0)

            #Score
            score_a = 0
            score_b = 0

            #paddle A
            paddle_A = turtle.Turtle()
            paddle_A.speed(0) #speed of animation
            paddle_A.shape("square")
            paddle_A.color("white")
            paddle_A.shapesize(stretch_wid=5, stretch_len=1)
            paddle_A.penup()
            paddle_A.goto(-350,0) #left side of screen

            #paddle B
            paddle_B = turtle.Turtle()
            paddle_B.speed(0) #speed of animation
            paddle_B.shape("square")
            paddle_B.color("white")
            paddle_B.shapesize(stretch_wid=5, stretch_len=1)
            paddle_B.penup()
            paddle_B.goto(350,0) #right side of screen

            #Ball
            ball = turtle.Turtle()
            ball.speed(0) #speed of animation
            ball.shape("square")
            ball.color("white")
            ball.penup()
            ball.goto(0,0) #centre side of screen
            ball.dx = 0.1 #it moves to right diagonally down
            ball.dy = -0.1 #it moves to left diagonally up

            #Pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(0,255)
            pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",16,"normal"))


            def paddle_A_up():
                y = paddle_A.ycor() #returns y coordinate
                y += 20 #when paddle A goes up so it increases so, to inc we add by 20 pixels
                paddle_A.sety(y)

            def paddle_A_down():
                y = paddle_A.ycor() #returns y coordinate
                y -= 20 #when paddle A goes up so it increases so, to inc we add by 20 pixels
                paddle_A.sety(y)

            def paddle_B_up():
                y = paddle_B.ycor() #returns y coordinate
                y += 20 #when paddle A goes up so it increases so, to inc we add by 20 pixels
                paddle_B.sety(y)

            def paddle_B_down():
                y = paddle_B.ycor() #returns y coordinate
                y -= 20 #when paddle A goes up so it increases so, to inc we add by 20 pixels
                paddle_B.sety(y)

            #keyboard binding
            pong.listen() #listen for keyboard input
            pong.onkeypress(paddle_A_up, "w") #it calls the function
            pong.onkeypress(paddle_A_down, "s") #it calls the function
            pong.onkeypress(paddle_B_up, "Up") #it calls the function
            pong.onkeypress(paddle_B_down, "Down") #it calls the function

            #Main game loop
            while True:
                pong.update()
                #everytime when game runs, it updates the screen

                #Move the ball
                ball.setx(ball.xcor() + ball.dx)
                ball.sety(ball.ycor() + ball.dy)

                #Border checking
                if ball.ycor()>290:
                    ball.sety(290) #it sets the ycor of ball to 290 so that it can bounce back
                    ball.dy *= -1 #it reverses the direction of the ball
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball.ycor()<-290:
                    ball.sety(-290)
                    ball.dy *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball.xcor()>390:
                    ball.goto(0,0) #it goes back to center after hitting right and left wall
                    ball.dx *= -1
                    score_a += 1
                    pen.clear()
                    pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",16,"normal"))

                if ball.xcor()<-390:
                    ball.goto(0,0) 
                    ball.dx *= -1
                    score_b += 1
                    pen.clear()
                    pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",16,"normal"))

                #Paddle and ball collisions
                if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
                    ball.setx(340)
                    ball.dx *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

                if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
                    ball.setx(-340)
                    ball.dx *= -1
                    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
        elif 'draw' in phrase:
            my_pen = turtle.Pen()
            turtle.bgcolor("black") 
                    

    
                

        
            


            

                

    
        
            
    
        

        
     





