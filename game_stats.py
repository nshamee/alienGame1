
class gameStats:

    def __init__(self):
        self.settings = ai_game.settings
        self.reset_stats()

        def reset_stats(self):
            self.ships_left = self.settings.ship_limit