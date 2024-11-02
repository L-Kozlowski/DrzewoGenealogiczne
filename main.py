import pygame
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def create_grid(rows : int, cols : int):
    tst = []
    for row in range(0, rows):
        tst.append([])
        for col in range(0, cols):
            tst[row].append([row,col])
    return  tst

def print_matrix(gird : list):
    for rows in gird:
        for cols in rows:
            print(cols, end=' | ')
        print('')

def turn(grid : list, direction : str):
    cnt_row = len(grid)
    cnt_col = len(grid[0])
    num = 0
    idx = 0
    if direction == 'left':
        num = -1
        idx = 1
    elif direction == 'right':
        num = 1
        idx = 1
    elif direction == 'up':
        num = -1
    elif direction == 'down':
        num = 1

    for row in range(0, cnt_row):
        for col in range(0, cnt_col):
            grid[row][col][idx] += num
    return grid


pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((500, 500))
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

grid = create_grid(screen_width, screen_height)


pygame.display.set_caption("Physics")
print()
print()
print()
running = True
while running:
    pygame.display.flip()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                grid = turn(grid, 'left')
            if event.key == pygame.K_RIGHT:
                grid = turn(grid, 'right')
            if event.key == pygame.K_UP:
                grid = turn(grid, 'up')
            if event.key == pygame.K_DOWN:
                grid = turn(grid, 'down')
            print('tst')
            # print_matrix(grid)
