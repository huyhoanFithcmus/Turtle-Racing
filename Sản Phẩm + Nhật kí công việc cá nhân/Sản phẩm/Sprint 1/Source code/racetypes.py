    #python setup
import pygame, sys
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
                    #DAT HAM DUONG DUA NGAN VAO DONG CMT NAY!
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
