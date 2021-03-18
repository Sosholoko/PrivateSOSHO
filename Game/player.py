import pygame
from fireball import Fireball



class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 3
        self.all_fireball = pygame.sprite.Group()
        self.image = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/player 2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 490


    def damage_player(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.jeu.game_over()



    def update_health_bar(self, surface):
        #draw health bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 10, self.rect.y - 13, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 10, self.rect.y - 13, self.health, 5])


    def launch_fire(self):
        self.all_fireball.add(Fireball(self))


    def move_right(self):
        #can move only if its not colliding with an ennemy
        if not self.jeu.check_coll(self, self.jeu.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity