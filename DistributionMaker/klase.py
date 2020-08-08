import pygame
from pygame import gfxdraw

WIN_W = 800
WIN_H = 500

ST_POS_X = 35
EN_POS_X = WIN_W - 30
ST_POS_Y = 35
EN_POS_Y = WIN_H - 35


red = (255, 0, 0)


class Slider:
    SLID_W = 5

    def __init__(self, i):
        self.x = ST_POS_X + self.SLID_W * i
        self.y = ST_POS_Y
        self.height = EN_POS_Y - ST_POS_Y


class Dot:
    def __init__(self, slider):
        self.slider = slider
        self.x = slider.x
        self.y = EN_POS_Y
        self.r = 5
        self.chance = 0

    def draw_dot(self, win):
        pygame.gfxdraw.aacircle(win, int(self.x), int(self.y), self.r, red)
        pygame.gfxdraw.filled_circle(win, int(self.x), int(self.y), self.r, red)

    def update_dot(self):
        if pygame.mouse.get_pressed()[0] == 1:
            if pygame.mouse.get_pos()[0] >= self.x and pygame.mouse.get_pos()[0] < self.x + self.slider.SLID_W:
                if pygame.mouse.get_pos()[1] > ST_POS_Y and pygame.mouse.get_pos()[1] < EN_POS_Y:
                    self.y = pygame.mouse.get_pos()[1]
                elif pygame.mouse.get_pos()[1] < ST_POS_Y:
                    self.y = ST_POS_Y
                else:
                    self.y = EN_POS_Y
                self.chance = (EN_POS_Y - self.y) / (EN_POS_Y - ST_POS_Y)
