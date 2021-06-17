import pygame 

color = (0,0,0)
red = (255,0,0)
white = (255,255,255)

def next():
    pass


def main():
    screen = pygame.display.set_mode((1050, 650))
    background = pygame.transform.scale(pygame.image.load("17933.jpg"),(1050,650))
    font = pygame.font.Font("8-BIT WONDER.TTF", 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(420, 350, 140, 50)
    color_inactive = pygame.Color('red')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    text1 = font.render("Your have 100 dollars",True,red)
    text2 = font.render("please type monney you want to bet", True,red)
    text3 = font.render("NEXT",True,red)
    done = False


    while not done:
        # fill the bg
        screen.blit(background,[0,0])
        # get text to screen
        screen.blit(text1,[250,0])
        screen.blit(text2,[15,100])
        screen.blit(text3,[450,600])
        # set the box to sceen
    
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