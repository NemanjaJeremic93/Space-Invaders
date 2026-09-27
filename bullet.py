import pygame
from settings import HEIGHT


class Bullet:

    def __init__(
            self,
            x,
            y,
            speed,
            color,
            direction,
    ):

        self.rect = pygame.Rect(
            x,
            y,
            6,
            12,
        )

        self.speed = speed
        self.color = color
        self.direction = direction

    def update(self):
            self.rect.y += (self.speed * self.direction)

    def draw(self, screen):
            pygame.draw.rect(
                screen,
                self.color,
                self.rect,
            )

    def is_off_screen(self):
        return self.rect.bottom < 0 or self.rect.top > HEIGHT
