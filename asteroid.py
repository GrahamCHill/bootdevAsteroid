import pygame
from pygame.transform import rotate

import circleshape
import constants
import random


class Asteroid(circleshape.CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroid_group):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        # Calculate new velocities based on random angles
        random_angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(random_angle)  # Rotating the velocity vector
        angle2 = self.velocity.rotate(-random_angle)

        # Reduce the radius for the new asteroids
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        # Create two new asteroids
        _asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        _asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities
        _asteroid1.velocity = angle1 * 1.2  # Scale the velocity vector
        _asteroid2.velocity = angle2 * 1.2  # Scale the velocity vector

        # Add the new asteroids to the game
        asteroid_group.add(_asteroid1)
        asteroid_group.add(_asteroid2)

        # Destroy the current asteroid
        self.kill()

