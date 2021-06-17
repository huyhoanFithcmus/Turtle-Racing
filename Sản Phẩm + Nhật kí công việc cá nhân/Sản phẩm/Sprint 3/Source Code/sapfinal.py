     #python setup
import pygame,random,time,sys
from turtle import *
import turtle
import time
from turtle import *
from random import *
from tkinter import *
import pickle
import os
import winsound
os.system("cls")
pygame.init()                                       
clock = pygame.time.Clock()

#  VAR SETUP
text = "Start"
button_color = "red"
text_color = "white"
vitri_x = -525
vitri_y = 200

#pickle.dump(bank, open("bank.dat", "wb"))
bank = pickle.load(open("bank.dat", "rb"))
#bank = pickle.load(open("bank.dat", "rb"))
wager = 0       
choice = 0
temp = 0 # so sanh so tien de in ra thang thua
history = [[0, " ", 0], [0, " ", 0], [0, " ", 0],
            [0, " ", 0], [0, " ", 0]]
    #screen setup
screen = pygame.display.set_mode([800, 650])
font = pygame.font.SysFont(None, 32)
base_font = pygame.font.SysFont(None, 32)
title_font = pygame.font.SysFont(None, 60)
menu_font = pygame.font.SysFont(None, 40)
history_font = pygame.font.SysFont(None, 44)
def draw_text (text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_position = (x, y)
    surface.blit (textobj, text_position)
def lichsu():
    history_rect_x = 50
    history_rect_y = 50
    history_rect = pygame.Rect(history_rect_x, history_rect_y, 700, 550)
    thongtin_rect = pygame.Rect(history_rect_x, history_rect_y, 700, 50)
    thongtin1_rect = pygame.Rect(history_rect_x, history_rect_y, 650 * 0.35, 50)
    thongtin2_rect = pygame.Rect(history_rect_x + 650 * 0.35, history_rect_y, 650 * 0.35 , 50)
    thongtin3_rect = pygame.Rect(history_rect_x + 650 * 0.7 , history_rect_y, 650 * 0.38, 50)
    thongtin4_rect = pygame.Rect(0, 0, 30, 30)
    lichsu1_rect = pygame.Rect(history_rect_x, history_rect_y + 50, 700, 100)
    lichsu2_rect = pygame.Rect(history_rect_x, history_rect_y + 150, 700, 100)
    lichsu3_rect = pygame.Rect(history_rect_x, history_rect_y + 250, 700, 100)
    lichsu4_rect = pygame.Rect(history_rect_x, history_rect_y + 350, 700, 100)
    lichsu5_rect = pygame.Rect(history_rect_x, history_rect_y + 450, 700, 100)
    history_running = True
    while history_running:
        background = pygame.image.load('racetypes.gif')
        for event in pygame.event.get():
                # bam nut cheo x se out
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        history_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if thongtin4_rect.collidepoint(event.pos): 
                        history_running = False


        screen.fill((250, 250, 250))
        screen.blit(background, (0,0))

        pygame.draw.rect(screen, "orange", history_rect, 6)
        pygame.draw.rect(screen,"orange", thongtin_rect, 6)
        pygame.draw.rect(screen,"orange", thongtin1_rect, 1)
        pygame.draw.rect(screen,"orange", thongtin2_rect, 1)
        pygame.draw.rect(screen,"orange", thongtin3_rect, 1)
        pygame.draw.rect(screen,"orange", thongtin4_rect, 3)
        pygame.draw.rect(screen,"orange", lichsu1_rect, 1)
        pygame.draw.rect(screen,"orange", lichsu2_rect, 1)
        pygame.draw.rect(screen,"orange", lichsu3_rect, 1)
        pygame.draw.rect(screen,"orange", lichsu4_rect, 1)
        pygame.draw.rect(screen,"orange", lichsu5_rect, 1)
        new_history = pickle.load(open("history.dat", "rb"))
        draw_text("WAGER",menu_font, "white", screen, thongtin1_rect.x + 60, thongtin1_rect.y + 20 )
        draw_text("RESULT",menu_font, "white", screen, thongtin2_rect.x + 60, thongtin2_rect.y + 20 )
        draw_text("BANK",menu_font, "white", screen, thongtin3_rect.x + 80, thongtin3_rect.y + 20 )
        draw_text("X",menu_font, "white", screen, thongtin4_rect.x + 6, thongtin4_rect.y + 2 )
        lichsu1 = str(new_history[0][0])
        lichsu2 = new_history[0][1]
        lichsu3 = str(new_history[0][2])
        lichsu4 = str(new_history[1][0])
        lichsu5 = new_history[1][1]
        lichsu6 = str(new_history[1][2])
        lichsu7 = str(new_history[2][0])
        lichsu8 = new_history[2][1]
        lichsu9 = str(new_history[2][2])
        lichsu10 = str(new_history[3][0])
        lichsu11 = new_history[3][1]
        lichsu12 = str(new_history[3][2])
        lichsu13 = str(new_history[4][0])
        lichsu14 = new_history[4][1]
        lichsu15 = str(new_history[4][2])
        draw_text(lichsu1, history_font, "black", screen, thongtin1_rect.x + 90, thongtin1_rect.y + 80 )
        draw_text(lichsu2, history_font, "black", screen, thongtin2_rect.x + 90, thongtin2_rect.y + 80 )
        draw_text(lichsu3, history_font, "black", screen, thongtin3_rect.x + 90, thongtin3_rect.y + 80 )
        draw_text(lichsu4, history_font, "black", screen, thongtin1_rect.x + 90, thongtin1_rect.y + 80 +100)
        draw_text(lichsu5, history_font, "black", screen, thongtin2_rect.x + 90, thongtin2_rect.y + 80 +100)
        draw_text(lichsu6, history_font, "black", screen, thongtin3_rect.x + 90, thongtin3_rect.y + 80 +100)
        draw_text(lichsu7, history_font, "black", screen, thongtin1_rect.x + 90, thongtin1_rect.y + 80 +200)
        draw_text(lichsu8, history_font, "black", screen, thongtin2_rect.x + 90, thongtin2_rect.y + 80 +200)
        draw_text(lichsu9, history_font, "black", screen, thongtin3_rect.x + 90, thongtin3_rect.y + 80 +200)
        draw_text(lichsu10, history_font, "black", screen, thongtin1_rect.x + 90, thongtin1_rect.y + 80 +300)
        draw_text(lichsu11, history_font, "black", screen, thongtin2_rect.x + 90, thongtin2_rect.y + 80 +300)
        draw_text(lichsu12, history_font, "black", screen, thongtin3_rect.x + 90, thongtin3_rect.y + 80 +300)
        draw_text(lichsu13, history_font, "black", screen, thongtin1_rect.x + 90, thongtin1_rect.y + 80 +400)
        draw_text(lichsu14, history_font, "black", screen, thongtin2_rect.x + 90, thongtin2_rect.y + 80 +400)
        draw_text(lichsu15, history_font, "black", screen, thongtin3_rect.x + 90, thongtin3_rect.y + 80 +400)

        pygame.display.flip()
        clock.tick(60)
def mini_game():
    # load hình ảnh
    m = 20 # kích thước chiều cao và chiều rộng
    mini_background = pygame.image.load('history.gif')
    Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(m,m))
    Imghead = pygame.transform.scale(pygame.image.load('head.jpg'),(m,m))
    Imgfood = pygame.transform.scale(pygame.image.load('covid.png'),(m,m))
    # tạo cửa sổ
    gameSurface = pygame.display.set_mode((800,650))
    pygame.display.set_caption('Snake Covid-19!')
    # màu sắc
    red = pygame.Color(255,0,0)
    blue = pygame.Color(65,105,255)
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    gray = pygame.Color(128,128,128)
    # khai báo biến
    snakepos = [100,60]
    snakebody = [[100,60],[80,60],[60,60]]
    foodx = randrange(1,71)
    foody = randrange(1,45)
    if foodx % 2 != 0: foodx += 1
    if foody % 2 != 0: foody += 1
    foodpos = [foodx * 10, foody * 10]
    foodflat = True
    direction = 'RIGHT'
    changeto = direction
    global bank
    score = 0
    # hàm gameover
    def game_over():
        gfont = pygame.font.SysFont('consolas',40)
        gsurf = gfont.render('Game over!',True,red)
        grect = gsurf.get_rect()
        grect.midtop = (360,150)
        gameSurface.blit(gsurf,grect)
        show_score(0)
        pygame.display.flip()
        time.sleep(1) #time wait to exit

        #pygame.quit()
        #sys.exit()
    # hàm show_score
    def show_score(choice = 1):
        sfont = pygame.font.SysFont('consolas',20)
        ssurf = sfont.render('Score: {0}'.format(score),True,black)
        srect = ssurf.get_rect()
        if choice == 1:
            srect.midtop = (70,20)
        else:
            srect.midtop = (360,230)
        gameSurface.blit(ssurf,srect)
    winsound.PlaySound("menu.wav", winsound.SND_ASYNC)
    # vòng lặp chính
    minigame_running = True
    while minigame_running:
        
        pygame.time.delay(200) # tốc độ chơi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # xử lý phím
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.evet.Event(pygame.QUIT))
        # hướng đi
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        # cập nhật vị trí mới
        if direction == 'RIGHT':
            snakepos[0] += m
        if direction == 'LEFT':
            snakepos[0] -= m
        if direction == 'UP':
            snakepos[1] -= m
        if direction == 'DOWN':
            snakepos[1] += m
        #cơ chế thêm khúc dài ra
        snakebody.insert(0,list(snakepos))
        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            score += 1
            bank += 1
            print (bank)
            foodflat = False
        else:
            snakebody.pop()
        # sản sinh covid
        if foodflat == False:
            foodx = randrange(1,71)
            foody = randrange(1,45)
            if foodx %2 != 0: foodx += 1
            if foody %2 != 0: foody += 1
            foodpos = [foodx * 10, foody * 10]
        foodflat = True
        #  cập nhật lên cửa sổ
        gameSurface.fill(white)
        gameSurface.blit(mini_background,(0,0))
        for pos in snakebody:
            gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))
            #pygame.draw.rect(gameSurface,blue,pygame.Rect(pos[0],pos[1],m,m))
        gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m)) # head
        gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))
        #pygame.draw.rect(gameSurface,gray,pygame.Rect(foodpos[0],foodpos[1],m,m))
        # xử lý di chuyển đụng 4 cạnh biên
        if snakepos[0] > 710 or snakepos[0] < 10:
            game_over()
            minigame_running = False
        if snakepos[1] > 450 or snakepos[1] < 10:
            game_over()
            minigame_running = False
        # xử lý tự ăn chính mình
        for b in snakebody[1:]:
            if snakepos[0] == b[0] and snakepos[1] == b[1]:
                game_over()
                minigame_running = False
        # đường viền
        pygame.draw.rect(gameSurface,gray,(10,10,715,455),2)
        show_score()
        pygame.display.flip() 
def main_menu():
    
    background = pygame.image.load('mainmenunew.gif')
    while True:
        screen.blit(background,(0,0))
        draw_text("MAIN MENU", title_font, "lightblue", screen, 280, 500)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(70, 80, 170, 35)
        button_2 = pygame.Rect(320, 80, 170, 35)
        button_3 = pygame.Rect(550, 80, 170, 35)
        button_4 = pygame.Rect(320, 200, 170, 35)
        draw_text("Game", menu_font, "white", screen, button_1.x + 40, button_1.y + 5)
        draw_text("History", menu_font, "white", screen, button_2.x + 40, button_2.y + 5)
        draw_text("Mini Game", menu_font, "white", screen, button_3.x + 20, button_3.y + 5)
        draw_text("Exit", menu_font, "white", screen, button_4.x + 60, button_4.y + 5)
        if button_1.collidepoint ((mx, my)):
            # BAM VAO O VUONG 1. (GIAO DIEN GAME)
            if click:
                race_types()
        if button_2.collidepoint ((mx, my)):
            if click:
                lichsu() # history
        if button_3.collidepoint ((mx, my)): 
            if click:
                mini_game() # minigame
        if button_4.collidepoint ((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, "orange", button_1, 4)
        pygame.draw.rect(screen, "orange", button_2, 4)
        pygame.draw.rect(screen, "orange", button_3, 4)
        pygame.draw.rect(screen, "orange", button_4, 4)

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
def user_name():
        #content setup
    winsound.PlaySound("menu.wav", winsound.SND_ASYNC)
    color_active = pygame.Color("gray")
    color_passive = pygame.Color("gray15")
    color = color_passive
    background = pygame.image.load('mainmenunew.gif')
    user_text = 'enter username: '
    game_title = "TURTLE GAME"
    #demo_font = pygame.font.Font('8-BIT WONDER.TTF', 50)

    # tao khung dien username, switch screen
    username_button = pygame.Rect(280, 100, 240 , 35)
    switchscreen_button = pygame.Rect(480, 100, 40, 35)
    
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
        pygame.draw.rect(screen, color, username_button, 4)
        pygame.draw.rect(screen, color, switchscreen_button, 4)

        draw_text(">>", menu_font , "black", screen, switchscreen_button.x + 5, switchscreen_button.y )
        draw_text(game_title, title_font, "black", screen, 250, 160)
        draw_text(user_text, base_font, "black", screen, username_button.x + 5, username_button.y + 5)
        pygame.display.flip()
        clock.tick(60)
def dua_ngan():
    def draw_button(vitri_x, vitri_y, button_color, text_color, text):
        pen = Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x, vitri_y)
        pen.color(button_color)
        # to dam nen
        pen.begin_fill()
        for i in range (2):
            pen.forward(100)
            pen.left(90)
            pen.forward(40)
            pen.left(90)
        pen.end_fill()
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x + 30 , vitri_y + 10)
        pen.color(text_color)
        pen.write(text, font = ("Arial", 16, "bold"))
    def draw_smallbutton(vitri_x, vitri_y, button_color, text_color, text):
        pen = Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x, vitri_y)
        pen.color(button_color)
        # to dam nen
        pen.begin_fill()
        for i in range (2):
            pen.forward(70)
            pen.left(90)
            pen.forward(30)
            pen.left(90)
        pen.end_fill()
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x + 20 , vitri_y + 5)
        pen.color(text_color)
        pen.write(text, font = ("Arial", 16, "bold"))
    def cacuoc():
        # key down function
        def click():    #submit BUTTON
            global bank
            global choice
            global wager
            char_text = int(char_textentry.get())
            money_text = int(money_textentry.get()) 
            if char_text <= 6 and char_text > 0 and money_text <= bank:
                choice = char_text # collect character (nhan vat)
                wager = money_text # collect text (tien cuoc)
                Label(window, text = "submitted !!!         .       ", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                draw_smallbutton(vitri_x + 110, vitri_y, "red", "white", choice)
                draw_smallbutton(vitri_x + 190, vitri_y, "yellow", "black", wager)
                window.destroy()
                exit()
            else:
                if char_text > 6 or char_text <= 0:
                    Label(window, text = "invalid choice !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter choice again !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)
                else:
                    Label(window, text = "not enough money !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter wager again !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)              
        ## main
        window = Tk()
        window.title("Gambling")
        window.geometry("200x180")
        window.configure(background = "white")
        #window.resizable(0,0)
        # photo
        #photo1 = PhotoImage(file = 'cho1.gif')
        #Label (window, image = photo1, bg = "white") .grid(row = 0, column = 0, sticky = E)
        # create label
        Label(window, text = "Enter character(1 - 6)", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 1, column = 0, sticky = W) 
        Label(window, text = "Enter wager", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 3, column = 0, sticky = W)

        #   create a text entry box
        char_textentry = Entry(window, width = 25)
        char_textentry.grid(row = 2, column = 0, sticky = W)
        money_textentry = Entry(window, width = 25)
        money_textentry.grid(row = 4, column = 0, sticky = W)
        # add a submit button
        Button(window, text = "Submit", width = 6, command = click) .grid(row = 6, column = 0, sticky = W)
        # run the main loop
        #window.mainloop()

        #SCREEN SETUP
    ### GIAO DIEN CHO 
    print("bank o ham dua ngan")
    print(bank)
    draw_button(vitri_x, vitri_y, button_color, text_color, text)
    draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
    setup(1050, 650)
    title("Turtle Race")
    bgcolor("white")
    bgpic("dua6.gif")
    speed(0)
    ### LANE SETUP
    # HEADING
    penup()
    goto(-150, 205)
    color("red")
    write("TURTLE RACE", font=("Arial", 40, "bold"))
    #DIRT (DON LAI DUONG DUA)
    goto(-525, 200)
    pendown()
    color("orange")
    begin_fill()
    for i in range(2):
        forward(1050)
        ## 350 la` end cua duong dua
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
    winsound.PlaySound("dua.wav", winsound.SND_ASYNC)
        # HIEN THI CAC NHAN VAT
    # KHAI BAO RUA
    blue_turtle = Turtle()
    pink_turtle = Turtle()
    yellow_turtle = Turtle()
    green_turtle = Turtle()
    red_turtle = Turtle()
    black_turtle = Turtle()

    addshape("rua4.gif")
    addshape("chim3.gif")
    addshape("cho5.gif")
    addshape("meo4.gif")
    addshape("Car5.gif")
    blue_turtle.shape("rua4.gif")
    blue_turtle.penup()
    blue_turtle.goto(-340, 100 -30)

    pink_turtle.shape("chim3.gif")
    pink_turtle.penup()
    pink_turtle.goto(-170, 100 -30)

    yellow_turtle.shape("cho5.gif")
    yellow_turtle.penup()
    yellow_turtle.goto(0, 100 -30)

    green_turtle.shape("meo4.gif")
    green_turtle.penup()
    green_turtle.goto(-150, 0 -30)

    red_turtle.shape("Car5.gif")
    red_turtle.penup()
    red_turtle.goto(-320, 0 -30)
    def duangan():
        
        # VARIABLE SETUP 
        turtle.clear()
        global first_elapsed_time
        global second_elapsed_time
        global third_elapsed_time
        global fourth_elapsed_time
        global fifth_elapsed_time
        global sixth_elapsed_time
            # THEM VAO HINH ANH CAC NHAN VAT
        if True:

            addshape ("chim1.gif") 
            addshape ("chim1r.gif")
            addshape ("chim2.gif") 
            addshape ("chim2r.gif")
            addshape ("chim3.gif") 
            addshape ("chim3r.gif")
            addshape ("chim4.gif") 
            addshape ("chim4r.gif")
            addshape ("chim5.gif") 
            addshape ("chim5r.gif")
            addshape ("chim6.gif") 
            addshape ("chim6r.gif")
                # rua
            addshape ("rua1.gif") 
            addshape ("rua1r.gif")
            addshape ("rua2.gif") 
            addshape ("rua2r.gif")
            addshape ("rua3.gif") 
            addshape ("rua3r.gif")
            addshape ("rua4.gif") 
            addshape ("rua4r.gif")
            addshape ("rua5.gif") 
            addshape ("rua5r.gif")
            addshape ("rua6.gif") 
            addshape ("rua6r.gif")

                # cho
            addshape ("cho1.gif") 
            addshape ("cho1r.gif")
            addshape ("cho2.gif") 
            addshape ("cho2r.gif")
            addshape ("cho3.gif") 
            addshape ("cho3r.gif")
            addshape ("cho4.gif") 
            addshape ("cho4r.gif")
            addshape ("cho5.gif") 
            addshape ("cho5r.gif")
            addshape ("cho6.gif") 
            addshape ("cho6r.gif")
                # MEO
            addshape ("meo1.gif") 
            addshape ("meo1r.gif")
            addshape ("meo2.gif") 
            addshape ("meo2r.gif")
            addshape ("meo3.gif") 
            addshape ("meo3r.gif")
            addshape ("meo4.gif") 
            addshape ("meo4r.gif")
            addshape ("meo5.gif") 
            addshape ("meo5r.gif")
            addshape ("meo6.gif") 
            addshape ("meo6r.gif")
            # XE
            addshape ("Car1.gif") 
            addshape ("Car1r.gif")
            addshape ("Car2.gif") 
            addshape ("Car2r.gif")
            addshape ("Car3.gif") 
            addshape ("Car3r.gif")
            addshape ("Car4.gif") 
            addshape ("Car4r.gif")
            addshape ("Car5.gif") 
            addshape ("Car5r.gif")
            addshape ("Car6.gif") 
            addshape ("Car6r.gif")  
        #bgpic('background.gif')
        # SCREEN SETUP
        # setup(1050, 650)
        # title("Turtle Race")
        # bgcolor("white")
        # speed(0)
        character = 1
        while True:
            winsound.PlaySound("dua.wav", winsound.SND_ASYNC)
            # SET LAI TIEN CUOC
            cacuoc()
            # xong 1 nv se doi nhan vat khac (rua = 1 -> cho = ?)
            if character > 5:
                character = 1
            
            # HEADING
            penup()
            goto(-150, 205)
            color("red")
            write("TURTLE RACE", font=("Arial", 40, "bold"))
            #DIRT (DON LAI DUONG DUA)
            goto(-525, 200)
            pendown()
            color("orange")
            begin_fill()
            for i in range(2):
                forward(1050)
                ## 350 la` end cua duong dua
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
            # KHAI BAO RUA
            blue_turtle = Turtle()
            pink_turtle = Turtle()
            yellow_turtle = Turtle()
            green_turtle = Turtle()
            red_turtle = Turtle()
            black_turtle = Turtle()

            #Khai Bao Con Tro Print
            print_turtle = Turtle()
            print_turtle.penup()
            print_turtle.hideturtle()

            
                #DOI NHAN VAT (chua chen nhan vat) + SETUP NHAN VAT
            if character == 1:
                # chim
                blue_turtle.shape("rua1.gif")
                pink_turtle.shape("rua2.gif")
                yellow_turtle.shape("rua3.gif")
                green_turtle.shape("rua4.gif")
                red_turtle.shape("rua5.gif")
                black_turtle.shape("rua6.gif")
            elif character == 2:
                #xe
                blue_turtle.shape("chim1.gif")
                pink_turtle.shape("chim2.gif")
                yellow_turtle.shape("chim3.gif")
                green_turtle.shape("chim4.gif")
                red_turtle.shape("chim5.gif")
                black_turtle.shape("chim6.gif")
            elif character == 3:
                blue_turtle.shape("cho1.gif")
                pink_turtle.shape("cho2.gif")
                yellow_turtle.shape("cho3.gif")
                green_turtle.shape("cho4.gif")
                red_turtle.shape("cho5.gif")
                black_turtle.shape("cho6.gif")
            elif character == 4:
                blue_turtle.shape("meo1.gif")
                pink_turtle.shape("meo2.gif")
                yellow_turtle.shape("meo3.gif")
                green_turtle.shape("meo4.gif")
                red_turtle.shape("meo5.gif")
                black_turtle.shape("meo6.gif")
            elif character == 5:
                blue_turtle.shape("Car1.gif")
                pink_turtle.shape("Car2.gif")
                yellow_turtle.shape("Car3.gif")
                green_turtle.shape("Car4.gif")
                red_turtle.shape("Car5.gif")
                black_turtle.shape("Car6.gif")

            blue_turtle.shapesize(1.5)
            pink_turtle.shapesize(1.5)
            yellow_turtle.shapesize(1.5)
            green_turtle.shapesize(1.5)
            red_turtle.shapesize(1.5)
            black_turtle.shapesize(1.5)

            # KHONG VE~ TREN DUONG DI
            blue_turtle.penup()
            pink_turtle.penup()
            yellow_turtle.penup()
            green_turtle.penup()
            red_turtle.penup()
            black_turtle.penup()
            # Set toa do rua`
            blue_turtle_x = -450
            blue_turtle_y = 140
            pink_turtle_x = -450
            pink_turtle_y = 90
            yellow_turtle_x = -450
            yellow_turtle_y = 30
            green_turtle_x = -450
            green_turtle_y = -30
            red_turtle_x = -450
            red_turtle_y = -90
            black_turtle_x = -450
            black_turtle_y = -150

            # DUA RUA` DEN CAC VI TRI
            blue_turtle.speed(2)
            pink_turtle.speed(2)
            yellow_turtle.speed(2)
            green_turtle.speed(1)
            red_turtle.speed(1)
            black_turtle.speed(1)
            blue_turtle.goto(blue_turtle_x, blue_turtle_y)
            pink_turtle.goto(pink_turtle_x, pink_turtle_y)
            yellow_turtle.goto(yellow_turtle_x, yellow_turtle_y)
            green_turtle.goto(green_turtle_x, green_turtle_y)
            red_turtle.goto(red_turtle_x, red_turtle_y)   
            black_turtle.goto(black_turtle_x, black_turtle_y)

        #PAUSE FOR 1 SECOND BEFORE RACING
            time.sleep(1)
            blue_turtle.speed(0)
            pink_turtle.speed(0)
            yellow_turtle.speed(0)
            green_turtle.speed(0)
            red_turtle.speed(0)
            black_turtle.speed(0)
        #MOVE THE  TURTLE
            # nho doi lai turn = randint (1,6)
            # STOP SCREEN UNTIL CHOICE IS SUBMITTED
            global choice   # choice o ham ca cuoc
            global wager    # wager o tren ham ca cuoc
            global bank     # bank duoc dung` de so sanh o cacuoc()
            global temp
            global temp_wager # luu lai muc cuoc
            temp = bank
            temp_wager = wager
            if choice != 0 and wager != 0:
                turn = randint(1,6)
                stop = randint(1,6)
                global start_time
                start_time = time.time()
                while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and red_turtle.xcor() <= 230 and black_turtle.xcor() <= 230 :
                    blue_turtle.forward(randint(1, 18))
                    pink_turtle.forward(randint(1, 18))
                    yellow_turtle.forward(randint(1, 18))
                    green_turtle.forward(randint(1, 18))
                    red_turtle.forward(randint(1, 18))
                    black_turtle.forward(randint(1, 18))
                    first_elapsed_time = '%.5s'%(time.time() - start_time)
                    #print (first_elapsed_time)
                    # GHEP NHAC NHANH
                    if blue_turtle.xcor() > -200:
                        winsound.PlaySound("duanhanh.wav", winsound.SND_ASYNC)
                    # QUAY DAU (On~)
                    if blue_turtle.xcor() >= -20 and pink_turtle.xcor() >= -20 and yellow_turtle.xcor() >= -20 and green_turtle.xcor() >= -20 and red_turtle.xcor() >=-20 and black_turtle.xcor() >= -20 :
                        if turn != 0:
                            #for i in range (2):
                                if turn == 1:
                                    if character == 1:
                                        blue_turtle.shape("rua1r.gif")
                                    elif character == 2:
                                        blue_turtle.shape("chim1r.gif")
                                    elif character == 3:
                                        blue_turtle.shape("cho1r.gif")
                                    elif character == 4:
                                        blue_turtle.shape("meo1r.gif")
                                    elif character == 5:
                                        blue_turtle.shape("Car1r.gif")
                                    for i in range (8):
                                        blue_turtle.backward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        blue_turtle.shape("rua1.gif")
                                    elif character == 2:
                                        blue_turtle.shape("chim1.gif")
                                    elif character == 3:
                                        blue_turtle.shape("cho1.gif")
                                    elif character == 4:
                                        blue_turtle.shape("meo1.gif")
                                    elif character == 5:
                                        blue_turtle.shape("Car1.gif")
                                elif turn == 2:
                                    if character == 1:
                                        pink_turtle.shape("rua2r.gif")
                                    elif character == 2:
                                        pink_turtle.shape("chim2r.gif")
                                    elif character == 3:
                                        pink_turtle.shape("cho2r.gif")
                                    elif character == 4:
                                        pink_turtle.shape("meo2r.gif")
                                    elif character == 5:
                                        pink_turtle.shape("Car2r.gif")
                                    for i in range (8):
                                        pink_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        pink_turtle.shape("rua2.gif")
                                    elif character == 2:
                                        pink_turtle.shape("chim2.gif")
                                    elif character == 3:
                                        pink_turtle.shape("cho2.gif")
                                    elif character == 4:
                                        pink_turtle.shape("meo2.gif")
                                    elif character == 5:
                                        pink_turtle.shape("Car2.gif")
                                elif turn == 3:
                                    if character == 1:
                                        yellow_turtle.shape("rua3r.gif")
                                    elif character == 2:
                                        yellow_turtle.shape("chim3r.gif")
                                    elif character == 3:
                                        yellow_turtle.shape("cho3r.gif")
                                    elif character == 4:
                                        yellow_turtle.shape("meo3r.gif")
                                    elif character == 5:
                                        yellow_turtle.shape("Car3r.gif")
                                    for i in range (8):
                                        yellow_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        yellow_turtle.shape("rua3.gif")
                                    elif character == 2:
                                        yellow_turtle.shape("chim3.gif")
                                    elif character == 3:
                                        yellow_turtle.shape("cho3.gif")
                                    elif character == 4:
                                        yellow_turtle.shape("meo3.gif")
                                    elif character == 5:
                                        yellow_turtle.shape("Car3.gif")
                                elif turn == 4:
                                    if character == 1:
                                        green_turtle.shape("rua4r.gif")
                                    elif character == 2:
                                        green_turtle.shape("chim4r.gif")
                                    elif character == 3:
                                        green_turtle.shape("cho4r.gif")
                                    elif character == 4:
                                        green_turtle.shape("meo4r.gif")
                                    elif character == 5:
                                        green_turtle.shape("Car4r.gif")
                                    for i in range (8):
                                        green_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        green_turtle.shape("rua4.gif")
                                    elif character == 2:
                                        green_turtle.shape("chim4.gif")
                                    elif character == 3:
                                        green_turtle.shape("cho4.gif")
                                    elif character == 4:
                                        green_turtle.shape("meo4.gif")
                                    elif character == 5:
                                        green_turtle.shape("Car4.gif")
                                elif turn == 5:
                                    if character == 1:
                                        red_turtle.shape("rua5r.gif")
                                    elif character == 2:
                                        red_turtle.shape("chim5r.gif")
                                    elif character == 3:
                                        red_turtle.shape("cho5r.gif")
                                    elif character == 4:
                                        red_turtle.shape("meo5r.gif")
                                    elif character == 5:
                                        red_turtle.shape("Car5r.gif")
                                    for i in range (8):
                                        red_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        red_turtle.shape("rua5.gif")
                                    elif character == 2:
                                        red_turtle.shape("chim5.gif")
                                    elif character == 3:
                                        red_turtle.shape("cho5.gif")
                                    elif character == 4:
                                        red_turtle.shape("meo5.gif")
                                    elif character == 5:
                                        red_turtle.shape("Car5.gif")
                                elif turn == 6:
                                    if character == 1:
                                        black_turtle.shape("rua6r.gif")
                                    elif character == 2:
                                        black_turtle.shape("chim6r.gif")
                                    elif character == 3:
                                        black_turtle.shape("cho6r.gif")
                                    elif character == 4:
                                        black_turtle.shape("meo6r.gif")
                                    elif character == 5:
                                        black_turtle.shape("Car6r.gif")
                                    for i in range (8):
                                        black_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                    if character == 1:
                                        black_turtle.shape("rua6.gif")
                                    elif character == 2:
                                        black_turtle.shape("chim6.gif")
                                    elif character == 3:
                                        black_turtle.shape("cho6.gif")
                                    elif character == 4:
                                        black_turtle.shape("meo6.gif")
                                    elif character == 5:
                                        black_turtle.shape("Car6.gif") 
                                turn = 0
                    # STOPP        
                    if blue_turtle.xcor() >= -300: 
                        if stop != 0:
                            #blue stop
                            if stop == 1:
                                for i in range (20):
                                    #blue ko chay
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 2:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    #pink khong chay
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 3:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    # yellow stop
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 4:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    #green stop
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 5:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    #red stop
                                    black_turtle.forward(randint(1, 10))
                            if stop == 6:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    #black stop
                            stop = 0
                        
            #CELEBRATE THE WINNER + TIME
                #BLUE WIN
                if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > black_turtle.xcor():
                    #global choice # khong can dung nua tai o tren co dung` rui`
                    # bank setup
                    if choice == 1:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            blue_turtle.shape("rua6.gif")
                            blue_turtle.shape("rua2.gif")
                            blue_turtle.shape("rua3.gif")
                            blue_turtle.shape("rua4.gif")
                            blue_turtle.shape("rua5.gif")
                            blue_turtle.shape("rua1.gif")
                        if character == 2:
                            blue_turtle.shape("chim6.gif")
                            blue_turtle.shape("chim2.gif")
                            blue_turtle.shape("chim3.gif")
                            blue_turtle.shape("chim4.gif")
                            blue_turtle.shape("chim5.gif")
                            blue_turtle.shape("chim1.gif")
                        if character == 3:
                            blue_turtle.shape("cho6.gif")
                            blue_turtle.shape("cho2.gif")
                            blue_turtle.shape("cho3.gif")
                            blue_turtle.shape("cho4.gif")
                            blue_turtle.shape("cho5.gif")
                            blue_turtle.shape("cho1.gif")
                        if character == 4:
                            blue_turtle.shape("meo6.gif")
                            blue_turtle.shape("meo2.gif")
                            blue_turtle.shape("meo3.gif")
                            blue_turtle.shape("meo4.gif")
                            blue_turtle.shape("meo5.gif")
                            blue_turtle.shape("meo1.gif")
                        if character == 5:
                            blue_turtle.shape("Car6.gif")
                            blue_turtle.shape("Car2.gif")
                            blue_turtle.shape("Car3.gif")
                            blue_turtle.shape("Car4.gif")
                            blue_turtle.shape("Car5.gif")
                            blue_turtle.shape("Car1.gif")

                    print_turtle.goto(blue_turtle_x + 705 + 60, blue_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    # may con con` lai chay tiep.
                    while pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                        if pink_turtle.xcor() <= 230:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 230:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 230:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))  
                        if red_turtle.xcor() <= 230:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 230:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    #  IN RA DUONG DUA O DAY.
                    print_turtle.goto(pink_turtle_x + 705 + 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705 + 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705 + 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705 + 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705 + 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))   

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold")) 
                #PINK WIN
                elif  pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor() and pink_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 2:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            pink_turtle.shape("rua6.gif")
                            pink_turtle.shape("rua2.gif")
                            pink_turtle.shape("rua3.gif")
                            pink_turtle.shape("rua4.gif")
                            pink_turtle.shape("rua5.gif")
                            pink_turtle.shape("rua2.gif")
                        if character == 2:
                            pink_turtle.shape("chim6.gif")
                            pink_turtle.shape("chim1.gif")
                            pink_turtle.shape("chim3.gif")
                            pink_turtle.shape("chim4.gif")
                            pink_turtle.shape("chim5.gif")
                            pink_turtle.shape("chim2.gif")
                        if character == 3:
                            pink_turtle.shape("cho6.gif")
                            pink_turtle.shape("cho1.gif")
                            pink_turtle.shape("cho3.gif")
                            pink_turtle.shape("cho4.gif")
                            pink_turtle.shape("cho5.gif")
                            pink_turtle.shape("cho2.gif")
                        if character == 4:
                            pink_turtle.shape("meo6.gif")
                            pink_turtle.shape("meo1.gif")
                            pink_turtle.shape("meo3.gif")
                            pink_turtle.shape("meo4.gif")
                            pink_turtle.shape("meo5.gif")
                            pink_turtle.shape("meo2.gif")
                        if character == 5:
                            pink_turtle.shape("Car6.gif")
                            pink_turtle.shape("Car1.gif")
                            pink_turtle.shape("Car3.gif")
                            pink_turtle.shape("Car4.gif")
                            pink_turtle.shape("Car5.gif")
                            pink_turtle.shape("Car2.gif")
                    print_turtle.goto(pink_turtle_x + 705 + 60, pink_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                        if blue_turtle.xcor() <= 230:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 230:   
                        
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 230:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))
                        if red_turtle.xcor() <= 230:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 230:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### Print time
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))  

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: blue_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write("1st" , font=("Arial", 20, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold")) 
                #YELLOW WIN
                elif  yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 3:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            yellow_turtle.shape("rua6.gif")
                            yellow_turtle.shape("rua2.gif")
                            yellow_turtle.shape("rua1.gif")
                            yellow_turtle.shape("rua4.gif")
                            yellow_turtle.shape("rua5.gif")
                            yellow_turtle.shape("rua3.gif")
                        if character == 2:
                            yellow_turtle.shape("chim6.gif")
                            yellow_turtle.shape("chim2.gif")
                            yellow_turtle.shape("chim1.gif")
                            yellow_turtle.shape("chim4.gif")
                            yellow_turtle.shape("chim5.gif")
                            yellow_turtle.shape("chim3.gif")
                        if character == 3:
                            yellow_turtle.shape("cho6.gif")
                            yellow_turtle.shape("cho2.gif")
                            yellow_turtle.shape("cho1.gif")
                            yellow_turtle.shape("cho4.gif")
                            yellow_turtle.shape("cho5.gif")
                            yellow_turtle.shape("cho3.gif")
                        if character == 4:
                            yellow_turtle.shape("meo6.gif")
                            yellow_turtle.shape("meo2.gif")
                            yellow_turtle.shape("meo1.gif")
                            yellow_turtle.shape("meo4.gif")
                            yellow_turtle.shape("meo5.gif")
                            yellow_turtle.shape("meo3.gif")
                        if character == 5:
                            yellow_turtle.shape("Car6.gif")
                            yellow_turtle.shape("Car2.gif")
                            yellow_turtle.shape("Car1.gif")
                            yellow_turtle.shape("Car4.gif")
                            yellow_turtle.shape("Car5.gif")
                            yellow_turtle.shape("Car3.gif")
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                        if pink_turtle.xcor() <= 230:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 230:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 230:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 230:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 230:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))

                    ### print time
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold")) 

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: blue_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #GREEN WIN
                elif green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > blue_turtle.xcor() and green_turtle.xcor() > yellow_turtle.xcor() and green_turtle.xcor() > red_turtle.xcor() and green_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 4:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            green_turtle.shape("rua6.gif")
                            green_turtle.shape("rua2.gif")
                            green_turtle.shape("rua1.gif")
                            green_turtle.shape("rua3.gif")
                            green_turtle.shape("rua5.gif")
                            green_turtle.shape("rua4.gif")
                        if character == 2:
                            green_turtle.shape("chim6.gif")
                            green_turtle.shape("chim2.gif")
                            green_turtle.shape("chim1.gif")
                            green_turtle.shape("chim3.gif")
                            green_turtle.shape("chim5.gif")
                            green_turtle.shape("chim4.gif")
                        if character == 3:
                            green_turtle.shape("cho6.gif")
                            green_turtle.shape("cho2.gif")
                            green_turtle.shape("cho1.gif")
                            green_turtle.shape("cho3.gif")
                            green_turtle.shape("cho5.gif")
                            green_turtle.shape("cho4.gif")
                        if character == 4:
                            green_turtle.shape("meo6.gif")
                            green_turtle.shape("meo2.gif")
                            green_turtle.shape("meo1.gif")
                            green_turtle.shape("meo3.gif")
                            green_turtle.shape("meo5.gif")
                            green_turtle.shape("meo4.gif")
                        if character == 5:
                            green_turtle.shape("Car6.gif")
                            green_turtle.shape("Car2.gif")
                            green_turtle.shape("Car1.gif")
                            green_turtle.shape("Car3.gif")
                            green_turtle.shape("Car5.gif")
                            green_turtle.shape("Car4.gif")
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or red_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                        if pink_turtle.xcor() <= 230:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 230:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 230:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 230:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 230:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### time
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: blue_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #RED WIN
                elif red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > green_turtle.xcor() and red_turtle.xcor() > yellow_turtle.xcor() and red_turtle.xcor() > black_turtle.xcor() :
                    # bank setup
                    if choice == 5:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            red_turtle.shape("rua6.gif")
                            red_turtle.shape("rua2.gif")
                            red_turtle.shape("rua1.gif")
                            red_turtle.shape("rua4.gif")
                            red_turtle.shape("rua3.gif")
                            red_turtle.shape("rua5.gif")
                        if character == 2:
                            red_turtle.shape("chim6.gif")
                            red_turtle.shape("chim2.gif")
                            red_turtle.shape("chim1.gif")
                            red_turtle.shape("chim4.gif")
                            red_turtle.shape("chim3.gif")
                            red_turtle.shape("chim5.gif")
                        if character == 3:
                            red_turtle.shape("cho6.gif")
                            red_turtle.shape("cho2.gif")
                            red_turtle.shape("cho1.gif")
                            red_turtle.shape("cho4.gif")
                            red_turtle.shape("cho3.gif")
                            red_turtle.shape("cho5.gif")
                        if character == 4:
                            red_turtle.shape("meo6.gif")
                            red_turtle.shape("meo2.gif")
                            red_turtle.shape("meo1.gif")
                            red_turtle.shape("meo4.gif")
                            red_turtle.shape("meo3.gif")
                            red_turtle.shape("meo5.gif")
                        if character == 5:
                            red_turtle.shape("Car6.gif")
                            red_turtle.shape("Car2.gif")
                            red_turtle.shape("Car1.gif")
                            red_turtle.shape("Car4.gif")
                            red_turtle.shape("Car3.gif")
                            red_turtle.shape("Car5.gif")
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or black_turtle.xcor() <= 230:
                        if pink_turtle.xcor() <= 230:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 230:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 230:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 230:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 230:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### TIME
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: blue_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #BLACK WIN
                else: 
                    # bank setup
                    if choice == 6:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            black_turtle.shape("rua5.gif")
                            black_turtle.shape("rua2.gif")
                            black_turtle.shape("rua1.gif")
                            black_turtle.shape("rua4.gif")
                            black_turtle.shape("rua3.gif")
                            black_turtle.shape("rua6.gif")
                        if character == 2:
                            black_turtle.shape("chim5.gif")
                            black_turtle.shape("chim2.gif")
                            black_turtle.shape("chim1.gif")
                            black_turtle.shape("chim4.gif")
                            black_turtle.shape("chim3.gif")
                            black_turtle.shape("chim6.gif")
                        if character == 3:
                            black_turtle.shape("cho5.gif")
                            black_turtle.shape("cho2.gif")
                            black_turtle.shape("cho1.gif")
                            black_turtle.shape("cho4.gif")
                            black_turtle.shape("cho3.gif")
                            black_turtle.shape("cho6.gif")
                        if character == 4:
                            black_turtle.shape("meo5.gif")
                            black_turtle.shape("meo2.gif")
                            black_turtle.shape("meo1.gif")
                            black_turtle.shape("meo4.gif")
                            black_turtle.shape("meo3.gif")
                            black_turtle.shape("meo6.gif")
                        if character == 5:
                            black_turtle.shape("Car5.gif")
                            black_turtle.shape("Car2.gif")
                            black_turtle.shape("Car1.gif")
                            black_turtle.shape("Car4.gif")
                            black_turtle.shape("Car3.gif")
                            black_turtle.shape("Car6.gif")
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 230 or pink_turtle.xcor() <= 230 or yellow_turtle.xcor() <= 230 or green_turtle.xcor() <= 230 or red_turtle.xcor() <= 230:
                        if pink_turtle.xcor() <= 230:
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 230:   
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 230:
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 230:         
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 230:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                    ### time 
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))
                    
                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: blue_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                
                if (bank > temp):
                    print_turtle.goto(-300, 0)
                    print_turtle.write("YOU WIN !!!", font=("Arial", 40, "bold"))
                    history[character - 1][0] = temp_wager
                    history[character - 1][1] = "win"
                    history[character - 1][2] = bank

                else:
                    print_turtle.goto(-300, 0)
                    print_turtle.write("YOU LOSE !!!", font=("Arial", 40, "bold"))
                    history[character - 1][0] = temp_wager
                    history[character - 1][1] = "lose"
                    history[character - 1][2] = bank
                # tang bien dem doi nhan vat
                character += 1
                time.sleep(2)
                # LICH SU
                pickle.dump(bank, open("bank.dat", "wb"))
                pickle.dump(history, open("history.dat", "wb"))
                new_history = pickle.load(open("history.dat", "rb"))
            else:
                turtle.clear()
                time.sleep(2)
    def start_button(x,y):  #dai 100 rong 40
        if x > vitri_x and x < vitri_x + 100 and y > vitri_y and y < vitri_y + 40:
            clear()
            duangan()

    turtle.onscreenclick(start_button, 1)
    turtle.listen()
    turtle.done()
def dua_vua():
    def draw_button(vitri_x, vitri_y, button_color, text_color, text):
        pen = Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x, vitri_y)
        pen.color(button_color)
        # to dam nen
        pen.begin_fill()
        for i in range (2):
            pen.forward(100)
            pen.left(90)
            pen.forward(40)
            pen.left(90)
        pen.end_fill()
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x + 30 , vitri_y + 10)
        pen.color(text_color)
        pen.write(text, font = ("Arial", 16, "bold"))
    def draw_smallbutton(vitri_x, vitri_y, button_color, text_color, text):
        pen = Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x, vitri_y)
        pen.color(button_color)
        # to dam nen
        pen.begin_fill()
        for i in range (2):
            pen.forward(70)
            pen.left(90)
            pen.forward(30)
            pen.left(90)
        pen.end_fill()
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x + 20 , vitri_y + 5)
        pen.color(text_color)
        pen.write(text, font = ("Arial", 16, "bold"))
    def cacuoc():
        # key down function
        def click():    #submit BUTTON
            global bank
            global choice
            global wager
            char_text = int(char_textentry.get())
            money_text = int(money_textentry.get()) 
            if char_text <= 6 and char_text > 0 and money_text <= bank:
                choice = char_text # collect character (nhan vat)
                wager = money_text # collect text (tien cuoc)
                Label(window, text = "submitted !!!         .       ", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                draw_smallbutton(vitri_x + 110, vitri_y, "red", "white", choice)
                draw_smallbutton(vitri_x + 190, vitri_y, "yellow", "black", wager)
                window.destroy()
                exit()
            else:
                if char_text > 6 or char_text <= 0:
                    Label(window, text = "invalid choice !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter choice again !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)
                else:
                    Label(window, text = "not enough money !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter wager again !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)              
        ## main
        window = Tk()
        window.title("Gambling")
        window.geometry("200x180")
        window.configure(background = "white")
        #window.resizable(0,0)
        # photo
        #photo1 = PhotoImage(file = 'cho1.gif')
        #Label (window, image = photo1, bg = "white") .grid(row = 0, column = 0, sticky = E)
        # create label
        Label(window, text = "Enter character(1 - 6)", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 1, column = 0, sticky = W) 
        Label(window, text = "Enter wager", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 3, column = 0, sticky = W)

        #   create a text entry box
        char_textentry = Entry(window, width = 25)
        char_textentry.grid(row = 2, column = 0, sticky = W)
        money_textentry = Entry(window, width = 25)
        money_textentry.grid(row = 4, column = 0, sticky = W)
        # add a submit button
        Button(window, text = "Submit", width = 6, command = click) .grid(row = 6, column = 0, sticky = W)
        # run the main loop
        #window.mainloop()

        #SCREEN SETUP
    ### GIAO DIEN CHO 
    draw_button(vitri_x, vitri_y, button_color, text_color, text)
    draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
    setup(1050, 650)
    title("Turtle Race")
    bgcolor("white")
    bgpic("dua6.gif")
    speed(0)
    ### LANE SETUP
    # HEADING
    penup()
    goto(-150, 205)
    color("red")
    write("TURTLE RACE", font=("Arial", 40, "bold"))
    #DIRT (DON LAI DUONG DUA)
    goto(-525, 200)
    pendown()
    color("orange")
    begin_fill()
    for i in range(2):
        forward(1050)
        ## 350 la` end cua duong dua
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
        goto(300, (170 - (i * gap_size * 2)))
        stamp()
    # WHITE SQUARES ROW 2
    for i in range(10):
        goto(300 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        stamp()
    # BLACK SQUARES ROW 1
    color("black")
    for i in range(10):
        goto(300, (190 - (i * gap_size * 2)))
        stamp()
    # BLACK SQUARES ROW 2
    for i in range(10):
        goto(301 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        stamp()
    winsound.PlaySound("dua.wav", winsound.SND_ASYNC)
        # HIEN THI CAC NHAN VAT
    # KHAI BAO RUA
    blue_turtle = Turtle()
    pink_turtle = Turtle()
    yellow_turtle = Turtle()
    green_turtle = Turtle()
    red_turtle = Turtle()
    black_turtle = Turtle()

    addshape("rua4.gif")
    addshape("chim3.gif")
    addshape("cho5.gif")
    addshape("meo4.gif")
    addshape("Car5.gif")
    blue_turtle.shape("rua4.gif")
    blue_turtle.penup()
    blue_turtle.goto(-340, 100 -30)

    pink_turtle.shape("chim3.gif")
    pink_turtle.penup()
    pink_turtle.goto(-170, 100 -30)

    yellow_turtle.shape("cho5.gif")
    yellow_turtle.penup()
    yellow_turtle.goto(0, 100 -30)

    green_turtle.shape("meo4.gif")
    green_turtle.penup()
    green_turtle.goto(-150, 0 -30)

    red_turtle.shape("Car5.gif")
    red_turtle.penup()
    red_turtle.goto(-320, 0 -30)



    def duangan():
        # VARIABLE SETUP 
        turtle.clear()
        global first_elapsed_time
        global second_elapsed_time
        global third_elapsed_time
        global fourth_elapsed_time
        global fifth_elapsed_time
        global sixth_elapsed_time
            # THEM VAO HINH ANH CAC NHAN VAT
        if True:

            addshape ("chim1.gif") 
            addshape ("chim1r.gif")
            addshape ("chim2.gif") 
            addshape ("chim2r.gif")
            addshape ("chim3.gif") 
            addshape ("chim3r.gif")
            addshape ("chim4.gif") 
            addshape ("chim4r.gif")
            addshape ("chim5.gif") 
            addshape ("chim5r.gif")
            addshape ("chim6.gif") 
            addshape ("chim6r.gif")
                # rua
            addshape ("rua1.gif") 
            addshape ("rua1r.gif")
            addshape ("rua2.gif") 
            addshape ("rua2r.gif")
            addshape ("rua3.gif") 
            addshape ("rua3r.gif")
            addshape ("rua4.gif") 
            addshape ("rua4r.gif")
            addshape ("rua5.gif") 
            addshape ("rua5r.gif")
            addshape ("rua6.gif") 
            addshape ("rua6r.gif")

                # cho
            addshape ("cho1.gif") 
            addshape ("cho1r.gif")
            addshape ("cho2.gif") 
            addshape ("cho2r.gif")
            addshape ("cho3.gif") 
            addshape ("cho3r.gif")
            addshape ("cho4.gif") 
            addshape ("cho4r.gif")
            addshape ("cho5.gif") 
            addshape ("cho5r.gif")
            addshape ("cho6.gif") 
            addshape ("cho6r.gif")
                # MEO
            addshape ("meo1.gif") 
            addshape ("meo1r.gif")
            addshape ("meo2.gif") 
            addshape ("meo2r.gif")
            addshape ("meo3.gif") 
            addshape ("meo3r.gif")
            addshape ("meo4.gif") 
            addshape ("meo4r.gif")
            addshape ("meo5.gif") 
            addshape ("meo5r.gif")
            addshape ("meo6.gif") 
            addshape ("meo6r.gif")
            # XE
            addshape ("Car1.gif") 
            addshape ("Car1r.gif")
            addshape ("Car2.gif") 
            addshape ("Car2r.gif")
            addshape ("Car3.gif") 
            addshape ("Car3r.gif")
            addshape ("Car4.gif") 
            addshape ("Car4r.gif")
            addshape ("Car5.gif") 
            addshape ("Car5r.gif")
            addshape ("Car6.gif") 
            addshape ("Car6r.gif")  
        #bgpic('background.gif')
        # SCREEN SETUP
        # setup(1050, 650)
        # title("Turtle Race")
        # bgcolor("white")
        # speed(0)
        character = 1
        while True:
            winsound.PlaySound("dua.wav", winsound.SND_ASYNC)
            # SET LAI TIEN CUOC
            cacuoc()
            # xong 1 nv se doi nhan vat khac (rua = 1 -> cho = ?)
            if character > 5:
                character = 1
            
            # HEADING
            penup()
            goto(-150, 205)
            color("red")
            write("TURTLE RACE", font=("Arial", 40, "bold"))
            #DIRT (DON LAI DUONG DUA)
            goto(-525, 200)
            pendown()
            color("orange")
            begin_fill()
            for i in range(2):
                forward(1050)
                ## 350 la` end cua duong dua
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
                goto(300, (170 - (i * gap_size * 2)))
                stamp()

            # WHITE SQUARES ROW 2
            for i in range(10):
                goto(300 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
                stamp()

            # BLACK SQUARES ROW 1
            color("black")
            for i in range(10):
                goto(300, (190 - (i * gap_size * 2)))
                stamp()

            # BLACK SQUARES ROW 2
            for i in range(10):
                goto(301 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
                stamp()
            # KHAI BAO RUA
            blue_turtle = Turtle()
            pink_turtle = Turtle()
            yellow_turtle = Turtle()
            green_turtle = Turtle()
            red_turtle = Turtle()
            black_turtle = Turtle()

            #Khai Bao Con Tro Print
            print_turtle = Turtle()
            print_turtle.penup()
            print_turtle.hideturtle()

            
                #DOI NHAN VAT (chua chen nhan vat) + SETUP NHAN VAT
            if character == 1:
                # chim
                blue_turtle.shape("rua1.gif")
                pink_turtle.shape("rua2.gif")
                yellow_turtle.shape("rua3.gif")
                green_turtle.shape("rua4.gif")
                red_turtle.shape("rua5.gif")
                black_turtle.shape("rua6.gif")
            elif character == 2:
                #xe
                blue_turtle.shape("chim1.gif")
                pink_turtle.shape("chim2.gif")
                yellow_turtle.shape("chim3.gif")
                green_turtle.shape("chim4.gif")
                red_turtle.shape("chim5.gif")
                black_turtle.shape("chim6.gif")
            elif character == 3:
                blue_turtle.shape("cho1.gif")
                pink_turtle.shape("cho2.gif")
                yellow_turtle.shape("cho3.gif")
                green_turtle.shape("cho4.gif")
                red_turtle.shape("cho5.gif")
                black_turtle.shape("cho6.gif")
            elif character == 4:
                blue_turtle.shape("meo1.gif")
                pink_turtle.shape("meo2.gif")
                yellow_turtle.shape("meo3.gif")
                green_turtle.shape("meo4.gif")
                red_turtle.shape("meo5.gif")
                black_turtle.shape("meo6.gif")
            elif character == 5:
                blue_turtle.shape("Car1.gif")
                pink_turtle.shape("Car2.gif")
                yellow_turtle.shape("Car3.gif")
                green_turtle.shape("Car4.gif")
                red_turtle.shape("Car5.gif")
                black_turtle.shape("Car6.gif")

            blue_turtle.shapesize(1.5)
            pink_turtle.shapesize(1.5)
            yellow_turtle.shapesize(1.5)
            green_turtle.shapesize(1.5)
            red_turtle.shapesize(1.5)
            black_turtle.shapesize(1.5)

            # KHONG VE~ TREN DUONG DI
            blue_turtle.penup()
            pink_turtle.penup()
            yellow_turtle.penup()
            green_turtle.penup()
            red_turtle.penup()
            black_turtle.penup()
            # Set toa do rua`
            blue_turtle_x = -450
            blue_turtle_y = 140
            pink_turtle_x = -450
            pink_turtle_y = 90
            yellow_turtle_x = -450
            yellow_turtle_y = 30
            green_turtle_x = -450
            green_turtle_y = -30
            red_turtle_x = -450
            red_turtle_y = -90
            black_turtle_x = -450
            black_turtle_y = -150

            # DUA RUA` DEN CAC VI TRI
            blue_turtle.speed(2)
            pink_turtle.speed(2)
            yellow_turtle.speed(2)
            green_turtle.speed(1)
            red_turtle.speed(1)
            black_turtle.speed(1)
            blue_turtle.goto(blue_turtle_x, blue_turtle_y)
            pink_turtle.goto(pink_turtle_x, pink_turtle_y)
            yellow_turtle.goto(yellow_turtle_x, yellow_turtle_y)
            green_turtle.goto(green_turtle_x, green_turtle_y)
            red_turtle.goto(red_turtle_x, red_turtle_y)   
            black_turtle.goto(black_turtle_x, black_turtle_y)

        #PAUSE FOR 1 SECOND BEFORE RACING
            time.sleep(1)
            blue_turtle.speed(0)
            pink_turtle.speed(0)
            yellow_turtle.speed(0)
            green_turtle.speed(0)
            red_turtle.speed(0)
            black_turtle.speed(0)
        #MOVE THE  TURTLE
            # nho doi lai turn = randint (1,6)
            # STOP SCREEN UNTIL CHOICE IS SUBMITTED
            global choice   # choice o ham ca cuoc
            global wager    # wager o tren ham ca cuoc
            global bank     # bank duoc dung` de so sanh o cacuoc()
            global temp
            global temp_wager # luu lai muc cuoc
            temp = bank
            temp_wager = wager
            if choice != 0 and wager != 0:
                turn = randint(1,6)
                stop = randint(1,6)
                global start_time
                start_time = time.time()
                while blue_turtle.xcor() <= 270 and pink_turtle.xcor() <= 270 and yellow_turtle.xcor() <= 270 and green_turtle.xcor() <= 270 and red_turtle.xcor() <= 270 and black_turtle.xcor() <= 270 :
                    blue_turtle.forward(randint(1, 18))
                    pink_turtle.forward(randint(1, 18))
                    yellow_turtle.forward(randint(1, 18))
                    green_turtle.forward(randint(1, 18))
                    red_turtle.forward(randint(1, 18))
                    black_turtle.forward(randint(1, 18))
                    first_elapsed_time = '%.5s'%(time.time() - start_time)
                    #print (first_elapsed_time)
                    # GHEP NHAC NHANH
                    if blue_turtle.xcor() > -200:
                        winsound.PlaySound("duanhanh.wav", winsound.SND_ASYNC)
                    # QUAY DAU (On~)
                    if blue_turtle.xcor() >= -20 and pink_turtle.xcor() >= -20 and yellow_turtle.xcor() >= -20 and green_turtle.xcor() >= -20 and red_turtle.xcor() >=-20 and black_turtle.xcor() >= -20 :
                        if turn != 0:
                            #for i in range (2):
                                if turn == 1:
                                    if character == 1:
                                        blue_turtle.shape("rua1r.gif")
                                    elif character == 2:
                                        blue_turtle.shape("chim1r.gif")
                                    elif character == 3:
                                        blue_turtle.shape("cho1r.gif")
                                    elif character == 4:
                                        blue_turtle.shape("meo1r.gif")
                                    elif character == 5:
                                        blue_turtle.shape("Car1r.gif")
                                    for i in range (8):
                                        blue_turtle.backward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        blue_turtle.shape("rua1.gif")
                                    elif character == 2:
                                        blue_turtle.shape("chim1.gif")
                                    elif character == 3:
                                        blue_turtle.shape("cho1.gif")
                                    elif character == 4:
                                        blue_turtle.shape("meo1.gif")
                                    elif character == 5:
                                        blue_turtle.shape("Car1.gif")
                                elif turn == 2:
                                    if character == 1:
                                        pink_turtle.shape("rua2r.gif")
                                    elif character == 2:
                                        pink_turtle.shape("chim2r.gif")
                                    elif character == 3:
                                        pink_turtle.shape("cho2r.gif")
                                    elif character == 4:
                                        pink_turtle.shape("meo2r.gif")
                                    elif character == 5:
                                        pink_turtle.shape("Car2r.gif")
                                    for i in range (8):
                                        pink_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        pink_turtle.shape("rua2.gif")
                                    elif character == 2:
                                        pink_turtle.shape("chim2.gif")
                                    elif character == 3:
                                        pink_turtle.shape("cho2.gif")
                                    elif character == 4:
                                        pink_turtle.shape("meo2.gif")
                                    elif character == 5:
                                        pink_turtle.shape("Car2.gif")
                                elif turn == 3:
                                    if character == 1:
                                        yellow_turtle.shape("rua3r.gif")
                                    elif character == 2:
                                        yellow_turtle.shape("chim3r.gif")
                                    elif character == 3:
                                        yellow_turtle.shape("cho3r.gif")
                                    elif character == 4:
                                        yellow_turtle.shape("meo3r.gif")
                                    elif character == 5:
                                        yellow_turtle.shape("Car3r.gif")
                                    for i in range (8):
                                        yellow_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        yellow_turtle.shape("rua3.gif")
                                    elif character == 2:
                                        yellow_turtle.shape("chim3.gif")
                                    elif character == 3:
                                        yellow_turtle.shape("cho3.gif")
                                    elif character == 4:
                                        yellow_turtle.shape("meo3.gif")
                                    elif character == 5:
                                        yellow_turtle.shape("Car3.gif")
                                elif turn == 4:
                                    if character == 1:
                                        green_turtle.shape("rua4r.gif")
                                    elif character == 2:
                                        green_turtle.shape("chim4r.gif")
                                    elif character == 3:
                                        green_turtle.shape("cho4r.gif")
                                    elif character == 4:
                                        green_turtle.shape("meo4r.gif")
                                    elif character == 5:
                                        green_turtle.shape("Car4r.gif")
                                    for i in range (8):
                                        green_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        green_turtle.shape("rua4.gif")
                                    elif character == 2:
                                        green_turtle.shape("chim4.gif")
                                    elif character == 3:
                                        green_turtle.shape("cho4.gif")
                                    elif character == 4:
                                        green_turtle.shape("meo4.gif")
                                    elif character == 5:
                                        green_turtle.shape("Car4.gif")
                                elif turn == 5:
                                    if character == 1:
                                        red_turtle.shape("rua5r.gif")
                                    elif character == 2:
                                        red_turtle.shape("chim5r.gif")
                                    elif character == 3:
                                        red_turtle.shape("cho5r.gif")
                                    elif character == 4:
                                        red_turtle.shape("meo5r.gif")
                                    elif character == 5:
                                        red_turtle.shape("Car5r.gif")
                                    for i in range (8):
                                        red_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        red_turtle.shape("rua5.gif")
                                    elif character == 2:
                                        red_turtle.shape("chim5.gif")
                                    elif character == 3:
                                        red_turtle.shape("cho5.gif")
                                    elif character == 4:
                                        red_turtle.shape("meo5.gif")
                                    elif character == 5:
                                        red_turtle.shape("Car5.gif")
                                elif turn == 6:
                                    if character == 1:
                                        black_turtle.shape("rua6r.gif")
                                    elif character == 2:
                                        black_turtle.shape("chim6r.gif")
                                    elif character == 3:
                                        black_turtle.shape("cho6r.gif")
                                    elif character == 4:
                                        black_turtle.shape("meo6r.gif")
                                    elif character == 5:
                                        black_turtle.shape("Car6r.gif")
                                    for i in range (8):
                                        black_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                    if character == 1:
                                        black_turtle.shape("rua6.gif")
                                    elif character == 2:
                                        black_turtle.shape("chim6.gif")
                                    elif character == 3:
                                        black_turtle.shape("cho6.gif")
                                    elif character == 4:
                                        black_turtle.shape("meo6.gif")
                                    elif character == 5:
                                        black_turtle.shape("Car6.gif") 
                                turn = 0
                    # STOPP        
                    if blue_turtle.xcor() >= -300: 
                        if stop != 0:
                            #blue stop
                            if stop == 1:
                                for i in range (20):
                                    #blue ko chay
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 2:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    #pink khong chay
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 3:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    # yellow stop
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 4:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    #green stop
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 5:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    #red stop
                                    black_turtle.forward(randint(1, 10))
                            if stop == 6:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    #black stop
                            stop = 0
                        
            #CELEBRATE THE WINNER + TIME
                #BLUE WIN
                if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > black_turtle.xcor():
                    #global choice # khong can dung nua tai o tren co dung` rui`
                    # bank setup
                    if choice == 1:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            blue_turtle.shape("rua6.gif")
                            blue_turtle.shape("rua2.gif")
                            blue_turtle.shape("rua3.gif")
                            blue_turtle.shape("rua4.gif")
                            blue_turtle.shape("rua5.gif")
                            blue_turtle.shape("rua1.gif")
                        if character == 2:
                            blue_turtle.shape("chim6.gif")
                            blue_turtle.shape("chim2.gif")
                            blue_turtle.shape("chim3.gif")
                            blue_turtle.shape("chim4.gif")
                            blue_turtle.shape("chim5.gif")
                            blue_turtle.shape("chim1.gif")
                        if character == 3:
                            blue_turtle.shape("cho6.gif")
                            blue_turtle.shape("cho2.gif")
                            blue_turtle.shape("cho3.gif")
                            blue_turtle.shape("cho4.gif")
                            blue_turtle.shape("cho5.gif")
                            blue_turtle.shape("cho1.gif")
                        if character == 4:
                            blue_turtle.shape("meo6.gif")
                            blue_turtle.shape("meo2.gif")
                            blue_turtle.shape("meo3.gif")
                            blue_turtle.shape("meo4.gif")
                            blue_turtle.shape("meo5.gif")
                            blue_turtle.shape("meo1.gif")
                        if character == 5:
                            blue_turtle.shape("Car6.gif")
                            blue_turtle.shape("Car2.gif")
                            blue_turtle.shape("Car3.gif")
                            blue_turtle.shape("Car4.gif")
                            blue_turtle.shape("Car5.gif")
                            blue_turtle.shape("Car1.gif")

                    print_turtle.goto(blue_turtle_x + 705 + 60, blue_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    # may con con` lai chay tiep.
                    while pink_turtle.xcor() <= 270 or yellow_turtle.xcor() <= 270 or green_turtle.xcor() <= 270 or red_turtle.xcor() <= 270 or black_turtle.xcor() <= 270:
                        if pink_turtle.xcor() <= 270:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 270:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 270:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))  
                        if red_turtle.xcor() <= 270:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 270:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    #  IN RA DUONG DUA O DAY.
                    print_turtle.goto(pink_turtle_x + 705 + 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705 + 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705 + 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705 + 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705 + 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))   

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold")) 
                #PINK WIN
                elif  pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor() and pink_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 2:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            pink_turtle.shape("rua6.gif")
                            pink_turtle.shape("rua2.gif")
                            pink_turtle.shape("rua3.gif")
                            pink_turtle.shape("rua4.gif")
                            pink_turtle.shape("rua5.gif")
                            pink_turtle.shape("rua2.gif")
                        if character == 2:
                            pink_turtle.shape("chim6.gif")
                            pink_turtle.shape("chim1.gif")
                            pink_turtle.shape("chim3.gif")
                            pink_turtle.shape("chim4.gif")
                            pink_turtle.shape("chim5.gif")
                            pink_turtle.shape("chim2.gif")
                        if character == 3:
                            pink_turtle.shape("cho6.gif")
                            pink_turtle.shape("cho1.gif")
                            pink_turtle.shape("cho3.gif")
                            pink_turtle.shape("cho4.gif")
                            pink_turtle.shape("cho5.gif")
                            pink_turtle.shape("cho2.gif")
                        if character == 4:
                            pink_turtle.shape("meo6.gif")
                            pink_turtle.shape("meo1.gif")
                            pink_turtle.shape("meo3.gif")
                            pink_turtle.shape("meo4.gif")
                            pink_turtle.shape("meo5.gif")
                            pink_turtle.shape("meo2.gif")
                        if character == 5:
                            pink_turtle.shape("Car6.gif")
                            pink_turtle.shape("Car1.gif")
                            pink_turtle.shape("Car3.gif")
                            pink_turtle.shape("Car4.gif")
                            pink_turtle.shape("Car5.gif")
                            pink_turtle.shape("Car2.gif")
                    print_turtle.goto(pink_turtle_x + 705 + 60, pink_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 270 or yellow_turtle.xcor() <= 270 or green_turtle.xcor() <= 270 or red_turtle.xcor() <= 270 or black_turtle.xcor() <= 270:
                        if blue_turtle.xcor() <= 270:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 270:   
                        
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 270:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))
                        if red_turtle.xcor() <= 270:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 270:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### Print time
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))  

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: blue_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write("1st" , font=("Arial", 20, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold")) 
                #YELLOW WIN
                elif  yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 3:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            yellow_turtle.shape("rua6.gif")
                            yellow_turtle.shape("rua2.gif")
                            yellow_turtle.shape("rua1.gif")
                            yellow_turtle.shape("rua4.gif")
                            yellow_turtle.shape("rua5.gif")
                            yellow_turtle.shape("rua3.gif")
                        if character == 2:
                            yellow_turtle.shape("chim6.gif")
                            yellow_turtle.shape("chim2.gif")
                            yellow_turtle.shape("chim1.gif")
                            yellow_turtle.shape("chim4.gif")
                            yellow_turtle.shape("chim5.gif")
                            yellow_turtle.shape("chim3.gif")
                        if character == 3:
                            yellow_turtle.shape("cho6.gif")
                            yellow_turtle.shape("cho2.gif")
                            yellow_turtle.shape("cho1.gif")
                            yellow_turtle.shape("cho4.gif")
                            yellow_turtle.shape("cho5.gif")
                            yellow_turtle.shape("cho3.gif")
                        if character == 4:
                            yellow_turtle.shape("meo6.gif")
                            yellow_turtle.shape("meo2.gif")
                            yellow_turtle.shape("meo1.gif")
                            yellow_turtle.shape("meo4.gif")
                            yellow_turtle.shape("meo5.gif")
                            yellow_turtle.shape("meo3.gif")
                        if character == 5:
                            yellow_turtle.shape("Car6.gif")
                            yellow_turtle.shape("Car2.gif")
                            yellow_turtle.shape("Car1.gif")
                            yellow_turtle.shape("Car4.gif")
                            yellow_turtle.shape("Car5.gif")
                            yellow_turtle.shape("Car3.gif")
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 270 or pink_turtle.xcor() <= 270 or green_turtle.xcor() <= 270 or red_turtle.xcor() <= 270 or black_turtle.xcor() <= 270:
                        if pink_turtle.xcor() <= 270:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 270:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 270:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 270:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 270:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))

                    ### print time
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold")) 

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: blue_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #GREEN WIN
                elif green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > blue_turtle.xcor() and green_turtle.xcor() > yellow_turtle.xcor() and green_turtle.xcor() > red_turtle.xcor() and green_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 4:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            green_turtle.shape("rua6.gif")
                            green_turtle.shape("rua2.gif")
                            green_turtle.shape("rua1.gif")
                            green_turtle.shape("rua3.gif")
                            green_turtle.shape("rua5.gif")
                            green_turtle.shape("rua4.gif")
                        if character == 2:
                            green_turtle.shape("chim6.gif")
                            green_turtle.shape("chim2.gif")
                            green_turtle.shape("chim1.gif")
                            green_turtle.shape("chim3.gif")
                            green_turtle.shape("chim5.gif")
                            green_turtle.shape("chim4.gif")
                        if character == 3:
                            green_turtle.shape("cho6.gif")
                            green_turtle.shape("cho2.gif")
                            green_turtle.shape("cho1.gif")
                            green_turtle.shape("cho3.gif")
                            green_turtle.shape("cho5.gif")
                            green_turtle.shape("cho4.gif")
                        if character == 4:
                            green_turtle.shape("meo6.gif")
                            green_turtle.shape("meo2.gif")
                            green_turtle.shape("meo1.gif")
                            green_turtle.shape("meo3.gif")
                            green_turtle.shape("meo5.gif")
                            green_turtle.shape("meo4.gif")
                        if character == 5:
                            green_turtle.shape("Car6.gif")
                            green_turtle.shape("Car2.gif")
                            green_turtle.shape("Car1.gif")
                            green_turtle.shape("Car3.gif")
                            green_turtle.shape("Car5.gif")
                            green_turtle.shape("Car4.gif")
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 270 or pink_turtle.xcor() <= 270 or yellow_turtle.xcor() <= 270 or red_turtle.xcor() <= 270 or black_turtle.xcor() <= 270:
                        if pink_turtle.xcor() <= 270:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 270:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 270:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 270:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 270:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### time
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: blue_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #RED WIN
                elif red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > green_turtle.xcor() and red_turtle.xcor() > yellow_turtle.xcor() and red_turtle.xcor() > black_turtle.xcor() :
                    # bank setup
                    if choice == 5:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            red_turtle.shape("rua6.gif")
                            red_turtle.shape("rua2.gif")
                            red_turtle.shape("rua1.gif")
                            red_turtle.shape("rua4.gif")
                            red_turtle.shape("rua3.gif")
                            red_turtle.shape("rua5.gif")
                        if character == 2:
                            red_turtle.shape("chim6.gif")
                            red_turtle.shape("chim2.gif")
                            red_turtle.shape("chim1.gif")
                            red_turtle.shape("chim4.gif")
                            red_turtle.shape("chim3.gif")
                            red_turtle.shape("chim5.gif")
                        if character == 3:
                            red_turtle.shape("cho6.gif")
                            red_turtle.shape("cho2.gif")
                            red_turtle.shape("cho1.gif")
                            red_turtle.shape("cho4.gif")
                            red_turtle.shape("cho3.gif")
                            red_turtle.shape("cho5.gif")
                        if character == 4:
                            red_turtle.shape("meo6.gif")
                            red_turtle.shape("meo2.gif")
                            red_turtle.shape("meo1.gif")
                            red_turtle.shape("meo4.gif")
                            red_turtle.shape("meo3.gif")
                            red_turtle.shape("meo5.gif")
                        if character == 5:
                            red_turtle.shape("Car6.gif")
                            red_turtle.shape("Car2.gif")
                            red_turtle.shape("Car1.gif")
                            red_turtle.shape("Car4.gif")
                            red_turtle.shape("Car3.gif")
                            red_turtle.shape("Car5.gif")
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 270 or pink_turtle.xcor() <= 270 or yellow_turtle.xcor() <= 270 or green_turtle.xcor() <= 270 or black_turtle.xcor() <= 270:
                        if pink_turtle.xcor() <= 270:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 270:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 270:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 270:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 270:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### TIME
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: blue_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #BLACK WIN
                else: 
                    # bank setup
                    if choice == 6:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            black_turtle.shape("rua5.gif")
                            black_turtle.shape("rua2.gif")
                            black_turtle.shape("rua1.gif")
                            black_turtle.shape("rua4.gif")
                            black_turtle.shape("rua3.gif")
                            black_turtle.shape("rua6.gif")
                        if character == 2:
                            black_turtle.shape("chim5.gif")
                            black_turtle.shape("chim2.gif")
                            black_turtle.shape("chim1.gif")
                            black_turtle.shape("chim4.gif")
                            black_turtle.shape("chim3.gif")
                            black_turtle.shape("chim6.gif")
                        if character == 3:
                            black_turtle.shape("cho5.gif")
                            black_turtle.shape("cho2.gif")
                            black_turtle.shape("cho1.gif")
                            black_turtle.shape("cho4.gif")
                            black_turtle.shape("cho3.gif")
                            black_turtle.shape("cho6.gif")
                        if character == 4:
                            black_turtle.shape("meo5.gif")
                            black_turtle.shape("meo2.gif")
                            black_turtle.shape("meo1.gif")
                            black_turtle.shape("meo4.gif")
                            black_turtle.shape("meo3.gif")
                            black_turtle.shape("meo6.gif")
                        if character == 5:
                            black_turtle.shape("Car5.gif")
                            black_turtle.shape("Car2.gif")
                            black_turtle.shape("Car1.gif")
                            black_turtle.shape("Car4.gif")
                            black_turtle.shape("Car3.gif")
                            black_turtle.shape("Car6.gif")
                    print_turtle.goto(black_turtle_x + 705+ 60, black_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 270 or pink_turtle.xcor() <= 270 or yellow_turtle.xcor() <= 270 or green_turtle.xcor() <= 270 or red_turtle.xcor() <= 270:
                        if pink_turtle.xcor() <= 270:
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 270:   
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 270:
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 270:         
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 270:         
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                    ### time 
                    print_turtle.goto(pink_turtle_x + 705+ 60, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 60, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 60, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 60, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 60, blue_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))
                    
                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: blue_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                
                if (bank > temp):
                    print_turtle.goto(-300, 0)
                    print_turtle.write("YOU WIN !!!", font=("Arial", 40, "bold"))
                    history[character - 1][0] = temp_wager
                    history[character - 1][1] = "win"
                    history[character - 1][2] = bank

                else:
                    print_turtle.goto(-300, 0)
                    print_turtle.write("YOU LOSE !!!", font=("Arial", 40, "bold"))
                    history[character - 1][0] = temp_wager
                    history[character - 1][1] = "lose"
                    history[character - 1][2] = bank
                # tang bien dem doi nhan vat
                character += 1
                time.sleep(2)
                # LICH SU
                pickle.dump(history, open("history.dat", "wb"))
                #new_history = pickle.load(open("history.dat", "rb"))
                #print("lich su o file ", new_history)
            else:
                turtle.clear()
                time.sleep(1)
    def start_button(x,y):  #dai 100 rong 40
        if x > vitri_x and x < vitri_x + 100 and y > vitri_y and y < vitri_y + 40:
            clear()
            duangan()

    turtle.onscreenclick(start_button, 1)
    turtle.listen()
    turtle.done()
def dua_dai():
    def draw_button(vitri_x, vitri_y, button_color, text_color, text):
        pen = Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x, vitri_y)
        pen.color(button_color)
        # to dam nen
        pen.begin_fill()
        for i in range (2):
            pen.forward(100)
            pen.left(90)
            pen.forward(40)
            pen.left(90)
        pen.end_fill()
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x + 30 , vitri_y + 10)
        pen.color(text_color)
        pen.write(text, font = ("Arial", 16, "bold"))
    def draw_smallbutton(vitri_x, vitri_y, button_color, text_color, text):
        pen = Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x, vitri_y)
        pen.color(button_color)
        # to dam nen
        pen.begin_fill()
        for i in range (2):
            pen.forward(70)
            pen.left(90)
            pen.forward(30)
            pen.left(90)
        pen.end_fill()
        pen.hideturtle()
        pen.penup()
        pen.goto(vitri_x + 20 , vitri_y + 5)
        pen.color(text_color)
        pen.write(text, font = ("Arial", 16, "bold"))
    def cacuoc():
        # key down function
        def click():    #submit BUTTON
            global bank
            global choice
            global wager
            char_text = int(char_textentry.get())
            money_text = int(money_textentry.get()) 
            if char_text <= 6 and char_text > 0 and money_text <= bank:
                choice = char_text # collect character (nhan vat)
                wager = money_text # collect text (tien cuoc)
                Label(window, text = "submitted !!!         .       ", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                draw_smallbutton(vitri_x + 110, vitri_y, "red", "white", choice)
                draw_smallbutton(vitri_x + 190, vitri_y, "yellow", "black", wager)
                window.destroy()
                exit()
            else:
                if char_text > 6 or char_text <= 0:
                    Label(window, text = "invalid choice !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter choice again !", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)
                else:
                    Label(window, text = "not enough money !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 7, column = 0, sticky = W)
                    Label(window, text = "enter wager again !!!", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 8, column = 0, sticky = W)              
        ## main
        window = Tk()
        window.title("Gambling")
        window.geometry("200x180")
        window.configure(background = "white")
        #window.resizable(0,0)
        # photo
        #photo1 = PhotoImage(file = 'cho1.gif')
        #Label (window, image = photo1, bg = "white") .grid(row = 0, column = 0, sticky = E)
        # create label
        Label(window, text = "Enter character(1 - 6)", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 1, column = 0, sticky = W) 
        Label(window, text = "Enter wager", bg= "white", fg = "black", font = "none 12 bold"). grid(row = 3, column = 0, sticky = W)

        #   create a text entry box
        char_textentry = Entry(window, width = 25)
        char_textentry.grid(row = 2, column = 0, sticky = W)
        money_textentry = Entry(window, width = 25)
        money_textentry.grid(row = 4, column = 0, sticky = W)
        # add a submit button
        Button(window, text = "Submit", width = 6, command = click) .grid(row = 6, column = 0, sticky = W)
        # run the main loop
        #window.mainloop()

        #SCREEN SETUP
    ### GIAO DIEN CHO 
    draw_button(vitri_x, vitri_y, button_color, text_color, text)
    draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
    setup(1050, 650)
    title("Turtle Race")
    bgcolor("white")
    bgpic("dua6.gif")
    speed(0)
    ### LANE SETUP
    # HEADING
    penup()
    goto(-150, 205)
    color("red")
    write("TURTLE RACE", font=("Arial", 40, "bold"))
    #DIRT (DON LAI DUONG DUA)
    goto(-525, 200)
    pendown()
    color("orange")
    begin_fill()
    for i in range(2):
        forward(1050)
        ## 350 la` end cua duong dua
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
        goto(470, (170 - (i * gap_size * 2)))
        stamp()
    # WHITE SQUARES ROW 2
    for i in range(10):
        goto(470 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        stamp()
    # BLACK SQUARES ROW 1
    color("black")
    for i in range(10):
        goto(470, (190 - (i * gap_size * 2)))
        stamp()
    # BLACK SQUARES ROW 2
    for i in range(10):
        goto(471 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        stamp()
    winsound.PlaySound("dua.wav", winsound.SND_ASYNC)
        # HIEN THI CAC NHAN VAT
    # KHAI BAO RUA
    blue_turtle = Turtle()
    pink_turtle = Turtle()
    yellow_turtle = Turtle()
    green_turtle = Turtle()
    red_turtle = Turtle()
    black_turtle = Turtle()

    addshape("rua4.gif")
    addshape("chim3.gif")
    addshape("cho5.gif")
    addshape("meo4.gif")
    addshape("Car5.gif")
    blue_turtle.shape("rua4.gif")
    blue_turtle.penup()
    blue_turtle.goto(-340, 100 -30)

    pink_turtle.shape("chim3.gif")
    pink_turtle.penup()
    pink_turtle.goto(-170, 100 -30)

    yellow_turtle.shape("cho5.gif")
    yellow_turtle.penup()
    yellow_turtle.goto(0, 100 -30)

    green_turtle.shape("meo4.gif")
    green_turtle.penup()
    green_turtle.goto(-150, 0 -30)

    red_turtle.shape("Car5.gif")
    red_turtle.penup()
    red_turtle.goto(-320, 0 -30)



    def duangan():
        # VARIABLE SETUP 
        turtle.clear()
        global first_elapsed_time
        global second_elapsed_time
        global third_elapsed_time
        global fourth_elapsed_time
        global fifth_elapsed_time
        global sixth_elapsed_time
            # THEM VAO HINH ANH CAC NHAN VAT
        if True:

            addshape ("chim1.gif") 
            addshape ("chim1r.gif")
            addshape ("chim2.gif") 
            addshape ("chim2r.gif")
            addshape ("chim3.gif") 
            addshape ("chim3r.gif")
            addshape ("chim4.gif") 
            addshape ("chim4r.gif")
            addshape ("chim5.gif") 
            addshape ("chim5r.gif")
            addshape ("chim6.gif") 
            addshape ("chim6r.gif")
                # rua
            addshape ("rua1.gif") 
            addshape ("rua1r.gif")
            addshape ("rua2.gif") 
            addshape ("rua2r.gif")
            addshape ("rua3.gif") 
            addshape ("rua3r.gif")
            addshape ("rua4.gif") 
            addshape ("rua4r.gif")
            addshape ("rua5.gif") 
            addshape ("rua5r.gif")
            addshape ("rua6.gif") 
            addshape ("rua6r.gif")

                # cho
            addshape ("cho1.gif") 
            addshape ("cho1r.gif")
            addshape ("cho2.gif") 
            addshape ("cho2r.gif")
            addshape ("cho3.gif") 
            addshape ("cho3r.gif")
            addshape ("cho4.gif") 
            addshape ("cho4r.gif")
            addshape ("cho5.gif") 
            addshape ("cho5r.gif")
            addshape ("cho6.gif") 
            addshape ("cho6r.gif")
                # MEO
            addshape ("meo1.gif") 
            addshape ("meo1r.gif")
            addshape ("meo2.gif") 
            addshape ("meo2r.gif")
            addshape ("meo3.gif") 
            addshape ("meo3r.gif")
            addshape ("meo4.gif") 
            addshape ("meo4r.gif")
            addshape ("meo5.gif") 
            addshape ("meo5r.gif")
            addshape ("meo6.gif") 
            addshape ("meo6r.gif")
            # XE
            addshape ("Car1.gif") 
            addshape ("Car1r.gif")
            addshape ("Car2.gif") 
            addshape ("Car2r.gif")
            addshape ("Car3.gif") 
            addshape ("Car3r.gif")
            addshape ("Car4.gif") 
            addshape ("Car4r.gif")
            addshape ("Car5.gif") 
            addshape ("Car5r.gif")
            addshape ("Car6.gif") 
            addshape ("Car6r.gif")  
        #bgpic('background.gif')
        # SCREEN SETUP
        # setup(1050, 650)
        # title("Turtle Race")
        # bgcolor("white")
        # speed(0)
        character = 1
        while True:
            winsound.PlaySound("dua.wav", winsound.SND_ASYNC)
            # SET LAI TIEN CUOC
            cacuoc()
            # xong 1 nv se doi nhan vat khac (rua = 1 -> cho = ?)
            if character > 5:
                character = 1
            
            # HEADING
            penup()
            goto(-150, 205)
            color("red")
            write("TURTLE RACE", font=("Arial", 40, "bold"))
            #DIRT (DON LAI DUONG DUA)
            goto(-525, 200)
            pendown()
            color("orange")
            begin_fill()
            for i in range(2):
                forward(1050)
                ## 350 la` end cua duong dua
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
                goto(470, (170 - (i * gap_size * 2)))
                stamp()

            # WHITE SQUARES ROW 2
            for i in range(10):
                goto(470 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
                stamp()

            # BLACK SQUARES ROW 1
            color("black")
            for i in range(10):
                goto(470, (190 - (i * gap_size * 2)))
                stamp()

            # BLACK SQUARES ROW 2
            for i in range(10):
                goto(471 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
                stamp()
            # KHAI BAO RUA
            blue_turtle = Turtle()
            pink_turtle = Turtle()
            yellow_turtle = Turtle()
            green_turtle = Turtle()
            red_turtle = Turtle()
            black_turtle = Turtle()

            #Khai Bao Con Tro Print
            print_turtle = Turtle()
            print_turtle.penup()
            print_turtle.hideturtle()

            
                #DOI NHAN VAT (chua chen nhan vat) + SETUP NHAN VAT
            if character == 1:
                # chim
                blue_turtle.shape("rua1.gif")
                pink_turtle.shape("rua2.gif")
                yellow_turtle.shape("rua3.gif")
                green_turtle.shape("rua4.gif")
                red_turtle.shape("rua5.gif")
                black_turtle.shape("rua6.gif")
            elif character == 2:
                #xe
                blue_turtle.shape("chim1.gif")
                pink_turtle.shape("chim2.gif")
                yellow_turtle.shape("chim3.gif")
                green_turtle.shape("chim4.gif")
                red_turtle.shape("chim5.gif")
                black_turtle.shape("chim6.gif")
            elif character == 3:
                blue_turtle.shape("cho1.gif")
                pink_turtle.shape("cho2.gif")
                yellow_turtle.shape("cho3.gif")
                green_turtle.shape("cho4.gif")
                red_turtle.shape("cho5.gif")
                black_turtle.shape("cho6.gif")
            elif character == 4:
                blue_turtle.shape("meo1.gif")
                pink_turtle.shape("meo2.gif")
                yellow_turtle.shape("meo3.gif")
                green_turtle.shape("meo4.gif")
                red_turtle.shape("meo5.gif")
                black_turtle.shape("meo6.gif")
            elif character == 5:
                blue_turtle.shape("Car1.gif")
                pink_turtle.shape("Car2.gif")
                yellow_turtle.shape("Car3.gif")
                green_turtle.shape("Car4.gif")
                red_turtle.shape("Car5.gif")
                black_turtle.shape("Car6.gif")

            blue_turtle.shapesize(1.5)
            pink_turtle.shapesize(1.5)
            yellow_turtle.shapesize(1.5)
            green_turtle.shapesize(1.5)
            red_turtle.shapesize(1.5)
            black_turtle.shapesize(1.5)

            # KHONG VE~ TREN DUONG DI
            blue_turtle.penup()
            pink_turtle.penup()
            yellow_turtle.penup()
            green_turtle.penup()
            red_turtle.penup()
            black_turtle.penup()
            # Set toa do rua`
            blue_turtle_x = -450
            blue_turtle_y = 140
            pink_turtle_x = -450
            pink_turtle_y = 90
            yellow_turtle_x = -450
            yellow_turtle_y = 30
            green_turtle_x = -450
            green_turtle_y = -30
            red_turtle_x = -450
            red_turtle_y = -90
            black_turtle_x = -450
            black_turtle_y = -150

            # DUA RUA` DEN CAC VI TRI
            blue_turtle.speed(2)
            pink_turtle.speed(2)
            yellow_turtle.speed(2)
            green_turtle.speed(1)
            red_turtle.speed(1)
            black_turtle.speed(1)
            blue_turtle.goto(blue_turtle_x, blue_turtle_y)
            pink_turtle.goto(pink_turtle_x, pink_turtle_y)
            yellow_turtle.goto(yellow_turtle_x, yellow_turtle_y)
            green_turtle.goto(green_turtle_x, green_turtle_y)
            red_turtle.goto(red_turtle_x, red_turtle_y)   
            black_turtle.goto(black_turtle_x, black_turtle_y)

        #PAUSE FOR 1 SECOND BEFORE RACING
            time.sleep(1)
            blue_turtle.speed(0)
            pink_turtle.speed(0)
            yellow_turtle.speed(0)
            green_turtle.speed(0)
            red_turtle.speed(0)
            black_turtle.speed(0)
        #MOVE THE  TURTLE
            # nho doi lai turn = randint (1,6)
            # STOP SCREEN UNTIL CHOICE IS SUBMITTED
            global choice   # choice o ham ca cuoc
            global wager    # wager o tren ham ca cuoc
            global bank     # bank duoc dung` de so sanh o cacuoc()
            global temp
            global temp_wager # luu lai muc cuoc
            temp = bank
            temp_wager = wager
            if choice != 0 and wager != 0:
                turn = randint(1,6)
                stop = randint(1,6)
                global start_time
                start_time = time.time()
                while blue_turtle.xcor() <= 470 and pink_turtle.xcor() <= 470 and yellow_turtle.xcor() <= 470 and green_turtle.xcor() <= 470 and red_turtle.xcor() <= 470 and black_turtle.xcor() <= 470 :
                    blue_turtle.forward(randint(1, 18))
                    pink_turtle.forward(randint(1, 18))
                    yellow_turtle.forward(randint(1, 18))
                    green_turtle.forward(randint(1, 18))
                    red_turtle.forward(randint(1, 18))
                    black_turtle.forward(randint(1, 18))
                    first_elapsed_time = '%.5s'%(time.time() - start_time)
                    #print (first_elapsed_time)
                    # GHEP NHAC NHANH
                    if blue_turtle.xcor() > -150:
                        winsound.PlaySound("duanhanh.wav", winsound.SND_ASYNC)
                    # QUAY DAU (On~)
                    if blue_turtle.xcor() >= -80 and pink_turtle.xcor() >= -80 and yellow_turtle.xcor() >= -80 and green_turtle.xcor() >= -80 and red_turtle.xcor() >=-80 and black_turtle.xcor() >= -80 :
                        if turn != 0:
                            #for i in range (2):
                                if turn == 1:
                                    if character == 1:
                                        blue_turtle.shape("rua1r.gif")
                                    elif character == 2:
                                        blue_turtle.shape("chim1r.gif")
                                    elif character == 3:
                                        blue_turtle.shape("cho1r.gif")
                                    elif character == 4:
                                        blue_turtle.shape("meo1r.gif")
                                    elif character == 5:
                                        blue_turtle.shape("Car1r.gif")
                                    for i in range (8):
                                        blue_turtle.backward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        blue_turtle.shape("rua1.gif")
                                    elif character == 2:
                                        blue_turtle.shape("chim1.gif")
                                    elif character == 3:
                                        blue_turtle.shape("cho1.gif")
                                    elif character == 4:
                                        blue_turtle.shape("meo1.gif")
                                    elif character == 5:
                                        blue_turtle.shape("Car1.gif")
                                elif turn == 2:
                                    if character == 1:
                                        pink_turtle.shape("rua2r.gif")
                                    elif character == 2:
                                        pink_turtle.shape("chim2r.gif")
                                    elif character == 3:
                                        pink_turtle.shape("cho2r.gif")
                                    elif character == 4:
                                        pink_turtle.shape("meo2r.gif")
                                    elif character == 5:
                                        pink_turtle.shape("Car2r.gif")
                                    for i in range (8):
                                        pink_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        pink_turtle.shape("rua2.gif")
                                    elif character == 2:
                                        pink_turtle.shape("chim2.gif")
                                    elif character == 3:
                                        pink_turtle.shape("cho2.gif")
                                    elif character == 4:
                                        pink_turtle.shape("meo2.gif")
                                    elif character == 5:
                                        pink_turtle.shape("Car2.gif")
                                elif turn == 3:
                                    if character == 1:
                                        yellow_turtle.shape("rua3r.gif")
                                    elif character == 2:
                                        yellow_turtle.shape("chim3r.gif")
                                    elif character == 3:
                                        yellow_turtle.shape("cho3r.gif")
                                    elif character == 4:
                                        yellow_turtle.shape("meo3r.gif")
                                    elif character == 5:
                                        yellow_turtle.shape("Car3r.gif")
                                    for i in range (8):
                                        yellow_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        yellow_turtle.shape("rua3.gif")
                                    elif character == 2:
                                        yellow_turtle.shape("chim3.gif")
                                    elif character == 3:
                                        yellow_turtle.shape("cho3.gif")
                                    elif character == 4:
                                        yellow_turtle.shape("meo3.gif")
                                    elif character == 5:
                                        yellow_turtle.shape("Car3.gif")
                                elif turn == 4:
                                    if character == 1:
                                        green_turtle.shape("rua4r.gif")
                                    elif character == 2:
                                        green_turtle.shape("chim4r.gif")
                                    elif character == 3:
                                        green_turtle.shape("cho4r.gif")
                                    elif character == 4:
                                        green_turtle.shape("meo4r.gif")
                                    elif character == 5:
                                        green_turtle.shape("Car4r.gif")
                                    for i in range (8):
                                        green_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        green_turtle.shape("rua4.gif")
                                    elif character == 2:
                                        green_turtle.shape("chim4.gif")
                                    elif character == 3:
                                        green_turtle.shape("cho4.gif")
                                    elif character == 4:
                                        green_turtle.shape("meo4.gif")
                                    elif character == 5:
                                        green_turtle.shape("Car4.gif")
                                elif turn == 5:
                                    if character == 1:
                                        red_turtle.shape("rua5r.gif")
                                    elif character == 2:
                                        red_turtle.shape("chim5r.gif")
                                    elif character == 3:
                                        red_turtle.shape("cho5r.gif")
                                    elif character == 4:
                                        red_turtle.shape("meo5r.gif")
                                    elif character == 5:
                                        red_turtle.shape("Car5r.gif")
                                    for i in range (8):
                                        red_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        black_turtle.forward(randint(1,10))
                                    if character == 1:
                                        red_turtle.shape("rua5.gif")
                                    elif character == 2:
                                        red_turtle.shape("chim5.gif")
                                    elif character == 3:
                                        red_turtle.shape("cho5.gif")
                                    elif character == 4:
                                        red_turtle.shape("meo5.gif")
                                    elif character == 5:
                                        red_turtle.shape("Car5.gif")
                                elif turn == 6:
                                    if character == 1:
                                        black_turtle.shape("rua6r.gif")
                                    elif character == 2:
                                        black_turtle.shape("chim6r.gif")
                                    elif character == 3:
                                        black_turtle.shape("cho6r.gif")
                                    elif character == 4:
                                        black_turtle.shape("meo6r.gif")
                                    elif character == 5:
                                        black_turtle.shape("Car6r.gif")
                                    for i in range (8):
                                        black_turtle.backward(randint(1,10))
                                        blue_turtle.forward(randint(1,10))
                                        pink_turtle.forward(randint(1,10))
                                        yellow_turtle.forward(randint(1,10))
                                        green_turtle.forward(randint(1,10))
                                        red_turtle.forward(randint(1,10))
                                    if character == 1:
                                        black_turtle.shape("rua6.gif")
                                    elif character == 2:
                                        black_turtle.shape("chim6.gif")
                                    elif character == 3:
                                        black_turtle.shape("cho6.gif")
                                    elif character == 4:
                                        black_turtle.shape("meo6.gif")
                                    elif character == 5:
                                        black_turtle.shape("Car6.gif") 
                                turn = 0
                    # STOPP        
                    if blue_turtle.xcor() >= -250: 
                        if stop != 0:
                            #blue stop
                            if stop == 1:
                                for i in range (20):
                                    #blue ko chay
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 2:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    #pink khong chay
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 3:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    # yellow stop
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 4:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    #green stop
                                    red_turtle.forward(randint(1, 10))
                                    black_turtle.forward(randint(1, 10)) 
                            if stop == 5:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    #red stop
                                    black_turtle.forward(randint(1, 10))
                            if stop == 6:
                                for i in range (20):
                                    blue_turtle.forward(randint(1, 10))
                                    pink_turtle.forward(randint(1, 10))
                                    yellow_turtle.forward(randint(1, 10))
                                    green_turtle.forward(randint(1, 10))
                                    red_turtle.forward(randint(1, 10))
                                    #black stop
                            stop = 0
                        
            #CELEBRATE THE WINNER + TIME
                #BLUE WIN
                if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > black_turtle.xcor():
                    #global choice # khong can dung nua tai o tren co dung` rui`
                    # bank setup
                    if choice == 1:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            blue_turtle.shape("rua6.gif")
                            blue_turtle.shape("rua2.gif")
                            blue_turtle.shape("rua3.gif")
                            blue_turtle.shape("rua4.gif")
                            blue_turtle.shape("rua5.gif")
                            blue_turtle.shape("rua1.gif")
                        if character == 2:
                            blue_turtle.shape("chim6.gif")
                            blue_turtle.shape("chim2.gif")
                            blue_turtle.shape("chim3.gif")
                            blue_turtle.shape("chim4.gif")
                            blue_turtle.shape("chim5.gif")
                            blue_turtle.shape("chim1.gif")
                        if character == 3:
                            blue_turtle.shape("cho6.gif")
                            blue_turtle.shape("cho2.gif")
                            blue_turtle.shape("cho3.gif")
                            blue_turtle.shape("cho4.gif")
                            blue_turtle.shape("cho5.gif")
                            blue_turtle.shape("cho1.gif")
                        if character == 4:
                            blue_turtle.shape("meo6.gif")
                            blue_turtle.shape("meo2.gif")
                            blue_turtle.shape("meo3.gif")
                            blue_turtle.shape("meo4.gif")
                            blue_turtle.shape("meo5.gif")
                            blue_turtle.shape("meo1.gif")
                        if character == 5:
                            blue_turtle.shape("Car6.gif")
                            blue_turtle.shape("Car2.gif")
                            blue_turtle.shape("Car3.gif")
                            blue_turtle.shape("Car4.gif")
                            blue_turtle.shape("Car5.gif")
                            blue_turtle.shape("Car1.gif")

                    print_turtle.goto(blue_turtle_x + 705 + 50, blue_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    # may con con` lai chay tiep.
                    while pink_turtle.xcor() <= 470 or yellow_turtle.xcor() <= 470 or green_turtle.xcor() <= 470 or red_turtle.xcor() <= 470 or black_turtle.xcor() <= 470:
                        if pink_turtle.xcor() <= 470:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 470:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 470:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))  
                        if red_turtle.xcor() <= 470:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 470:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    #  IN RA DUONG DUA O DAY.
                    print_turtle.goto(pink_turtle_x + 705 + 50 , pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705 + 50, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705 + 50, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705 + 50, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705 + 50, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))   

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold")) 
                #PINK WIN
                elif  pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > yellow_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor() and pink_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 2:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            pink_turtle.shape("rua6.gif")
                            pink_turtle.shape("rua2.gif")
                            pink_turtle.shape("rua3.gif")
                            pink_turtle.shape("rua4.gif")
                            pink_turtle.shape("rua5.gif")
                            pink_turtle.shape("rua2.gif")
                        if character == 2:
                            pink_turtle.shape("chim6.gif")
                            pink_turtle.shape("chim1.gif")
                            pink_turtle.shape("chim3.gif")
                            pink_turtle.shape("chim4.gif")
                            pink_turtle.shape("chim5.gif")
                            pink_turtle.shape("chim2.gif")
                        if character == 3:
                            pink_turtle.shape("cho6.gif")
                            pink_turtle.shape("cho1.gif")
                            pink_turtle.shape("cho3.gif")
                            pink_turtle.shape("cho4.gif")
                            pink_turtle.shape("cho5.gif")
                            pink_turtle.shape("cho2.gif")
                        if character == 4:
                            pink_turtle.shape("meo6.gif")
                            pink_turtle.shape("meo1.gif")
                            pink_turtle.shape("meo3.gif")
                            pink_turtle.shape("meo4.gif")
                            pink_turtle.shape("meo5.gif")
                            pink_turtle.shape("meo2.gif")
                        if character == 5:
                            pink_turtle.shape("Car6.gif")
                            pink_turtle.shape("Car1.gif")
                            pink_turtle.shape("Car3.gif")
                            pink_turtle.shape("Car4.gif")
                            pink_turtle.shape("Car5.gif")
                            pink_turtle.shape("Car2.gif")
                    print_turtle.goto(pink_turtle_x + 705 + 50, pink_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 470 or yellow_turtle.xcor() <= 470 or green_turtle.xcor() <= 470 or red_turtle.xcor() <= 470 or black_turtle.xcor() <= 470:
                        if blue_turtle.xcor() <= 470:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 470:   
                        
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 470:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))
                        if red_turtle.xcor() <= 470:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 470:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### Print time
                    print_turtle.goto(blue_turtle_x + 705+ 50, blue_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 50, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 50, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 50, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 50, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))  

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: blue_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write("1st" , font=("Arial", 20, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold")) 
                #YELLOW WIN
                elif  yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 3:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            yellow_turtle.shape("rua6.gif")
                            yellow_turtle.shape("rua2.gif")
                            yellow_turtle.shape("rua1.gif")
                            yellow_turtle.shape("rua4.gif")
                            yellow_turtle.shape("rua5.gif")
                            yellow_turtle.shape("rua3.gif")
                        if character == 2:
                            yellow_turtle.shape("chim6.gif")
                            yellow_turtle.shape("chim2.gif")
                            yellow_turtle.shape("chim1.gif")
                            yellow_turtle.shape("chim4.gif")
                            yellow_turtle.shape("chim5.gif")
                            yellow_turtle.shape("chim3.gif")
                        if character == 3:
                            yellow_turtle.shape("cho6.gif")
                            yellow_turtle.shape("cho2.gif")
                            yellow_turtle.shape("cho1.gif")
                            yellow_turtle.shape("cho4.gif")
                            yellow_turtle.shape("cho5.gif")
                            yellow_turtle.shape("cho3.gif")
                        if character == 4:
                            yellow_turtle.shape("meo6.gif")
                            yellow_turtle.shape("meo2.gif")
                            yellow_turtle.shape("meo1.gif")
                            yellow_turtle.shape("meo4.gif")
                            yellow_turtle.shape("meo5.gif")
                            yellow_turtle.shape("meo3.gif")
                        if character == 5:
                            yellow_turtle.shape("Car6.gif")
                            yellow_turtle.shape("Car2.gif")
                            yellow_turtle.shape("Car1.gif")
                            yellow_turtle.shape("Car4.gif")
                            yellow_turtle.shape("Car5.gif")
                            yellow_turtle.shape("Car3.gif")
                    print_turtle.goto(yellow_turtle_x + 705+ 50, yellow_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 470 or pink_turtle.xcor() <= 470 or green_turtle.xcor() <= 470 or red_turtle.xcor() <= 470 or black_turtle.xcor() <= 470:
                        if pink_turtle.xcor() <= 470:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 470:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 470:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 470:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 470:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))

                    ### print time
                    print_turtle.goto(pink_turtle_x + 705+ 50, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(blue_turtle_x + 705+ 50, blue_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 50, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 50, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 50, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold")) 

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: blue_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #GREEN WIN
                elif green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > blue_turtle.xcor() and green_turtle.xcor() > yellow_turtle.xcor() and green_turtle.xcor() > red_turtle.xcor() and green_turtle.xcor() > black_turtle.xcor():
                    # bank setup
                    if choice == 4:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            green_turtle.shape("rua6.gif")
                            green_turtle.shape("rua2.gif")
                            green_turtle.shape("rua1.gif")
                            green_turtle.shape("rua3.gif")
                            green_turtle.shape("rua5.gif")
                            green_turtle.shape("rua4.gif")
                        if character == 2:
                            green_turtle.shape("chim6.gif")
                            green_turtle.shape("chim2.gif")
                            green_turtle.shape("chim1.gif")
                            green_turtle.shape("chim3.gif")
                            green_turtle.shape("chim5.gif")
                            green_turtle.shape("chim4.gif")
                        if character == 3:
                            green_turtle.shape("cho6.gif")
                            green_turtle.shape("cho2.gif")
                            green_turtle.shape("cho1.gif")
                            green_turtle.shape("cho3.gif")
                            green_turtle.shape("cho5.gif")
                            green_turtle.shape("cho4.gif")
                        if character == 4:
                            green_turtle.shape("meo6.gif")
                            green_turtle.shape("meo2.gif")
                            green_turtle.shape("meo1.gif")
                            green_turtle.shape("meo3.gif")
                            green_turtle.shape("meo5.gif")
                            green_turtle.shape("meo4.gif")
                        if character == 5:
                            green_turtle.shape("Car6.gif")
                            green_turtle.shape("Car2.gif")
                            green_turtle.shape("Car1.gif")
                            green_turtle.shape("Car3.gif")
                            green_turtle.shape("Car5.gif")
                            green_turtle.shape("Car4.gif")
                    print_turtle.goto(green_turtle_x + 705+ 50, green_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 470 or pink_turtle.xcor() <= 470 or yellow_turtle.xcor() <= 470 or red_turtle.xcor() <= 470 or black_turtle.xcor() <= 470:
                        if pink_turtle.xcor() <= 470:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 470:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 470:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 470:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 470:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### time
                    print_turtle.goto(pink_turtle_x + 705+ 50, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 50, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 50, blue_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 50, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 50, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: blue_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #RED WIN
                elif red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > green_turtle.xcor() and red_turtle.xcor() > yellow_turtle.xcor() and red_turtle.xcor() > black_turtle.xcor() :
                    # bank setup
                    if choice == 5:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            red_turtle.shape("rua6.gif")
                            red_turtle.shape("rua2.gif")
                            red_turtle.shape("rua1.gif")
                            red_turtle.shape("rua4.gif")
                            red_turtle.shape("rua3.gif")
                            red_turtle.shape("rua5.gif")
                        if character == 2:
                            red_turtle.shape("chim6.gif")
                            red_turtle.shape("chim2.gif")
                            red_turtle.shape("chim1.gif")
                            red_turtle.shape("chim4.gif")
                            red_turtle.shape("chim3.gif")
                            red_turtle.shape("chim5.gif")
                        if character == 3:
                            red_turtle.shape("cho6.gif")
                            red_turtle.shape("cho2.gif")
                            red_turtle.shape("cho1.gif")
                            red_turtle.shape("cho4.gif")
                            red_turtle.shape("cho3.gif")
                            red_turtle.shape("cho5.gif")
                        if character == 4:
                            red_turtle.shape("meo6.gif")
                            red_turtle.shape("meo2.gif")
                            red_turtle.shape("meo1.gif")
                            red_turtle.shape("meo4.gif")
                            red_turtle.shape("meo3.gif")
                            red_turtle.shape("meo5.gif")
                        if character == 5:
                            red_turtle.shape("Car6.gif")
                            red_turtle.shape("Car2.gif")
                            red_turtle.shape("Car1.gif")
                            red_turtle.shape("Car4.gif")
                            red_turtle.shape("Car3.gif")
                            red_turtle.shape("Car5.gif")
                    print_turtle.goto(red_turtle_x + 705+ 50, red_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 470 or pink_turtle.xcor() <= 470 or yellow_turtle.xcor() <= 470 or green_turtle.xcor() <= 470 or black_turtle.xcor() <= 470:
                        if pink_turtle.xcor() <= 470:
                            
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 470:   
                            
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 470:
                            
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 470:          
                            
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                        if black_turtle.xcor() <= 470:         
                            
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            black_turtle.forward(randint(1, 10))
                    ### TIME
                    print_turtle.goto(pink_turtle_x + 705+ 50, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 50, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 50, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 50, blue_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(black_turtle_x + 705+ 50, black_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))

                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: blue_position = i 
                        if xephang[i] == sixth_elapsed_time: black_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write(black_position + 2, font=("Arial", 16, "bold"))
                #BLACK WIN
                else: 
                    # bank setup
                    if choice == 6:
                        bank += wager
                        print_turtle.goto(950, 200)
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    else:
                        bank -= wager
                        draw_button(vitri_x + 950, vitri_y, "yellow", "black", bank)
                    choice = 0
                    wager = 0
                    for i in range(20):
                        if character == 1:
                            black_turtle.shape("rua5.gif")
                            black_turtle.shape("rua2.gif")
                            black_turtle.shape("rua1.gif")
                            black_turtle.shape("rua4.gif")
                            black_turtle.shape("rua3.gif")
                            black_turtle.shape("rua6.gif")
                        if character == 2:
                            black_turtle.shape("chim5.gif")
                            black_turtle.shape("chim2.gif")
                            black_turtle.shape("chim1.gif")
                            black_turtle.shape("chim4.gif")
                            black_turtle.shape("chim3.gif")
                            black_turtle.shape("chim6.gif")
                        if character == 3:
                            black_turtle.shape("cho5.gif")
                            black_turtle.shape("cho2.gif")
                            black_turtle.shape("cho1.gif")
                            black_turtle.shape("cho4.gif")
                            black_turtle.shape("cho3.gif")
                            black_turtle.shape("cho6.gif")
                        if character == 4:
                            black_turtle.shape("meo5.gif")
                            black_turtle.shape("meo2.gif")
                            black_turtle.shape("meo1.gif")
                            black_turtle.shape("meo4.gif")
                            black_turtle.shape("meo3.gif")
                            black_turtle.shape("meo6.gif")
                        if character == 5:
                            black_turtle.shape("Car5.gif")
                            black_turtle.shape("Car2.gif")
                            black_turtle.shape("Car1.gif")
                            black_turtle.shape("Car4.gif")
                            black_turtle.shape("Car3.gif")
                            black_turtle.shape("Car6.gif")
                    print_turtle.goto(black_turtle_x + 705+ 50, black_turtle_y)
                    print_turtle.write(first_elapsed_time, font=("Arial", 16, "bold"))
                    while blue_turtle.xcor() <= 470 or pink_turtle.xcor() <= 470 or yellow_turtle.xcor() <= 470 or green_turtle.xcor() <= 470 or red_turtle.xcor() <= 470:
                        if pink_turtle.xcor() <= 470:
                            second_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            pink_turtle.forward(randint(1, 10))
                        if yellow_turtle.xcor() <= 470:   
                            third_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            yellow_turtle.forward(randint(1, 10))
                        if green_turtle.xcor() <= 470:
                            fourth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            green_turtle.forward(randint(1, 10)) 
                        if red_turtle.xcor() <= 470:         
                            fifth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            red_turtle.forward(randint(1, 10))
                        if blue_turtle.xcor() <= 470:         
                            sixth_elapsed_time = '%.5s'%(time.time() - start_time - 3.2)
                            blue_turtle.forward(randint(1, 10))
                    ### time 
                    print_turtle.goto(pink_turtle_x + 705+ 50, pink_turtle_y)
                    print_turtle.write(second_elapsed_time, font=("Arial", 16, "bold"))
                    print_turtle.goto(yellow_turtle_x + 705+ 50, yellow_turtle_y)
                    print_turtle.write(third_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(green_turtle_x + 705+ 50, green_turtle_y)
                    print_turtle.write(fourth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(red_turtle_x + 705+ 50, red_turtle_y)
                    print_turtle.write(fifth_elapsed_time, font=("Arial", 16, "bold")) 
                    print_turtle.goto(blue_turtle_x + 705+ 50, blue_turtle_y)
                    print_turtle.write(sixth_elapsed_time, font=("Arial", 16, "bold"))
                    
                    xephang = [second_elapsed_time, third_elapsed_time, fourth_elapsed_time, fifth_elapsed_time, sixth_elapsed_time]
                    xephang.sort()
                    for i in range (5): 
                        if xephang[i] == second_elapsed_time: pink_position = i
                        if xephang[i] == third_elapsed_time: yellow_position = i 
                        if xephang[i] == fourth_elapsed_time: green_position = i
                        if xephang[i] == fifth_elapsed_time: red_position = i 
                        if xephang[i] == sixth_elapsed_time: blue_position = i
                    print_turtle.color("white")
                    print_turtle.goto(150, blue_turtle_y)
                    print_turtle.write(blue_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, pink_turtle_y)
                    print_turtle.write(pink_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, yellow_turtle_y)
                    print_turtle.write(yellow_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, green_turtle_y)
                    print_turtle.write(green_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, red_turtle_y)
                    print_turtle.write(red_position + 2, font=("Arial", 16, "bold"))
                    print_turtle.goto(150, black_turtle_y)
                    print_turtle.write("1st", font=("Arial", 20, "bold"))
                
                if (bank > temp):
                    print_turtle.goto(-300, 0)
                    print_turtle.write("YOU WIN !!!", font=("Arial", 40, "bold"))
                    history[character - 1][0] = temp_wager
                    history[character - 1][1] = "win"
                    history[character - 1][2] = bank

                else:
                    print_turtle.goto(-300, 0)
                    print_turtle.write("YOU LOSE !!!", font=("Arial", 40, "bold"))
                    history[character - 1][0] = temp_wager
                    history[character - 1][1] = "lose"
                    history[character - 1][2] = bank
                # tang bien dem doi nhan vat
                character += 1
                time.sleep(2)
                # LICH SU
                pickle.dump(history, open("history.dat", "wb"))
                #new_history = pickle.load(open("history.dat", "rb"))
                #print("lich su o file ", new_history)
            else:
                turtle.clear()
                time.sleep(1)
    def start_button(x,y):  #dai 100 rong 40
        if x > vitri_x and x < vitri_x + 100 and y > vitri_y and y < vitri_y + 40:
            clear()
            duangan()

    turtle.onscreenclick(start_button, 1)
    turtle.listen()
    turtle.done()
def race_types():
    #winsound.PlaySound("menu.wav", winsound.SND_ASYNC)
     #content setup
    background = pygame.image.load('racetypes.gif')
    #dua ngan
    button1 = pygame.Rect(160, 450 ,200, 35)
    #dua vua
    button2 = pygame.Rect(160 , 500 , 250 + 20, 35)
    #dua dai
    button3 = pygame.Rect(160 , 550, 300 + 30, 35)
    #return button 
    button4 = pygame.Rect(0, 0, 240 , 35)

    racetypes_running = True
    while racetypes_running:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            # bam nut cheo x se out
            if event.type == pygame.QUIT:
                pass
                #pygame.quit()
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
                    #racetypes_running = False
                    # NOI SOURCE DUA NGAN (pygame.quit() thoat giao dien racetypes)
                    pygame.quit()
                    dua_ngan()
                if button2.collidepoint(event.pos):
                    #racetypes_running = False
                    pygame.quit()
                    dua_vua()
                    #DAT HAM DUONG DUA VUA VAO DONG CMT NAY!
                if button3.collidepoint(event.pos):
                    #racetypes_running = False
                    pygame.quit()
                    dua_dai()
                    #DAT HAM DUONG DUA DAI VAO DONG CMT NAY!

        pygame.draw.rect(screen, "yellow", button1, 4)
        pygame.draw.rect(screen, "yellow", button2, 4)
        pygame.draw.rect(screen, "yellow", button3, 4)
        pygame.draw.rect(screen,"orange", button4, 5)

        draw_text("short", menu_font, "white", screen, button1.x + 15, button1.y + 10)
        draw_text("medium", menu_font, "white", screen, button2.x + 15, button2.y + 10)
        draw_text("long", menu_font, "white", screen, button3.x + 15, button3.y + 10)
        draw_text("Return", menu_font, "white", screen, button4.x + 80, button4.y + 10)
        draw_text("Race Types", title_font, "lightblue", screen, button2.x + 350, button2.y +5)

        pygame.display.flip()
        clock.tick(60)
user_name()