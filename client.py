import pygame
from network import Network
from player import Player

witdh = 500
height = 500
win = pygame.display.set_mode((witdh, height))
pygame.display.set_caption("Client")

def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    p = n.getP()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        p2 = n.send(p)
        redrawWindow(win, p, p2)


if __name__ == "__main__":
    main()
