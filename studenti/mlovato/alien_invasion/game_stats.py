class GameStats:
    # track game statistics
    def __init__(self, ai_game):
        # initialize stats
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        # start fresh
        self.ship_left = self.settings.ship_limit
