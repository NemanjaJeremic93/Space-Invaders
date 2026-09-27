import pygame

from bullet import Bullet
from player import Player
from invader_group import InvaderGroup
from settings import WIDTH, HEIGHT, FPS, BLACK, WHITE, STARTING_LIVES, POINTS_PER_INVADER


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)

        self.running = True

        self.restart()

    # RESTART

    def restart(self):
        self.player = Player()
        self.invader_group = InvaderGroup()

        self.player_bullets = []
        self.enemy_bullets = []

        self.score = 0
        self.lives = STARTING_LIVES

        self.game_over = False
        self.won = False

    # EVENTS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        bullet = self.player.shoot()
                        if bullet:
                            self.player_bullets.append(bullet)

                elif event.key == pygame.K_r:
                    if self.game_over:
                        self.restart()

    # UPDATE

    def update(self):
        if self.game_over:
            return

        self.player.update()
        self.invader_group.update()
        self.update_player_bullets()
        self.update_enemy_bullets()
        self.enemy_shooting()
        self.check_collisions()
        self.check_game_state()

    # PLAYER BULLETS

    def update_player_bullets(self):
        for bullet in self.player_bullets[:]:
            bullet.update()

            if bullet.is_off_screen():
                self.player_bullets.remove(bullet)

    # ENEMY BULLETS

    def update_enemy_bullets(self):
        for bullet in self.enemy_bullets[:]:
            bullet.update()

            if bullet.is_off_screen():
                self.enemy_bullets.remove(bullet)

            elif bullet.rect.colliderect(self.player.rect):
                self.enemy_bullets.remove(bullet)

                self.lives -= 1

                if self.lives <= 0:
                    self.game_over = True

    # ENEMY SHOOTING

    def enemy_shooting(self):
        bullet = self.invader_group.shoot()

        if bullet:
            self.enemy_bullets.append(bullet)

    # COLLISIONS

    def check_collisions(self):
        for bullet in self.player_bullets[:]:
            for invader in self.invader_group.invaders[:]:
                if bullet.rect.colliderect(invader.rect):
                    self.invader_group.remove(invader)
                    self.player_bullets.remove(bullet)
                    self.score += POINTS_PER_INVADER

                    break

    # GAME STATE

    def check_game_state(self):
        if self.invader_group.is_empty():
            self.game_over = True
            self.won = True

        elif self.invader_group.reached_player(self.player):
            self.game_over = True
            self.won = False

    # DRAW

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.invader_group.draw(self.screen)

        for bullet in self.player_bullets:
            bullet.draw(self.screen)

        for bullet in self.enemy_bullets:
            bullet.draw(self.screen)

        self.draw_hud()

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    # HUD

    def draw_hud(self):
        score_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        lives_text = self.font.render(f"Score: {self.score}", True, WHITE)

        self.screen.blit(score_text, (20, 20))
        self.screen.blit(lives_text, (WIDTH - 120, 20))

    # GAME OVER SCREEN

    def draw_game_over(self):
        if self.won:
            message = "You win!"
        else:
            message = "GAME OVER!"

        game_over_text = self.big_font.render(message, True, WHITE)
        reset_text = self.font.render("Press R to restart", True, WHITE)

        self.screen.blit(
            game_over_text,
            game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        )

        self.screen.blit(
            reset_text,
            reset_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        )

    # MAIN LOOP

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()