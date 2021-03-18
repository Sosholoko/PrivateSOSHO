import pygame
import math
from jeu import Game
pygame.init()


pygame.display.set_caption("Fall Game")
screen = pygame.display.set_mode((1080, 720))


background = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/bg game.jpg')

banner = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/banner.png')
banner = pygame.transform.scale(banner, (550, 550))


play_button = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/start button.png')
play_button = pygame.transform.scale(play_button, (400, 300))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
#load game 

game = Game()


running = True

while running:

    #background
    screen.blit(background, (0, 0))

    #check if game has started yet

    if game.is_playing:
        #trigger instructions of game
        game.update(screen)
    else:
        screen.blit(banner, (245, 5))
        screen.blit(play_button, (play_button_rect))





    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #keyborad keys event
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_fire()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check if the button is clicked
            if play_button_rect.collidepoint(event.pos):
                game.start()