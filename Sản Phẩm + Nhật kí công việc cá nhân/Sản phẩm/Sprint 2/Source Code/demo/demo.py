     #python setup
import pygame, sys
pygame.init()                                       
clock = pygame.time.Clock()
# duongdua setup
from turtle import *
from random import *
import turtle
import time
    #screen setup
screen = pygame.display.set_mode([800, 650])
font = pygame.font.SysFont(None, 32)
base_font = pygame.font.SysFont(None, 32)
title_font = pygame.font.SysFont(None, 60)


def draw_text (text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_position = (x, y)
    surface.blit (textobj, text_position)
def main_menu():
    
    background = pygame.image.load('menu.gif')
    while True:
        screen.blit(background,(0,0))
        draw_text("MAIN MENU", title_font, "black", screen, 280, 80)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(290, 200, 200, 35)
        button_2 = pygame.Rect(290, 300, 200, 35)
        button_3 = pygame.Rect(290, 400, 200, 35)
        draw_text("Vao Choi", base_font, "black", screen, button_1.x + 50, button_1.y + 5)
        draw_text("Luat Choi", base_font, "black", screen, button_2.x + 45, button_2.y + 5)
        draw_text("Thoat", base_font, "black", screen, button_3.x + 60, button_3.y + 5)
        if button_1.collidepoint ((mx, my)):
            # BAM VAO O VUONG 1. (GIAO DIEN GAME)
            if click:
                race_types()
        if button_2.collidepoint ((mx, my)):
            if click:
                options()
        if button_3.collidepoint ((mx, my)): 
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, "black", button_1, 2)
        pygame.draw.rect(screen, "black", button_2, 2)
        pygame.draw.rect(screen, "black", button_3, 2)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.flip()
        clock.tick(60)

def game():
    running = True
    screen.fill((250, 250,250))
    while running:
        draw_text('game', font, (0, 0, 0), screen, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()
        clock.tick(60)

def options():
    running = True
    screen.fill((250, 250,250))
    while running:
        draw_text('options', font, (0, 0, 0), screen, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()
        clock.tick(60)
def user_name():
        #content setup
    color_active = pygame.Color("blue")
    color_passive = pygame.Color("gray15")
    color = color_passive
    background = pygame.image.load('username.gif')
    user_text = 'enter username: '
    game_title = "TURTLE GAME"
    #demo_font = pygame.font.Font('8-BIT WONDER.TTF', 50)

    # tao khung dien username, switch screen
    username_button = pygame.Rect(280, 400, 240 , 35)
    switchscreen_button = pygame.Rect(480, 400, 40, 35)
    
    #bien active dung cho mau, running dung cho ca screen username
    active = False
    username_running = True

    while username_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # neu vi tri nguoi dung click = vi tri o^
                if username_button.collidepoint(event.pos):
                    active = True
                    user_text = ' '
                else:
                    active = False

            if active == True:
                if event.type == pygame.KEYDOWN:
                    #neu nguoi dung bam backspace se xoa' 1 ki tu 
                    if event.key == pygame.K_BACKSPACE:   
                         #xoa 1 chu cuoi  
                        user_text = user_text [0:-1]    
                    else:
                            #gioi han chi duoc viet 20 ki tu
                            if len(user_text) < 16: 
                                #lay tat ca nhung gi nguoi dung nhap
                                user_text += event.unicode    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if switchscreen_button.collidepoint(event.pos):
                        username_running = False
                        main_menu()
                          
        if active == False:
            color = color_active
        else:
            color = color_passive

        #mau trang    
        screen.fill ((250, 250, 250)) 
        screen.blit(background,(0,0))
        pygame.draw.rect(screen, color, username_button, 2)
        pygame.draw.rect(screen, color, switchscreen_button, 2)

        draw_text(">>", base_font , "black", screen, switchscreen_button.x + 5, switchscreen_button.y + 5)
        draw_text(game_title, title_font, "lightblue", screen, 250, 450)
        draw_text(user_text, base_font, "lightblue", screen, username_button.x + 5, username_button.y + 5)
        pygame.display.flip()
        clock.tick(60)
def duangan():
    #bgpic('race7.gif')
    # SCREEN SETUP
    setup(1050, 650)
    title("Turtle Race")
    bgcolor("white")
    speed(0)

    duangan_running = True
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

        #MOVE THE  TURTLE
        blue_turn = False
        yellow_stop = False
        black_stop = False
        while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and red_turtle.xcor() <= 230 and black_turtle.xcor() <= 230 :
            blue_turtle.forward(randint(1, 10))
            pink_turtle.forward(randint(1, 10))
            yellow_turtle.forward(randint(1, 10))
            green_turtle.forward(randint(1, 10))
            red_turtle.forward(randint(1, 10))
            black_turtle.forward(randint(1, 10))
            if blue_turtle.xcor() >= 60 and pink_turtle.xcor() >= 60 and yellow_turtle.xcor() >= 60 and green_turtle.xcor() >= 60 and red_turtle.xcor() >= 60 and black_turtle.xcor() >= 60 :
                if blue_turn == False:
                    for i in range (2):
                        blue_turtle.right(180)
                        pink_turtle.forward(randint(1, 10))
                        yellow_turtle.forward(randint(1, 10))
                        green_turtle.forward(randint(1, 10))
                        red_turtle.forward(randint(1, 10))
                        black_turtle.forward(randint(1, 10))
                        blue_turtle.forward(randint(1, 10))
                    blue_turn = True
                     
            if blue_turtle.xcor() >= 15 and pink_turtle.xcor() >= 15:
                if yellow_stop == False:
                    for i in range (10):
                        blue_turtle.forward(randint(1, 10))
                        pink_turtle.forward(randint(1, 10))
                        #yellow khong chay
                        green_turtle.forward(randint(1, 10))
                        red_turtle.forward(randint(1, 10))
                        black_turtle.forward(randint(1, 10)) 
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
            print("Blue turtle win")
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
        begin_fill()
def race_types():
     #content setup
    background = pygame.image.load('menu.gif')
    #dua ngan
    button1 = pygame.Rect(800 * 0.2, 650 * 0.55, 90 , 50)
    #dua vua
    button2 = pygame.Rect(800 * 0.44, 650 * 0.55, 110 , 50)
    #dua dai
    button3 = pygame.Rect(800 * 0.7, 650 * 0.55, 90 , 50)
    #return button 
    button4 = pygame.Rect(280, 500, 240 , 35)

    racetypes_running = True
    while racetypes_running:
        screen.blit(background,(0,0))
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
                    # NOI SOURCE DUA NGAN (pygame.quit() thoat giao dien racetypes)
                    pygame.quit()
                    duangan()
                if button2.collidepoint(event.pos):
                     racetypes_running = False
                    #DAT HAM DUONG DUA VUA VAO DONG CMT NAY!
                if button3.collidepoint(event.pos):
                     racetypes_running = False
                    #DAT HAM DUONG DUA DAI VAO DONG CMT NAY!

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

user_name()