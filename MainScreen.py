import pygame as pg
from time import sleep
from collections import defaultdict
from pygame.examples.music_drop_fade import draw_text_line

from Index import Index
from PersonList import PersonList


class MainScreen(object):
    def __init__(self):
        pg.init()
        self.screen =  pg.display.set_mode((800, 500))
        pg.display.set_caption("Main")
        info = pg.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h

        self.idx = Index()
        self.idx.x =  self.screen_width//2
        self.idx.y =  -self.screen_height//2

        self.main_font = pg.font.SysFont('Arial', 26)
        self.small_font = pg.font.SysFont('Arial', 15)

        self.keys = {'left': False, 'right': False, 'up': False, 'down': False}
        self.running = True

        self.person_list = PersonList()
        self.person_list.set_configue(self.screen_width, self.screen_height)

    def index_text(self):
        idx_position = self.idx.get_index()
        idx_txt = "(" + str(idx_position[0]) + ", " + str(idx_position[1]) + ")"
        text = self.main_font.render(idx_txt, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topright = (self.screen_width - 10, 10)
        self.screen.blit(text, text_rect)

    def persons_text(self):

        vertical_position = defaultdict(list)
        for person in self.person_list:
            text = self.small_font.render(person.get_name(), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (person.get_current_window_position(self.idx.get_index()))
            self.screen.blit(text, text_rect)
            # text_width, text_height =  self.small_font.size(person.get_name())
            self.draw_vertical_line(*person.get_position())
            if person.get_child_id() != -1:
                vertical_position[person.get_child_id()].append(person.get_position())

        for key in vertical_position.keys():
            self.draw_horizontal_line(*vertical_position[key][0], *vertical_position[key][1])

    def draw_horizontal_line(self, sx1, sy1, sx2, sy2):
        x, y = self.idx.get_index()
        sx1 += x
        sy1 -= y
        sx2 += x
        sy2 -= y

        pg.draw.line(self.screen, (255, 255, 255), (sx1, sy1 + 20), (sx2, sy2 + 20), 2)

    def draw_vertical_line(self, sx, sy):
        x, y = self.idx.get_index()
        sx += x
        sy -= y
        pg.draw.line(self.screen, (255, 255, 255), (sx, sy + 10), (sx, sy + 20), 2)
        pg.draw.line(self.screen, (255, 255, 255), (sx, sy - 10), (sx, sy - 20), 2)

    def create_moving_space(self):
        rect_width = int(self.screen_width * 0.8)
        rect_height = int(self.screen_height * 0.8)
        rect_x = (self.screen_width - rect_width) // 2
        rect_y = (self.screen_height - rect_height) // 2
        rect_color = (255, 255, 255)
        pg.draw.rect(self.screen, rect_color, (rect_x, rect_y, rect_width, rect_height), 5)

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.create_moving_space()
        self.index_text()
        self.persons_text()
        pg.display.flip()

    def check_arrow_keys(self, event, key_type = 'KEYUP'):
        change = False
        if key_type == 'KEYDOWN':
            change = True

        if event.key == pg.K_LEFT:
            self.keys['left'] = change
        if event.key == pg.K_RIGHT:
            self.keys['right'] = change
        if event.key == pg.K_UP:
            self.keys['up'] = change
        if event.key == pg.K_DOWN:
            self.keys['down'] = change

    def index_change(self):
        for direction, if_change in self.keys.items():
            if if_change:
                sleep(0.01)
                self.idx.turn(direction)
                self.update_screen()

    def event_change(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.KEYDOWN:
                self.check_arrow_keys(event, 'KEYDOWN')

            elif event.type == pg.KEYUP:
                self.check_arrow_keys(event, 'KEYUP')

    def run(self):
        self.update_screen()

        while self.running:
            self.event_change()
            self.index_change()
