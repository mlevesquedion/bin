import pygame
import random
import sys
import time

usage = """\
rmd [reminder_text] [remind_me_in] [time_unit]
available time units are 's', 'm' and 'h', 's' is default
(press enter to exit) """

try:
    text = sys.argv[1]
    after = int(sys.argv[2])
except IndexError:
    input(usage)
    sys.exit(0)
try:
    unit = sys.argv[3]
except IndexError:
    unit = 's'

if unit == 'm':
    after *= 60
elif unit == 'h':
    after *= 3600

for _ in range(after):
    time.sleep(1)

pygame.init()
display_info = pygame.display.Info()
W, H = display_info.current_w, display_info.current_h
DISPLAY = pygame.display.set_mode((W, H), pygame.FULLSCREEN)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 50)
MAGENTA = (255, 50, 255)
CYAN = (50, 255, 255)
COLORS = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN]
random.shuffle(COLORS)

CLOCK = pygame.time.Clock()
FPS = 2

font_size = W // (len(text) + 1)
font = pygame.font.SysFont('times', font_size, True)
text_surf = font.render(text, True, BLACK)
text_rect = text_surf.get_rect()
text_rect.center = (W//2, H//2)

i = 0
Quit = False
while not Quit:

    DISPLAY.fill(COLORS[i % len(COLORS)])
    DISPLAY.blit(text_surf, text_rect)
    pygame.display.update()

    i += 1
    CLOCK.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Quit = True
        if event.type == pygame.QUIT:
            Quit = True

pygame.quit()
sys.exit()
