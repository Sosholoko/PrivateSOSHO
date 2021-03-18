import pygame

#fireball class

class Fireball(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('/Users/sashakharoubi/Downloads/Portofolio Sasha/Game/image/massage-ball.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 10
        self.origin_img = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_img, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_fireball.remove(self)

    
    def move(self):
        self.rect.x += self.velocity + 1
        self.rotate()

        #check if fireball is colliding with monster
        for monster in self.player.jeu.check_coll(self, self.player.jeu.all_monsters):
            self.remove()
            monster.damage(self.player.attack)


        #check if fireball is out of screen
        if self.rect.x > 1080:
            self.remove()
