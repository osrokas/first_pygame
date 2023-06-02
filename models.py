import pygame
from typing import Optional
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
    """
    The class describes all parameters and actions of player.
    """

    def __init__(self, img, x_pos, y_pos, group) -> None:

        super().__init__(group)
        # self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.image.load(img).convert()
        self.rect = self.img.get_rect(midbottom = (x_pos, y_pos) )
        
    # def control(self, speed_lr:float, speed_up: float, speed_down: float):
    def control(self): 
        """
        The method defines control of player.
        """  
        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_RIGHT]:
            self.rect.x+= 2
        if pressed_key[K_UP]:
            self.rect.y+= -1
        if pressed_key[K_DOWN]:
            self.rect.y+= +1

    def movement(self, screen : pygame.Surface):
        """
        The method defines movement of player.
        """
        
        screen.blit(self.img, (self.rect.x, self.rect.y))

    # def collider(self, bonus_point):

    #     get_bonus = pygame.sprite.spritecollide(self, bonus_point, True)
        
    #     print(self.rect)
    #     print(bonus_point)
        


class Enemy(pygame.sprite.Sprite):
    """
    The class describes all parameters and actions of enemy.
    """

    #Initialzaing parent class
    def __init__(self, img, x_pos, y_pos, group) -> None:

        super().__init__(group)
        # self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.image.load(img).convert()
        self.rect = self.img.get_rect(midbottom = (x_pos, y_pos) )
            
    def movement(self):
        """
        The method describes enemy movement.
        """

        self.rect.move_ip(1.2, 0)


# class Bonus(pygame.sprite.Sprite):
#     """
#     The class describes all parameters and actions of bonus.
#     """
#     def __init__(self, img: str, x_min, y_min, x_max, y_max, group) -> None:

#         #Initialzaing parent class
#         super().__init__(group)
        
#         self.img = pygame.image.load(img)
#         x_loc = random.randrange(x_min, x_max, 50)
#         y_loc = random.randrange(y_min, y_max, 50)
#         self.rect = self.img.get_rect()
#         self.rect.center = (x_loc, y_loc)

#     def show_player(self, resize: bool, factor: Optional[int] = 1):

#         if resize == True:
#             width = self.img.get_rect().width
#             height = self.img.get_rect().height
#             self.img = pygame.transform.scale(self.img, (width/factor, height/factor))
#         else:
#             self.img = self.img

#     def update_position(self):

#         self.rect.move_ip(1.1, 0)


class CameraGroup(pygame.sprite.Group):
    """
    The class describes game camera.
    """

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0,0)
        self.half_w = self.display_surface.get_size()[0] / 10
        self.half_h = self.display_surface.get_size()[1]

    def center_target_camera(self, target):
        """
        
        """
        
        self.offset.x = target.rect.centerx - self.half_w - 100
        self.offset.y = target.rect.centery - self.half_h + 200

    def sprites_draw(self, player, road, mountains):
        """
        Draw sprites on the screen and controls camera movement.
        """
        
        self.center_target_camera(player)
        ground_offset = (0,0) - self.offset
        lap = 0
        for value in road:
            self.display_surface.blit(value, (lap,400) + ground_offset)
            lap+=600
        self.display_surface.blit(mountains, ground_offset)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.img, offset_pos)


class Display(pygame.sprite.Sprite):
    
    def __init__(self) -> None:
        super().__init__()
        self.display_surf = pygame.Surface((1200, 900))
        self.display_surf.fill((137, 207, 240))

    def run_display(self, screen : pygame.Surface ):

        screen.blit(self.display_surf, [0,0])


class Background(pygame.sprite.Sprite):

        def __init__(self) -> None:
            
            super().__init__()

            self.mountains_surf = pygame.image.load('assets/mountains.png').convert_alpha()
            self.mountains_surf = pygame.transform.scale(self.mountains_surf, (1100, 400))

            self.road_surf = pygame.image.load('assets/road.png').convert_alpha()
            self.road_surf = pygame.transform.scale(self.road_surf, (600, 200))

        def return_background(self):
            
            roads = []
            i = 0
            while i < 10:
                self.road_surf_copy = self.road_surf.copy()
                roads.append(self.road_surf_copy)
                i+=1

            return self.mountains_surf, roads

        # def create_group(self):
            
        #     group = pygame.sprite.Group(self.mountains, self.road)

        #     return group