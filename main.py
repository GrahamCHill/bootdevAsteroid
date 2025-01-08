import pygame

from shot import Shot
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

    bullets = pygame.sprite.Group()

    Shot.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("boot.dev Asteroid Clone")
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
            for bullet in bullets:  # Copy the list to safely modify during iteration
                if rock.collide(bullet):
                    rock.split(asteroids)
                    rock.kill()  # Custom method to handle the asteroid's destruction
                    bullet.kill()  # Custom method to handle the bullet's destruction
                    asteroids.remove(rock)  # Remove the asteroid from the list
                    bullets.remove(bullet)  # Remove the bullet from the list
                    break  # Exit inner loop to avoid further checks on destroyed objects

        dt = clock.tick(60) / 1000.0
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()