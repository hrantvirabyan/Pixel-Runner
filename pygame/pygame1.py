import pygame
from sys import exit
import random
from pygame import mixer


score=0
def display_score():
    time = pygame.time.get_ticks()
    score_surf = test_font.render( f'{score}', False, (64,64,64))
    score_rect = score_surf.get_rect(center  = (400,50))
    screen.blit(score_surf, score_rect)


def p_animation():
    global player_surf, player_index
    if player_rect.bottom<300:
          player_surf = player_jump
    else:
         player_index += 0.2
         if player_index >= len(player_walk):
             player_index = 0
         player_surf = player_walk[int(player_index)]

def s_animation():
    global enemy_surface, enemy_index
    enemy_index += 0.15
    if enemy_index >= len(enemy_move):
        enemy_index = 0
    enemy_surface = enemy_move[int(enemy_index)]

def ground_animation():
    global ground_surface, ground_index
    ground_index += 0.1
    if ground_index >= len(ground_move):
        ground_index = 0
    ground_surface = ground_move[int(ground_index)]


r1 = 2.3
r2 = 70

def cloud_movement1():
    global r1, r2

    cloud1_rect.left -=r1
    cloud1_rect.bottom = 70
    cloud1_rect.bottom += r2
    if cloud1_rect.left < -200:
        r2 = random.randint(-5, 5)
        cloud1_rect.left = 1100

r4 = 50
def cloud_movement2():
    global r1, r4

    cloud2_rect.left -=r1
    cloud2_rect.bottom = 70
    cloud2_rect.bottom +=r4
    if cloud2_rect.left < -200:
        r4 = random.randint(-13, 13)
        cloud2_rect.left = 1100

pygame.init()
mixer.music.load('audio/music.wav')
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock= pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = False

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()

gameover_surface = pygame.image.load("graphics/Gameover.png").convert_alpha()
#score_surface = test_font.render('Score:', False, (64,64,64))
#score_rect = score_surface.get_rect( center  =(400, 50))

#CLOUD
cloud1_surface = pygame.image.load("graphics\Cloud\cloud1.png").convert_alpha()
cloud2_surface = pygame.image.load("graphics\Cloud\cloud2.png").convert_alpha()
cloud2_surface = pygame.transform.rotozoom(cloud2_surface, 0, 0.5)
cloud1_surface = pygame.transform.rotozoom(cloud1_surface, 0, 0.5)

cloud1_rect = cloud1_surface.get_rect(midbottom =(1600, 70))
cloud2_rect = cloud2_surface.get_rect(midbottom =(1100, 50))


#enemy

enemy_1 = pygame.image.load("graphics\enemy\enemy1.png")
enemy_2 = pygame.image.load("graphics\enemy\enemy2.png")
enemy_3 = pygame.image.load("graphics\enemy\enemy3.png")
enemy_4 =pygame.image.load("graphics\enemy\enemy4.png")



enemy_index = 0
enemy_move = [enemy_1, enemy_2, enemy_3, enemy_4]
enemy_surface = enemy_move[enemy_index]
enemy_rect = enemy_surface.get_rect(midbottom =(800, 300))

ground1_surface = pygame.image.load("graphics/ground1.png").convert_alpha()
ground2_surface = pygame.image.load("graphics/ground2.png").convert_alpha()

ground_index = 0
ground_move = [ground1_surface, ground2_surface]
ground_surface = ground_move[ground_index]
ground_rect = ground_surface.get_rect(midbottom =(400, 460))

#player_surf = player_walk[player_index]
#player_rect = player_surf.get_rect(midbottom = (80, 300))
# PLAYER
player_walk1 = pygame.image.load("graphics\Player\walking1.png").convert_alpha()
player_walk1 = pygame.transform.rotozoom(player_walk1, 0, 0.4)

player_walk2 = pygame.image.load("graphics\Player\walking2.png").convert_alpha()
player_walk2 = pygame.transform.rotozoom(player_walk2, 0, 0.4)

player_walk3 = pygame.image.load("graphics\Player\walking3.png").convert_alpha()
player_walk3 = pygame.transform.rotozoom(player_walk3, 0, 0.4)

player_walk= [player_walk1, player_walk2, player_walk3]
player_index = 0

player_jump = player_walk2 = pygame.image.load("graphics\Player\jump.png").convert_alpha()
player_jump = pygame.transform.rotozoom(player_jump, 0, 0.4)

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
#END PLAYER

gameover_surface = pygame.image.load("graphics/Gameover.png").convert_alpha()

player_gravity = 0
enemy_movement_speed = 4

jump_sound = mixer.Sound('audio/jump.wav')
collide_sound = mixer.Sound('audio/collide.wav')


mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        jump_sound.play()
                        player_gravity = -18

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:


                    game_active = True
                    enemy_rect.x = 800

    if game_active:

        screen.blit(sky_surface,(0,0))
        screen.blit(cloud1_surface,cloud1_rect)
        screen.blit(cloud2_surface,cloud2_rect)
        screen.blit(ground_surface,ground_rect)
        ground_animation()
        #pygame.draw.rect(screen, '#c0ecec', score_rect, 10)
        #pygame.draw.rect(screen, '#c0ecec', score_rect, )
        #screen.blit(score_surface,score_rect)
        enemy_rect.left -=enemy_movement_speed
        if enemy_rect.left < -50:
            enemy_rect.left = 850
            score += 1



        cloud_movement1()
        cloud_movement2()
        p_animation()
        s_animation()
        screen.blit(enemy_surface,enemy_rect)

        player_gravity +=0.7
        player_rect.y += player_gravity

        if score >= 5:
            enemy_movement_speed = 8
        if score >= 10:
            enemy_movement_speed = 16
        if score >= 15:
                enemy_movement_speed = 24
        if player_rect.bottom>=300:
            player_rect.bottom=300
        screen.blit(player_surf,player_rect)

        display_score()

    #collision
        if enemy_rect.colliderect(player_rect):
            play_background_music = False
            collide_sound.play()
            score = 0
            game_active = False
            enemy_movement_speed = 4
    else:

        screen.blit(gameover_surface,(0,0))


    pygame.display.update()
    clock.tick(60)
