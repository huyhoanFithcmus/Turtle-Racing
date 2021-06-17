    #python setup
import pygame, sys
from turtle import *
from random import *
import turtle
import time
pygame.init()
clock = pygame.time.Clock()

    #racetypes display setup
screen = pygame.display.set_mode ([800, 650])
font = pygame.font.SysFont(None, 32)
base_font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 50)



    #content setup
#dua ngan
button1 = pygame.Rect(800 * 0.2, 650 * 0.55, 90 , 50)
#dua vua
button2 = pygame.Rect(800 * 0.44, 650 * 0.55, 110 , 50)
#dua dai
button3 = pygame.Rect(800 * 0.7, 650 * 0.55, 90 , 50)
#return button 
button4 = pygame.Rect(280, 500, 240 , 35)


def duangan():
        # SCREEN SETUP
    setup(1050, 650)
    title("Turtle Race")
    bgcolor("forestgreen")
    speed(0)
    duangan_running = True
    while duangan_running:
        # HEADING
        penup()
        goto(-100, 205)
        color("white")
        write("TURTLE RACE", font=("Arial", 20, "bold"))

        # DIRT
        goto(-350, 200)
        pendown()
        color("chocolate")
        begin_fill()
        for i in range(2):
            forward(700)
            right(90)
            forward(400)
            right(90)
        end_fill()

        # FINISH LINE
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
            
        # TURTLE 0 - WHITE
        white_turtle = Turtle()
        white_turtle.color("white")
        white_turtle.shape("turtle")
        white_turtle.shapesize(1.5)
        white_turtle.penup()
        white_turtle.goto(-350, 170)
        white_turtle.pendown()
        for i in range(6):
            speed(0)
            white_turtle.forward(590)
            white_turtle.right(90)
            white_turtle.forward(50)
            white_turtle.right(90)
            white_turtle.forward(590)
            white_turtle.right(180)
            penup()
        white_turtle.right(90)
        white_turtle.forward(50)
        penup()

            
        # TURTLE 1 - BLUE
        blue_turtle = Turtle()
        blue_turtle.color("cyan")
        blue_turtle.shape("turtle")
        blue_turtle.shapesize(1.5)
        blue_turtle.penup()
        blue_turtle.goto(-350, 150)
        blue_turtle.penup()
            
        # TURTLE 2 - PINK
        pink_turtle = Turtle()
        pink_turtle.color("magenta")
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
        green_turtle.color("lime")
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
        time.sleep(2)

        #MOVE THE  TURTLE
        while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and red_turtle.xcor() <= 230 and black_turtle.xcor() <= 230 :
            blue_turtle.forward(randint(1, 10))
            pink_turtle.forward(randint(1, 10))
            yellow_turtle.forward(randint(1, 10))
            green_turtle.forward(randint(1, 10))
            red_turtle.forward(randint(1, 10))
            black_turtle.forward(randint(1, 10))

        #CELEBRATE THE WINNER
        #BLUE WIN
        if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > black_turtle.xcor():
            print("Blue turtle win")
            for i in range(72):
                blue_turtle.right(5)
                blue_turtle.shapesize(2.5)
            for i in range(10):
                blue_turtle.color("green")
                blue_turtle.color("blue")
                blue_turtle.color("black")
                blue_turtle.color("red")
                blue_turtle.color("yellow")
                blue_turtle.color("blue")
        #PINK WIN
        elif pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor() and pink_turtle.xcor() > black_turtle.xcor():
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
        #YELLOW WIN
        elif yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() > black_turtle.xcor():
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

    # ham in chu~
def draw_text (text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_position = (x, y)
    surface.blit (textobj, text_position)

def race_types():
    racetypes_running = True

    while racetypes_running:
        for event in pygame.event.get():
            # bam nut cheo x se out
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    racetypes_running = False
                    #DAT HAM MAIN MENU VAO CMT NAY!
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button4.collidepoint(event.pos):
                    #khi bam vao nut return se out 
                    racetypes_running = False
                    #DAT HAM MAIN MENU VAO DONG CMT NAY!
                if button1.collidepoint(event.pos):
                    racetypes_running = False
                    pygame.quit() # dung chuong trinh racetypes!!!
                    duangan()
                if button2.collidepoint(event.pos):
                     racetypes_running = False
                    #DAT HAM DUONG DUA VUA VAO DONG CMT NAY!
                if button3.collidepoint(event.pos):
                     racetypes_running = False
                    #DAT HAM DUONG DUA DAI VAO DONG CMT NAY!

        screen.fill((250, 250, 250))

        pygame.draw.rect(screen, (0,0,0), button1, 2)
        pygame.draw.rect(screen, (0,0,0), button2, 2)
        pygame.draw.rect(screen, (0,0,0), button3, 2)
        pygame.draw.rect(screen, (0,0,0), button4, 2)

        draw_text("short", base_font, (0,0,0), screen, button1.x + 15, button1.y + 10)
        draw_text("medium", base_font, (0,0,0), screen, button2.x + 15, button2.y + 10)
        draw_text("long", base_font, (0,0,0), screen, button3.x + 15, button3.y + 10)
        draw_text("Return", base_font, (0,0,0), screen, button4.x + 80, button4.y + 10)
        draw_text("Race Types", title_font, (0,0,0), screen, 800 * 0.38 , 600 * 0.2)

        pygame.display.flip()
        clock.tick(60)
race_types()

