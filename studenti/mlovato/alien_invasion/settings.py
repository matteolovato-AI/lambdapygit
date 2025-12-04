class Settings:
    """Containes all of Alien Invasion's settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (30, 30, 30)
        # ship speed
        self.ship_speed = 1.5
        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 60, 60)
        self.bullets_allowed = 3
        # alien settings
        self.alien_speed = 1.0
        # speed which aliens drop when they hit the border
        self.fleet_drop_speed = 10
        # fleet_direction 1 is equal to right
        # fleet_direction -1 is equal to left
        self.fleet_direction = 1
