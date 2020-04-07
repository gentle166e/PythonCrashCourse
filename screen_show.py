import pygame
import sys


def show():
    pygame.init()
    pygame.display.set_caption('My Game')
    screen = pygame.display.set_mode((500, 300))
    bg_color = (230, 230, 230)
    screen.fill(bg_color)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    show()
