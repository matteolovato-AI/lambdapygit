import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # a single alien
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
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
