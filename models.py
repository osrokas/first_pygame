import pygame
from typing import Optional
from pygame.locals import *
import random


class Player(pygame.sprite.Sprite):
    """
    The class describes all parameters and actions of player.
    """

    def __init__(self, img, x_loc, y_loc, group) -> None:

        super().__init__(group)
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect.center = (x_loc, y_loc)
        
    def show_player(self, resize: bool, factor: Optional[int] = 1):

        if resize == True:
            width = self.img.get_rect().width
            height = self.img.get_rect().height
            self.img = pygame.transform.scale(self.img, (width/factor, height/factor))

        else:
            self.img = self.img

    def control(self, speed_lr:float, speed_up: float, speed_down: float):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_RIGHT]:
            self.rect.move_ip(speed_lr, 0)
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -speed_up)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, speed_down)

    def collider(self, bonus_point):

        get_bonus = pygame.sprite.spritecollide(self, bonus_point, True)
        
        print(self.rect)
        print(bonus_point)
        


class Enemy(pygame.sprite.Sprite):
    """
    The class describes all parameters and actions of enemy.
    """
    def __init__(self, img, x_loc, y_loc, group) -> None:

        #Initialzaing parent class
        super().__init__(group)
        
        self.img = pygame.image.load(img)

        self.rect = self.img.get_rect()
        self.rect.center = (x_loc, y_loc)

    def show_player(self, resize: bool, factor: Optional[int] = 1):

        if resize == True:
            width = self.img.get_rect().width
            height = self.img.get_rect().height
            self.img = pygame.transform.scale(self.img, (width/factor, height/factor))
        else:
            self.img = self.img

    def update_position(self):

        self.rect.move_ip(1.1, 0)


class Bonus(pygame.sprite.Sprite):
    """
    The class describes all parameters and actions of bonus.
    """
    def __init__(self, img: str, x_min, y_min, x_max, y_max, group) -> None:

        #Initialzaing parent class
        super().__init__(group)
        
        self.img = pygame.image.load(img)
        x_loc = random.randrange(x_min, x_max, 50)
        y_loc = random.randrange(y_min, y_max, 50)
        self.rect = self.img.get_rect()
        self.rect.center = (x_loc, y_loc)

    def show_player(self, resize: bool, factor: Optional[int] = 1):

        if resize == True:
            width = self.img.get_rect().width
            height = self.img.get_rect().height
            self.img = pygame.transform.scale(self.img, (width/factor, height/factor))
        else:
            self.img = self.img

    def update_position(self):

        self.rect.move_ip(1.1, 0)


class CameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2(0,20)
        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1]

        # background
        self.background_surf = pygame.image.load('assets/background.png').convert()
        self.background_rect = self.background_surf.get_rect(topleft=(0,0))

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def sprites_draw(self, player):

        self.center_target_camera(player)
        ground_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background_surf, ground_offset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.img, offset_pos)


    






    