import pygame
from pygame.sprite import Group

from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from button import Button

import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    pygame.display.set_caption("alien invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard (ai_settings , screen, stats)
    
    
    #make the ship , group of bullets , group of aliens
    ship = Ship(screen , ai_settings)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #check status of game
    run = [True]
    #Start the mian loop for the game
    while run[0]:  
        gf.check_events( run , ai_settings, screen, stats, sb, play_button,
                        ship, aliens , bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                             play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats , sb , ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen,sb, ship, aliens, bullets)
            
        
    pygame.quit()
        
run_game()