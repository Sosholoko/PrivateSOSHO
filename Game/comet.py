import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        #define image of comet
        self.image = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = 3
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #check if comets number is 0
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.jeu.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity
        #check if the comet fall on the ground
        if self.rect.y >= 500:
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.jeu.check_coll(self, self.comet_event.jeu.all_players):
            print("j t")
            self.remove()
            self.comet_event.jeu.player.damage_player(20)