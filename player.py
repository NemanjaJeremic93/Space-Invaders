import pygame
from pathlib import Path
from bullet import Bullet
from settings import (WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED,
                      PLAYER_BULLET_SPEED, PLAYER_SHOOT_DELAY, GREEN, WHITE)

ASSET_DIR = Path(__file__).parent / "assets"

class Player:

    def __init__(self):

        self.image = pygame.image.load(
            str(ASSET_DIR / "player.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (PLAYER_WIDTH, PLAYER_HEIGHT)
        )

        self.rect = self.image.get_rect(
            midbottom=(WIDTH // 2, HEIGHT - 30)
        )

        self.speed = PLAYER_SPEED

        self.shoot_cooldown = 0
        self.shoot_delay = PLAYER_SHOOT_DELAY

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Keep player inside the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # Shooting cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def shoot(self):
        if self.shoot_cooldown > 0:
            return None

        bullet = Bullet(
            self.rect.centerx - 3,
            self.rect.top - 10,
            PLAYER_BULLET_SPEED,
            WHITE,
            -1,
        )

        self.shoot_cooldown = self.shoot_delay

        return bullet

    def draw(self, screen):
        screen.blit(self.image, self.rect)
