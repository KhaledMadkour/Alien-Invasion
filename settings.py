class Settings():
    """A class to store settings for Alien_invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #scoring
        self.alien_points = 50
        
        #bullet speed
        self.bullets_allowed = 3
        
        #settings incase of drawing
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        
        # Alien settings 1
        self.fleet_drop_speed = 10
        
        #GameStats
        self.ship_limit = 3
        
        # level up scaling
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.alien_points = int(self.alien_points * self.score_scale)
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale