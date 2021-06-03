import pygame
import random
import time
import sys

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Insertion sort")

MAIN_COLOR = (250, 242, 218)
S_COLOR = (142, 151, 117)
C_COLOR = (74, 80, 61)

FPS = 60

num_bars = 16
bar_width = 20
space = 5
bars = []

WIN.fill(MAIN_COLOR)

def sortowanie(l):
    dl = len(l)
    for i in range(1, dl):
        key = l[i]
        j = i-1
        while j >= 0 and key < l[j]:
            WIN.fill(MAIN_COLOR)
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

            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
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
    drawBar(x, height, (74, 80, 61))


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