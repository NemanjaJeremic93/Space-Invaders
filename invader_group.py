import pygame
import random
from invader import Invader
from settings import ( WIDTH, INVADER_ROWS, INVADER_COLUMNS, INVADER_WIDTH, INVADER_HEIGHT, INVADER_START_X,
                       INVADER_START_Y, INVADER_HORIZONTAL_SPACING, INVADER_VERTICAL_SPACING, INVADER_SPEED,
                       INVADER_DROP_DISTANCE, ENEMY_SHOOT_CHANCE, )


class InvaderGroup:

    def __init__(self):

        self.invaders = []

        self.speed = INVADER_SPEED
        self.direction = 1

        self.create_invaders()

    def create_invaders(self):
        self.invaders.clear()

        for row in range(INVADER_ROWS):
            for column in range(INVADER_COLUMNS):

                x = (
                    INVADER_START_X + column * (INVADER_WIDTH + INVADER_HORIZONTAL_SPACING)
                )

                y = (
                    INVADER_START_Y + row * (INVADER_HEIGHT + INVADER_VERTICAL_SPACING)
                )

                invader = Invader(x, y)

                self.invaders.append(invader)

    def update(self):
        move_down = False

        for invader in self.invaders:

            invader.rect.x += (self.speed * self.direction)

            if invader.rect.right >= WIDTH:
                move_down = True

            if invader.rect.left <= 0:
                move_down = True

        if move_down:
            self.direction *= -1

            for invader in self.invaders:

                invader.rect.y += INVADER_DROP_DISTANCE

    def draw(self, screen):
        for invader in self.invaders:

            invader.draw(screen)

    def shoot(self):

        if not self.invaders:
            return None

        if random.randint(1, ENEMY_SHOOT_CHANCE) != 1:
            return None

        shooter = random.choice(self.invaders)

        return shooter.shoot()

    def remove(self, invader):
        if invader in self.invaders:
            self.invaders.remove(invader)

    def is_empty(self):
        return len(self.invaders) == 0

    def reached_player(self, player):
        for invader in self.invaders:

            if invader.rect.bottom >= player.rect.top:
                return True

        return False
