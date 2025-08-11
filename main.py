import pygame
from constants import *
from player import Player

def main():
    # print("Starting Asteroids!")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while 1:
        # handles breaking the loop and quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))  # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()  # Update the display





        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
