from turtle import *
from random import *
import turtle
import time
import pygame, sys

                    # CO RUA QUAY DAU.

def duangan():
    #bgpic('race7.gif')
    # SCREEN SETUP
    setup(1050, 650)
    title("Turtle Race")
    bgcolor("white")
    speed(0)

    duangan_running = True
    green = False
    while duangan_running:
        # HEADING
        penup()
        goto(-150, 205)
        color("red")
        write("TURTLE RACE", font=("Arial", 40, "bold"))

        #DIRT (DON LAI DUONG DUA)
        goto(-350, 200)
        pendown()
        color("gray")
        begin_fill()
        for i in range(2):
            forward(700)
            right(90)
            forward(400)
            right(90)
        end_fill()

        #finish line
        gap_size = 20
        shape("square")
        penup()

        # WHITE SQUARES ROW 1
        color("white")
        for i in range(10):
            goto(250, (170 - (i * gap_size * 2)))
            stamp()

        # WHITE SQUARES ROW 2
        for i in range(10):
            goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
            stamp()

        # BLACK SQUARES ROW 1
        color("black")
        for i in range(10):
            goto(250, (190 - (i * gap_size * 2)))
            stamp()

        # BLACK SQUARES ROW 2
        for i in range(10):
            goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
            stamp()

        # TURTLE 1 - BLUE
        blue_turtle = Turtle()
        blue_turtle.color("blue")
        blue_turtle.shape("turtle")
        blue_turtle.shapesize(1.5)
        blue_turtle.penup()
        blue_turtle.goto(-350, 150)
        blue_turtle.penup()
            
        # TURTLE 2 - PINK
        pink_turtle = Turtle()
        pink_turtle.color("pink")
        pink_turtle.shape("turtle")
        pink_turtle.shapesize(1.5)
        pink_turtle.penup()
        pink_turtle.goto(-350, 100)
        pink_turtle.penup()    
            
        # TURTLE 3 - YELLOW
        yellow_turtle = Turtle()
        yellow_turtle.color("yellow")
        yellow_turtle.shape("turtle")
        yellow_turtle.shapesize(1.5)
        yellow_turtle.penup()
        yellow_turtle.goto(-350, 50)
        yellow_turtle.penup()    
        
        # TURTLE 4 - GREEN
        green_turtle = Turtle()
        green_turtle.color("green")
        green_turtle.shape("turtle")
        green_turtle.shapesize(1.5)
        green_turtle.penup()
        green_turtle.goto(-350, 0)
        green_turtle.penup()  

        # TURTLE 5 - RED
        red_turtle = Turtle()
        red_turtle.color("red")
        red_turtle.shape("turtle")
        red_turtle.shapesize(1.5)
        red_turtle.penup()
        red_turtle.goto(-350, -50)
        red_turtle.penup()  

        # TURTLE 6 - BLACK
        black_turtle = Turtle()
        black_turtle.color("black")
        black_turtle.shape("turtle")
        black_turtle.shapesize(1.5)
        black_turtle.penup()
        black_turtle.goto(-350, -100)
        black_turtle.penup()  

        # PAUSE FOR 1 SECOND BEFORE RACING
        time.sleep(1)
        
        #KHAI BAO TIME
        turtleA =turtle.Turtle()
        start = time.time()
        

        #MOVE THE  TURTLE
        blue_turn = False
        yellow_stop = False
        black_stop = False
        while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and red_turtle.xcor() <= 230 and black_turtle.xcor() <= 230 :
        #SET UP TIME
            turtleA.color("black")
            turtleA.clear()
            turtleA.shape()
            turtleA.penup()
            turtleA.goto(300,255)
            turtleA.penup()
            turtleA.write("Time: " + '%.4s'%(time.time() - start),font=("Arial", 20, "bold"))  
            
                        
            blue_turtle.forward(randint(1, 10))
            pink_turtle.forward(randint(9, 10))
            yellow_turtle.forward(randint(1, 10))
            green_turtle.forward(randint(1, 10))
            red_turtle.forward(randint(1, 10))
            black_turtle.forward(randint(1, 10))



            if blue_turtle.xcor() >= 60 and pink_turtle.xcor() >= 60 and yellow_turtle.xcor() >= 60 and green_turtle.xcor() >= 60 and red_turtle.xcor() >= 60 and black_turtle.xcor() >= 60 :
                if blue_turn == False:
                    for i in range (2):
                        blue_turtle.right(180)
                        pink_turtle.forward(randint(5, 10))
                        yellow_turtle.forward(randint(5, 10))
                        green_turtle.forward(randint(5, 10))
                        red_turtle.forward(randint(5, 10))
                        black_turtle.forward(randint(5, 10))
                        blue_turtle.forward(randint(5, 10))
                    blue_turn = True
                     
            if blue_turtle.xcor() >= 15 and pink_turtle.xcor() >= 15:
                if yellow_stop == False:
                    for i in range (10):
                        blue_turtle.forward(randint(1, 10))
                        pink_turtle.forward(randint(1, 10))
                        #yellow khong chay
                        green_turtle.forward(randint(1, 10))
                        red_turtle.forward(randint(1, 10))
                        black_turtle.forward(randint(8, 10)) 
                    yellow_stop = True
            if red_turtle.xcor() >= 40 and black_turtle.xcor() >= 40:
                if black_stop == False:
                    for i in range (10):
                        blue_turtle.forward(randint(1, 10))
                        pink_turtle.forward(randint(1, 10))
                        yellow_turtle.forward(randint(1, 10))
                        green_turtle.forward(randint(1, 10))
                        red_turtle.forward(randint(1, 10))
                        #black khong chay
                    black_stop = True
          
        #CELEBRATE THE WINNER
        #BLUE WIN
        if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > black_turtle.xcor():
            print("Blue turtle win" + eslapse)
            for i in range(72):
                blue_turtle.right(5)
            for i in range(10):
                blue_turtle.color("green")
                blue_turtle.color("blue")
                blue_turtle.color("black")
                blue_turtle.color("red")
                blue_turtle.color("yellow")
                blue_turtle.color("blue")
            # may con con` lai chay tiep.
            while pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                if pink_turtle.xcor() <= 230:
                    pink_turtle.forward(randint(1, 10))
                if yellow_turtle.xcor() <= 230:   
                    yellow_turtle.forward(randint(1, 10))
                if green_turtle.xcor() <= 230:
                    green_turtle.forward(randint(1, 10)) 
                if red_turtle.xcor() <= 230:          
                    red_turtle.forward(randint(1, 10))
                if black_turtle.xcor() <= 230:         
                    black_turtle.forward(randint(1, 10))
                turtleA.clear()
                turtleA.write("Time: " + '%.4s'%(time.time() - start - 4.5),font=("Arial", 20, "bold"))

        #PINK WIN
        elif  pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor() and pink_turtle.xcor() > black_turtle.xcor():
            print("pink turtle win")
            for i in range(72):
                pink_turtle.right(5)
                pink_turtle.shapesize(2.5)
            for i in range(10):
                pink_turtle.color("green")
                pink_turtle.color("pink")
                pink_turtle.color("black")
                pink_turtle.color("red")
                pink_turtle.color("yellow")
                pink_turtle.color("pink")

            while blue_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                if blue_turtle.xcor() <= 230:
                    blue_turtle.forward(randint(1, 10))
                if yellow_turtle.xcor() <= 230:   
                    yellow_turtle.forward(randint(1, 10))
                if green_turtle.xcor() <= 230:
                    green_turtle.forward(randint(1, 10)) 
                if red_turtle.xcor() <= 230:          
                    red_turtle.forward(randint(1, 10))
                if black_turtle.xcor() <= 230:         
                    black_turtle.forward(randint(1, 10))
                turtleA.clear()
                turtleA.write("Time: " + '%.4s'%(time.time() - start - 4.5),font=("Arial", 20, "bold"))
        #YELLOW WIN
        elif  yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() > black_turtle.xcor():
            print("yellow turtle win")
            for i in range(72):
                yellow_turtle.right(5)
                yellow_turtle.shapesize(2.5)
            for i in range(10):
                yellow_turtle.color("green")
                yellow_turtle.color("yellow")
                yellow_turtle.color("black")
                yellow_turtle.color("red")
                yellow_turtle.color("yellow")
                yellow_turtle.color("yellow")
            while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                if pink_turtle.xcor() <= 230:
                    pink_turtle.forward(randint(1, 10))
                if blue_turtle.xcor() <= 230:   
                    blue_turtle.forward(randint(1, 10))
                if green_turtle.xcor() <= 230:
                    green_turtle.forward(randint(1, 10)) 
                if red_turtle.xcor() <= 230:          
                    red_turtle.forward(randint(1, 10))
                if black_turtle.xcor() <= 230:         
                    black_turtle.forward(randint(1, 10))
                turtleA.clear()
                turtleA.write("Time: " + '%.4s'%(time.time() - start - 4.5),font=("Arial", 20, "bold"))
        #GREEN WIN
        elif green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > blue_turtle.xcor() and green_turtle.xcor() > yellow_turtle.xcor() and green_turtle.xcor() > red_turtle.xcor() and green_turtle.xcor() > black_turtle.xcor():
            print("yellow turtle win")
            for i in range(72):
                green_turtle.right(5)
                green_turtle.shapesize(2.5)
            for i in range(10):
                green_turtle.color("green")
                green_turtle.color("green")
                green_turtle.color("black")
                green_turtle.color("red")
                green_turtle.color("yellow")
                green_turtle.color("green")
            while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                if pink_turtle.xcor() <= 230:
                    pink_turtle.forward(randint(1, 10))
                if yellow_turtle.xcor() <= 230:   
                    yellow_turtle.forward(randint(1, 10))
                if blue_turtle.xcor() <= 230:
                    blue_turtle.forward(randint(1, 10)) 
                if red_turtle.xcor() <= 230:          
                    red_turtle.forward(randint(1, 10))
                if black_turtle.xcor() <= 230:         
                    black_turtle.forward(randint(1, 10))
                turtleA.clear()
                turtleA.write("Time: " + '%.4s'%(time.time() - start - 4.5),font=("Arial", 20, "bold"))
        #RED WIN
        elif red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > green_turtle.xcor() and red_turtle.xcor() > yellow_turtle.xcor() and red_turtle.xcor() > black_turtle.xcor() :
            print("yellow turtle win")
            for i in range(72):
                red_turtle.right(5)
                red_turtle.shapesize(2.5)
            for i in range(10):
                red_turtle.color("green")
                red_turtle.color("red")
                red_turtle.color("black")
                red_turtle.color("red")
                red_turtle.color("yellow")
                red_turtle.color("red")
            while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                if pink_turtle.xcor() <= 230:
                    pink_turtle.forward(randint(1, 10))
                if yellow_turtle.xcor() <= 230:   
                    yellow_turtle.forward(randint(1, 10))
                if green_turtle.xcor() <= 230:
                    green_turtle.forward(randint(1, 10)) 
                if blue_turtle.xcor() <= 230:          
                    blue_turtle.forward(randint(1, 10))
                if black_turtle.xcor() <= 230:         
                    black_turtle.forward(randint(1, 10))
                turtleA.clear()
                turtleA.write("Time: " + '%.4s'%(time.time() - start - 4.5),font=("Arial", 20, "bold"))
        #BLACK WIN
        else: 
            print("black turtle win")
            for i in range(72):
                black_turtle.right(5)
                black_turtle.shapesize(2.5)
            for i in range(10):
                black_turtle.color("green")
                black_turtle.color("black")
                black_turtle.color("black")
                black_turtle.color("red")
                black_turtle.color("yellow")
                black_turtle.color("black")
            while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230:
                if pink_turtle.xcor() <= 230:
                    pink_turtle.forward(randint(1, 10))
                if yellow_turtle.xcor() <= 230:   
                    yellow_turtle.forward(randint(1, 10))
                if green_turtle.xcor() <= 230:
                    green_turtle.forward(randint(1, 10)) 
                if red_turtle.xcor() <= 230:          
                    red_turtle.forward(randint(1, 10))
                if black_turtle.xcor() <= 230:         
                    black_turtle.forward(randint(1, 10))
                turtleA.clear()
                turtleA.write("Time: " + '%.4s'%(time.time() - start - 4.5),font=("Arial", 20, "bold"))
        turtleA.clear()
        begin_fill()
duangan()