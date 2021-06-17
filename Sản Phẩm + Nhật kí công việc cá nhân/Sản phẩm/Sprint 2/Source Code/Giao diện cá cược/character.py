import pygame 

color = (0,0,0)
red = (255,0,0)
white = (255,255,255)

def start():
    pass


def main():
    screen = pygame.display.set_mode((1050, 650))
    font = pygame.font.Font("8-BIT WONDER.TTF", 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(750, 350, 140, 50)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    text1 = font.render("CHOOSE YOUR CHARACTER",True,red)
    text2 = font.render("", True,red)
    text3 = font.render("START",True,red)
    done = False
    #import turtle
    image1 = pygame.transform.scale(pygame.image.load('rua1.png'),(100,100)) 
    image2 = pygame.transform.scale(pygame.image.load('rua2.png'),(100,100)) 
    image3 = pygame.transform.scale(pygame.image.load('rua3.png'),(100,100)) 
    image4 = pygame.transform.scale(pygame.image.load('rua4.png'),(100,100)) 
    image5 = pygame.transform.scale(pygame.image.load('rua5.png'),(100,100)) 
    image6 = pygame.transform.scale(pygame.image.load('rua6.png'),(100,100)) 
    #import num of turtle
    tex1 = font.render("1",True,red)
    tex2 = font.render("2",True,red)
    tex3 = font.render("3",True,red)
    tex4 = font.render("4",True,red)
    tex5 = font.render("5",True,red)
    tex6 = font.render("6",True,red)
    #set background
    background = pygame.transform.scale(pygame.image.load("background.png"),(1050,650))
    while not done:
        # fill the bg
        screen.blit(background,[0,0])
        # get text to screen
        screen.blit(text1,[50,350])
        screen.blit(text2,[15,100])
        screen.blit(text3,[450,450])
        #set turtle to screen
        screen.blit(image1,(100,100))
        screen.blit(image2,(480,100))
        screen.blit(image3,(850,100))
        screen.blit(image4,(100,200))
        screen.blit(image5,(480,200))
        screen.blit(image6,(850,200))
        #set the num of turtles
        screen.blit(tex1,(100,100))
        screen.blit(tex2,(480,100))
        screen.blit(tex3,(850,100))
        screen.blit(tex4,(100,200))
        screen.blit(tex5,(480,200))
        screen.blit(tex6,(850,200))
        # set the quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()