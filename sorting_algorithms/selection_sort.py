import pygame
import random
import time
import sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selection sort")

MAIN_COLOR = (255, 245, 235)
S_COLOR = (244, 199, 171)
C_COLOR = (217, 152, 121)

FPS = 60

num_bars = 16
bar_width = 20
space = 5
bars = []

WIN.fill(MAIN_COLOR)

def sortowanie(l):
    dl = len(l)
    for i in range(dl-1):
        for j in range(i+1, dl):
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]

        for k in range(num_bars):
            x = (k * bar_width) + (k * space) + (WIDTH - (num_bars * bar_width + num_bars * space)) / 2
            height = bars[k]
            if bars[k] is bars[i] or bars[k] is bars[j]:
                color = S_COLOR
            else:
                color = C_COLOR
            drawBar(x, height, color)
            time.sleep(.005)
        pygame.display.update()
        WIN.fill(MAIN_COLOR)
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
    drawBar(x, height, (217, 152, 121))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

sortowanie(bars)
main()