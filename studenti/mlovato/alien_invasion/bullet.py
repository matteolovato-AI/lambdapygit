import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # bullets from spaceship
    def __init__(self, ai_game):
        # add fired bullet on spaceship position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # create rect for bullet from (0,0) bullet position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # position bullet midtop equal ship midtop
        self.rect.midtop = ai_game.ship.rect.midtop
        # bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        # bullets go to the top
        self.y -= self.settings.bullet_speed
        # update real bullet's position
        self.rect.y = self.y

    def draw_bullet(self):
        # draw the actual bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
