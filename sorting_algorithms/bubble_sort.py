import pygame
import random
import time
import sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble sort")

MAIN_COLOR = (232, 69, 69)
S_COLOR = (144, 55, 73)
C_COLOR = (83, 53, 74)

FPS = 60

num_bars = 16
bar_width = 20
space = 5
bars = []

sorting = False

WIN.fill(MAIN_COLOR)

def sortowanie(l):
    dl = len(l)
    for i in range(dl):
        check = False
        for j in range(0, dl-1-i):

            for k in range(num_bars):
                x = (k * bar_width) + (k * space) + (WIDTH - (num_bars * bar_width + num_bars * space))/2
                height = bars[k]
                if bars[k] is bars[j] or bars[k] is bars[j+1]:
                    color = S_COLOR
                else:
                    color = C_COLOR
                drawBar(x, height, color)
                time.sleep(.005)
            pygame.display.update()
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                check = True
                WIN.fill(MAIN_COLOR)
        if not check:
            break
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



def drawBar(x, height, color):
    pygame.draw.rect(WIN, color, (x, 200, bar_width, height), 0)
    bars.append(height)


for i in range(num_bars):
    height = random.randint(10, 100)
    x = (i * bar_width) + (i * space) + (WIDTH - (num_bars * bar_width + num_bars * space))/2
    drawBar(x, height, (0, 0, 0))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        pygame.display.update()
        if sorting:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

sortowanie(bars)
main()