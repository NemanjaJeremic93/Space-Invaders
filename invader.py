import pygame
from bullet import Bullet
from settings import INVADER_WIDTH, INVADER_HEIGHT, ENEMY_BULLET_SPEED, RED, YELLOW


class Invader:

    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x,
            y,
            INVADER_WIDTH,
            INVADER_HEIGHT
        )

        self.color = RED

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect
        )

    def shoot(self):

        return Bullet(
            self.rect.centerx - 3,
            self.rect.bottom,
            ENEMY_BULLET_SPEED,
            YELLOW,
            1,
        )
