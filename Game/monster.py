import pygame 
import random


#create a class to set monsters

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 0.2
        self.image = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/ennemy.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 505
        self.velocity = random.randint(1, 2)


    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            #make him reappear as new
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

            #check if event bar is loaded
            if self.jeu.comet_event.is_full_loaded():
                self.jeu.all_monsters.remove(self)

                self.jeu.comet_event.attempt_fall()



    def update_health_bar(self, surface):
        #draw health bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 10, self.rect.y - 13, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 10, self.rect.y - 13, self.health, 5])
        

    def forward(self):
        if not self.jeu.check_coll(self, self.jeu.all_players):
            self.rect.x -= self.velocity
        else:
            self.jeu.player.damage_player(self.attack)



# class Piggy(Monster):
#     def __init__(self, jeu):
#             super().__init__(jeu, "piggy")

