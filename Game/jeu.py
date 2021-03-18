import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
# from monster import Piggy

class Game:

    
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #comet initialization
        self.comet_event = CometFallEvent(self)
        #monster groups
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, screen):
        #player image
        screen.blit(self.player.image, self.player.rect)

        #update hp bar of players
        self.player.update_health_bar(screen)

        #update event bar
        self.comet_event.update_bar(screen)


        for fireball in self.player.all_fireball:
            fireball.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_fireball.draw(screen)

        self.all_monsters.draw(screen)

        self.comet_event.all_comets.draw(screen)

        #verify if player wants to go left or right
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_coll(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)