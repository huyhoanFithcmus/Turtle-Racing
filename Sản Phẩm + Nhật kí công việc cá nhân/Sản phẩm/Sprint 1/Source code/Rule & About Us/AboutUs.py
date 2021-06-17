import pygame, sys
clock = pygame.time.Clock()
FPS = 200

screen = pygame.display.set_mode((1050,600))

GREY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.font.init()
font = pygame.font.SysFont("Times New Roman" , 20)
AboutUs = font.render("ABOUT US", True, BLACK)
Back = font.render("Back", True, YELLOW)  

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width= 1020 
    max_height = 520
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
text1 = "                                                       Class: 20CLC02 - Group: 02 - Central Circus\n"\
"\n \n \n"\
"20127063 - Phan Minh Phúc ------   20127063@student.hcmus.edu.vn - Developer.\n"\
"20127129 - Lê Hải Đăng -----------  20127129@student.hcmus.edu.vn - Scrum Master & Project Manager.\n"\
"20127166 - Nguyễn Huy Hoàn ----  20127166@student.hcmus.edu.vn - Developer & Quality Assurance.\n"\
"20127188 - Nguyễn Quốc Huy ----  20127188@student.hcmus.edu.vn - Developer & Quality Control.\n"\
"20127445 - Đỗ Quốc Bảo ----------  20127445@student.hcmus.edu.vn - Developer & Designer.\n"\
"20127460 - Lý Văn Đạt ------------  20127460@student.hcmus.edu.vn - Business Analyst & Document Control.\n"\
 


running = True
pygame.display.set_caption("Racing Game")
pygame.display.set_icon(pygame.image.load(r'D:\python\RacingGame\racetrack.png'))

while running:
    dt = clock.tick(FPS) 
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, WHITE, pygame.Rect(425,10,200,30))
    screen.blit(AboutUs, (477, 15))
    
    pygame.draw.rect(screen, GREY, pygame.Rect(0,50,1050,580))
    pygame.draw.rect(screen, WHITE, pygame.Rect(10,60,1030,530))
    blit_text(screen, text1, (65, 100), font)

    pygame.draw.rect(screen,RED, pygame.Rect(880,545,150,35))
    screen.blit(Back, (935, 551))
        
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
