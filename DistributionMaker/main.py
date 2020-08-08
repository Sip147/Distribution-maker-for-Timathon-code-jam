import pygame
import funkcije
import klase
import random


pygame.font.init()

WIN_W = 800
WIN_H = 500

ST_POS_X = 35
EN_POS_X = WIN_W - 30
ST_POS_Y = 35
EN_POS_Y = WIN_H - 35

white = (255, 255, 255)
black = (0, 0, 0)

dots = []
chosenDot = 0
number = None
sliders = []


def main():
    global number
    win = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption('Distribution maker (L-click to draw distribution; R-click to generate number)')
    run = True
    global sliders
    global dots
    global chosenDot
    canGenerate = True
    generateNumber = False
    maxNumber = funkcije.maxNumber
    precision = funkcije.precision
    # clock = pygame.time.Clock()
    for i in range(int((EN_POS_X - ST_POS_X) / 5)):
        sliders.append(klase.Slider(i))
        dots.append(klase.Dot(sliders[i]))

    numPoints = len(sliders)

    pointWidth = maxNumber / numPoints

    while run:
        # clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        funkcije.draw(win)
        for i, dot in enumerate(dots):
            dot.update_dot()
            # dot.draw_dot(win)
            try:
                funkcije.draw_line(win, dot.x, dot.y, dots[i + 1].x, dots[i + 1].y)
            except IndexError:
                pass

        if pygame.mouse.get_pressed()[2] == 1 and canGenerate:
            generateNumber = True
            canGenerate = False

        if pygame.mouse.get_pressed()[2] == 0:
            canGenerate = True

        if generateNumber:
            for dot in dots:
                if not dot.chance == 0:
                    while number == None:
                        chosenDot = choose_dot()
                        for i, dot in enumerate(dots):
                            if chosenDot == dot:
                                number = random.uniform((maxNumber / numPoints * i), (maxNumber / numPoints * i + (maxNumber / numPoints)))
                                number = round(number, int(precision))

            print(number)
            number = None

            generateNumber = False

        pygame.display.update()


def choose_dot():
    global dots
    global chosenDot
    newDots = dots.copy()
    random.shuffle(newDots)
    randomNum = random.random()
    for dot in newDots:
        if dot.chance > randomNum:
            chosenDot = dot
            return chosenDot


main()
