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
Rule = font.render("RULE", True, BLACK)
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
text = "Chào mừng các nhà đầu tư tài ba đến với tựa game của chúng tôi.\n"\
"Nhiệm vụ của bạn trong trò chơi này là tham gia phi vụ cá cược đua “rùa” lớn nhất hành tinh. \nMỗi lượt chơi sẽ gồm 5 lần cược; mỗi chặng đua gồm 6 lane và bạn sẽ phải đoán xem là con “rùa” nào sẽ là kẻ chiến thắng trong cuộc đua đầy khốc liệt này. \nĐây là một vài chỉ dẫn để các bạn đễ dàng tham gia trò chơi này:\n"\
"	Bước 1: Chọn loại đường đua (ngắn–vừa–dài).\n"\
"	Bước 2: Chọn nhân vật bạn muốn đặt cược.\n"\
"	Bước 3: Chọn mệnh giá bạn muốn đặt cược (100-200-500).\n"\
"	Bước 4: Tận hưởng sự hấp dẫn và hồi hộp của trò chơi.\n"\
"Khi đăng kí chơi lần đâu tiên, bạn sẽ có sẵn 800 tiền vàng trong tài khoản của mình.\n"\
"Tại mỗi chặng đua, bạn có thể dùng tiền này để đặt cược một số tiền (100–200–500) vào 1 nhân vật mà bạn cho là chiến thắng.\n"\
"Nếu nhân vật bạn đặt cược về nhất, bạn sẽ nhận được 100% số tiền bạn đã đặt.\n"\
"Nếu không, căn cứ theo thứ tự về đích của nhân vật mà bạn đặt cược (2, 3, 4, 5, 6) bạn sẽ bị trừ tương ứng (20%, 40%, 60%, 80%, 100%) khoảng tiền đã cược trong tài khoản.\n"\
"Nếu số tiền trong tài khoản của bạn tuột dốc không phanh? Đừng lo! Bạn có thể kiếm thêm tiền thông qua các minigame có trong trò chơi. (Lưu ý sô lần chơi minigame của bạn sẽ có giới hạn)\n"\
"Hãy thể hiện tài năng cuất chúng của mình bằng cách kiếm nhiều tiền nhất có thể.\n"\
"Chúc bạn may mắn =)))"\

running = True
pygame.display.set_caption("Racing Game")
pygame.display.set_icon(pygame.image.load(r'D:\python\RacingGame\racetrack.png'))

while running:
    dt = clock.tick(FPS) / 10
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, WHITE, pygame.Rect(425,10,200,30))
    screen.blit(Rule, (500, 15))
    
    pygame.draw.rect(screen, GREY, pygame.Rect(0,50,1050,580))
    pygame.draw.rect(screen, WHITE, pygame.Rect(10,60,1030,530))
    blit_text(screen, text, (35, 100), font)

    pygame.draw.rect(screen,RED, pygame.Rect(880,545,150,35))
    screen.blit(Back, (935, 551))
        
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
