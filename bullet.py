import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self , ai_settings , screen , ship):
        """Create a bullet a the ships current position."""
        super().__init__()
        self.screen = screen
        
        
        ###Draw Bullet (option 1)..
        self.rect = pygame.Rect(0 , 0 , ai_settings.bullet_width ,
                                ai_settings.bullet_height)
        self.color = ai_settings.bullet_color
        
        
        ###option 2 Image
        #self.image = pygame.image.load('images/bullets/Bluebullet.png')
        #self.rect = self.image.get_rect()
        
        
        self.rect.centerx =  ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store bullet position a decimal value
        self.y = float(self.rect.y)
        
        
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        
        """Move the bullet"""
        # Update the decimal poisition of the bullet.
        self.y -= self.speed_factor
        self.rect.y = self.y
        
        
        
    def blitme(self):
        """Draw the bullet"""
        ###DrawBullet(Option1) >>
        pygame.draw.rect(self.screen , self.color , self.rect)
        
        ###image (Option2)
        #self.screen.blit(self.image, self.rect)