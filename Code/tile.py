import pygame
from settings import * 

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups,sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft= pos)
        self.hitbox = self.rect.inflate(0, y_offset)
        
        
        #self.rect = self.image.get_rect(topleft = pos)
        #self.hitbox = self.rect.inflate(0, -10) # making the hitting point of the tile a little smaller creating overlap and making it look more natural. -10 makes the entire think shrink by 5 pixels on each side top and bottom 
