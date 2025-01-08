import pygame

from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for rock in asteroids:
            if player.collide(rock):
                pygame.quit()
                print("Game over!")
                return
        dt = clock.tick(60) / 1000.0
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()