     #python setup
import pygame, sys
pygame.init()                                       
clock = pygame.time.Clock()

    #username display setup
screen = pygame.display.set_mode([800, 650])
base_font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 50)

    #content setup
color_active = pygame.Color("lightskyblue3")
color_passive = pygame.Color("gray15")
color = color_passive

    #ham in chu
def draw_text (text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    text_position = (x, y)
    surface.blit (textobj, text_position)

    #ham in username
def user_name():
    user_text = 'enter username: '
    game_title = "RACING GAME"
    #demo_font = pygame.font.Font('8-BIT WONDER.TTF', 50)

    # tao khung dien username, switch screen
    username_button = pygame.Rect(280, 400, 240 , 35)
    switchscreen_button = pygame.Rect(480, 400, 40, 35)
    

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
                            if len(user_text) < 20: 
                                #lay tat ca nhung gi nguoi dung nhap
                                user_text += event.unicode    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if switchscreen_button.collidepoint(event.pos):
                        username_running = False
                        #THAY DONG COMMENT NAY THANH HAM MAIN_MENU!
                          
            
        if active == False:
            color = color_active
        else:
            color = color_passive

        #mau trang    
        screen.fill ((250, 250, 250)) 

        pygame.draw.rect(screen, color, username_button, 2)
        pygame.draw.rect(screen, color, switchscreen_button, 2)

        draw_text(user_text, base_font, (0, 0, 0), screen, username_button.x + 5, username_button.y + 5)
        draw_text(game_title, title_font, (0, 0, 0), screen, 280, 200)

        pygame.display.flip()
        clock.tick(60)
user_name()

