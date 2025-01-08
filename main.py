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
    score = 0
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    game_over = False

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)

    # Create player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Screen and font setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 32)
    pygame.display.set_caption("boot.dev Asteroids Clone")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # Handle restart logic in game-over state
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return main()  # Restart the game by re-calling `main`

        # Clear the screen
        screen.fill(BLACK)
        # Draw the score
        score_sur = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_sur, (10, 10))

        # Game Over handling
        if game_over:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over! Press 'R' to Restart.", True, WHITE)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(30)
            continue

        # Update and draw all sprites
        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)

        # Collision detection
        for rock in asteroids:
            if player.collide(rock):
                game_over = True
                break  # Exit the loop if the game is over
            for bullet in bullets:
                if rock.collide(bullet):
                    rock.split(asteroids)
                    rock.kill()  # Destroy the asteroid
                    bullet.kill()  # Destroy the bullet
                    score += 1
                    break  # Exit the inner loop to avoid further checks on destroyed objects

        # Update the screen
        dt = clock.tick(60) / 1000.0
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
