import pygame

pygame.font.init()
FONT = pygame.font.SysFont('arialblack', 10)

WIN_W = 800
WIN_H = 500

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

maxNumber = float(input('Enter maximum of distribution: '))
precision = float(input('Enter number of digits after decimal: '))


text1 = FONT.render('1', True, black)
text2 = FONT.render('.5', True, black)
text3 = FONT.render('0', True, black)
text4 = FONT.render(str(maxNumber), True, black)


def draw(win):
    win.fill(white)
    pygame.draw.line(win, black, (35, 35), (35, WIN_H - 20))
    pygame.draw.line(win, black, (20, WIN_H - 35), (WIN_W - 30, WIN_H - 35))
    win.blit(text1, (25, 30))
    win.blit(text2, (21, (WIN_H - 20) / 2 - 5))
    win.blit(text3, (25, WIN_H - 35))
    win.blit(text4, (WIN_W - 30 - text4.get_width(), WIN_H - 35))


def draw_line(win, x1, y1, x2, y2):
    # pygame.gfxdraw.line(win, x1, y1, x2, y2, red)
    pygame.draw.line(win, red, (x1, y1), (x2, y2), 5)
