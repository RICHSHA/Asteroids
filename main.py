import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 1:
        # handles breaking the loop and quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()
