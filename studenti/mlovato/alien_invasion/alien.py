import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # a single alien
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # load image
        self.image = pygame.transform.scale(
            pygame.image.load("images/alien.bmp"), (60, 85)
        )
        self.rect = self.image.get_rect()
        # add every alien at 0,0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save precise position of the alien
        self.x = float(self.rect.x)

    def update(self):
        # move aliens to the right or to the left (fleet direction = -1 if left otherwhise 1)
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        # return True if an alien hit the border
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
