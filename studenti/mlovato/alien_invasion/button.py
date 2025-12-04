# import pygame.font
import pygame


class Button:
    # class to create buttons
    def __init__(self, ai_game, msg):
        # initialize button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # set button dimensions
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 235)
        self.text_color = (255, 255, 255)
        # self.font = pygame.font.SysFont(None, 48)
        # create a rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # button text must be prepared just once
        # self._prep_msg(msg)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        # self.screen.blit(self.msg_image, self.msg_image_rect)

    """
        def _prep_msg(self, msg):
            # render a msg as an image and center onto the button
            self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center
    """
