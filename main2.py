from time import sleep
import pygame
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def turn(index : list, direction : str):
    num = 0
    col = 0
    if direction == 'left':
        num = -1
        col = 1
    elif direction == 'right':
        num = 1
        col = 1
    elif direction == 'up':
        num = -1
    elif direction == 'down':
        num = 1

    index[col] += num
    return index

pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((500, 500))
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
index = [0,0]

font = pygame.font.SysFont(None, 36)

# Obliczenie rozmiarów prostokąta (90% rozmiaru ekranu)
rect_width = int(screen_width * 0.8)
rect_height = int(screen_height * 0.8)

# Obliczenie pozycji (lewego górnego rogu) prostokąta, aby znalazł się w centrum
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2

# Kolor prostokąta (biały)
rect_color = (255, 255, 255)


def update_screen(txt : str):
    text = font.render(txt, True, (255, 255, 255))
    screen.fill((0, 0, 0))
    text_rect = text.get_rect()
    text_rect.topright = (screen_width - 10, 10)
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height), 5)
    pygame.draw.rect(screen, rect_color, (rect_x + index[1], rect_y + index[0], 10, 10), 5)

    pygame.display.flip()

pygame.display.set_caption("Zuzia")
print()
print()
print()
pygame.display.flip()
update_screen(str(index))

running = True
key = False
direction = ''
while running:
    events = pygame.event.get()
    if key:
        sleep(0.01)
        index = turn(index, direction)
        update_screen(str(index))

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                key = True
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                key = True
                direction = 'right'
            if event.key == pygame.K_UP:
                key = True
                direction = 'up'
            if event.key == pygame.K_DOWN:
                key = True
                direction = 'down'

        if event.type == pygame.KEYUP:
                key = False
                direction = ''

        # print_matrix(grid)
