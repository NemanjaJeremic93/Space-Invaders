import pygame
from bullet import Bullet
from settings import (WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED,
                      PLAYER_BULLET_SPEED, PLAYER_SHOOT_DELAY, GREEN, WHITE)


class Player:

    def __init__(self):

        self.rect = pygame.Rect(
            WIDTH // 2 - PLAYER_WIDTH // 2,
            HEIGHT - 60,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
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
        pygame.draw.rect(
            screen,
            GREEN,
            self.rect,
        )
