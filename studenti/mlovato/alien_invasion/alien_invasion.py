import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Create the base of the game"""

    def __init__(self):
        """
        Initialize resouces"""

        _ = pygame.init()
        # initialize a clock
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # new instance of stats
        self.stats = GameStats(self)
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        # group of bullets, like a list
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # start alien invasion only when flag is true
        # alien_invasion starts when hit play
        self.game_active = False
        # create play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """
        Start the game"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            # clock for fps so the game will run at the same speed on every
            # machine
            _ = self.clock.tick(60)

    def _check_events(self):
        # waiting for events from mouse or keyboad
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        # start new game when mouse click play button
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # reset game stats so game can be playied again
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.game_active = True
            # delete bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            # create new aliens' group and center ship
            self._create_fleet()
            self.ship.center_ship()
            # hide mouse
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        # create a new bullet and add to the group
        # limited to #bullets_allowed bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # create a group of aliens
        # create a new alien until there no more space
        # space between aliens is the width of the single alien
        # create a new alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        # append new alien to the group
        self.aliens.add(alien)
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _ship_hit(self):
        # if there is a ship left decrement
        # else stop game
        if self.stats.ship_left > 0:
            # ship collisions
            self.stats.ship_left -= 1
            # delete bullets
            self.bullets.empty()
            self.aliens.empty()
            # create new aliens
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        # check if an alien hit the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # same thing as ship hit
                self._ship_hit()
                break

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position

        self.aliens.add(new_alien)

    def _update_aliens(self):
        # update aliens' position
        self._check_fleet_edges()
        self.aliens.update()
        # look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # type:ignore
            self._ship_hit()
        # check alien and bottom screen collision
        self._check_aliens_bottom()

    def _update_screen(self):
        # draw the screen every cycle
        _ = self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # draw all the group of aliens to the screen
        self.aliens.draw(self.screen)

        # draw button if screen inactive
        if not self.game_active:
            self.play_button.draw_button()

        # update screen
        pygame.display.flip()

    def _update_bullets(self):
        # calling update on a group will call update for every element of the group
        self.bullets.update()
        # delete bullets out of screen
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # lower aliens when they hit the border and change direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        # check if bullets hit any alien
        # if do, delete both alien and bullet
        # collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # for super power bullet pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        _ = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # if there are no more aliens
        if not self.aliens:
            # destroy all active bullets and create a new group of aliens
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
