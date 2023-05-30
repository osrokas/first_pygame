import pygame
from models import Player, CameraGroup, Background, Display
import time
from sys import exit


def main():

    pygame.init()

    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Riders On The Storm")
    clock = pygame.time.Clock()
    display = Display()

    mountains, road = Background().return_background()
    camera_group = CameraGroup()
    
    # icon = pygame.image.load('assets/cycling.png')
    # pygame.display.set_icon(icon)
    
    player = Player('assets/racing.png',x_pos=100, y_pos=600)
    # player = Player('assets/racing.png', x_loc=0, y_loc=0, group=camera_group)
    # player.show_player(resize=True, factor=5)

    # enemy = Enemy('assets/enemy.png', x_loc=100, y_loc=980, group=camera_group)
    # enemy.show_player(resize=True, factor=5)

    # enemy_2 = Enemy('assets/enemy.png', x_loc=200, y_loc=1020, group=camera_group)
    # enemy_2.show_player(resize=True, factor=5)
    # coins = pygame.sprite.Group()

    # for a in range(10):
    #     bonus_point = Bonus('assets/bonus.png', x_min=-200, x_max=1100, y_min= 890, y_max=1000, group=camera_group)
    #     bonus_point.show_player(resize=True, factor=10)
    #     pygame.draw.rect(screen, (255, 255, 0), bonus_point.rect)
    #     coins.add(bonus_point)

    running = True

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        display.run_display(screen=screen)
            # screen.blit(blue_back, [0,0])
            # print(back)
            # backgorund = background.return_surface(screen=screen)
        player.control()
        camera_group.sprites_draw(player, road=road, mountains=mountains)
        player.movement(screen=screen)
        
        # if player.rect.centery < 840:
        #     player.control(2.0,0.0,2.0)
        # elif player.rect.centery > 1020:
        #     player.control(2.0,2.0,0.0)
        # else:
        #     player.control(2.0,2.0,2.0)

        # # enemy.update_position()
        # # enemy_2.update_position()

        # camera_group.sprites_draw(player)
    
        # if player.rect.center[0] >= 1200 and (enemy.rect.center[0] < 1200 or enemy_2.rect.center[0] < 1200):
        #     font = pygame.font.SysFont("Arial", 60, bold=True)
        #     txtsurf = font.render("You win", True, green)
        #     screen.blit(txtsurf,(600 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
        #     pygame.display.update()
        #     time.sleep(2)
        #     pygame.quit()
        #     exit()

        # if (enemy.rect.center[0] >= 1200 or enemy_2.rect.center[0] >= 1200) and player.rect.center[0] < 1200:

        #     font = pygame.font.SysFont("Arial", 60, bold=True)
        #     txtsurf = font.render("You lose", True, red)
        #     screen.blit(txtsurf,(600 - txtsurf.get_width() // 2, 400 - txtsurf.get_height() // 2))
        #     pygame.display.update()
        #     time.sleep(2)
        #     pygame.quit()
        #     exit()

        # player.collider(bonus_point=coins)

        # pygame.draw.rect(screen, (255, 0, 0), player.rect)
        # screen.blit(background, [0,0])
        # camera_group.sprites_draw(player)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()



