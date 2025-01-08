import pygame

import circleshape
import constants


class Shot(circleshape.CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, constants.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)