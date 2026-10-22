import pygame
from pathlib import Path
from bullet import Bullet
from settings import INVADER_WIDTH, INVADER_HEIGHT, ENEMY_BULLET_SPEED, RED, YELLOW

ASSET_DIR = Path(__file__).parent / "assets"

class Invader:

    def __init__(self, x, y):
        self.image = pygame.image.load(
            str(ASSET_DIR / "alien.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (INVADER_WIDTH, INVADER_HEIGHT)
        )

        self.rect = self.image.get_rect(
            topleft=(x, y)
        )

        self.color = RED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):

        return Bullet(
            self.rect.centerx - 3,
            self.rect.bottom,
            ENEMY_BULLET_SPEED,
            YELLOW,
            1,
        )
