import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # print("Starting Asteroids!")
    # print(f'Screen width: {SCREEN_WIDTH}')
    # print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while 1:
        # handles breaking the loop and quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0, 0, 0))  # Fill the screen with black
  
        # draw all the objects
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        
        # Update the display
        pygame.display.flip()  

        
        for a in asteroids:
            if a.collision(player):
                print('Game over!')
                sys.exit()
            
            for s in shots:
                if a.collision(s):
                    a.split()
                    s.kill()
        

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
