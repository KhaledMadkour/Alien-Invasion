class GameStats():
    """Track statistics for Alein invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.high_score = 0
        with open('HighScore.txt', 'r') as f:
            self.high_score = int (f.read())
        self.level = 0
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.reset_stats()
                
    def reset_stats(self):
        """initialize statistics than can change through the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0