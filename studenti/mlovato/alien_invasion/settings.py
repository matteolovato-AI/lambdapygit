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
