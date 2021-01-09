import pygame


class Player(object):

    # Loading images
    idle_image = [pygame.image.load('res/Player/Idle/idle1.png'), pygame.image.load('res/Player/Idle/idle2.png'),
                  pygame.image.load('res/Player/Idle/idle3.png'), pygame.image.load('res/Player/Idle/idle4.png'),
                  pygame.image.load('res/Player/Idle/idle5.png'), pygame.image.load('res/Player/Idle/idle6.png')]
    walk_image = [pygame.image.load('res/Player/Run/run1.png'), pygame.image.load('res/Player/Run/run2.png'),
                  pygame.image.load('res/Player/Run/run3.png'), pygame.image.load('res/Player/Run/run4.png'),
                  pygame.image.load('res/Player/Run/run5.png'), pygame.image.load('res/Player/Run/run6.png'),
                  pygame.image.load('res/Player/Run/run7.png'), pygame.image.load('res/Player/Run/run8.png')]
    attack1_image = [pygame.image.load('res/Player/Attack1/attack1.1.png'),
                     pygame.image.load('res/Player/Attack1/attack1.2.png'),
                     pygame.image.load('res/Player/Attack1/attack1.3.png'),
                     pygame.image.load('res/Player/Attack1/attack1.4.png'),
                     pygame.image.load('res/Player/Attack1/attack1.5.png'),
                     pygame.image.load('res/Player/Attack1/attack1.6.png'),
                     pygame.image.load('res/Player/Attack1/attack1.7.png'),
                     pygame.image.load('res/Player/Attack1/attack1.8.png')]
    attack2_image = [pygame.image.load('res/Player/Attack2/attack2.1.png'),
                     pygame.image.load('res/Player/Attack2/attack2.2.png'),
                     pygame.image.load('res/Player/Attack2/attack2.3.png'),
                     pygame.image.load('res/Player/Attack2/attack2.4.png'),
                     pygame.image.load('res/Player/Attack2/attack2.5.png'),
                     pygame.image.load('res/Player/Attack2/attack2.6.png'),
                     pygame.image.load('res/Player/Attack2/attack2.7.png'),
                     pygame.image.load('res/Player/Attack2/attack2.8.png')]

    def __init__(self):
        self.x = 18
        self.y = 350
        self.width = 90
        self.height = 100
        self.vel = 7
        self.walk_count = 0
        self.standing = True
        self.standing_count = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.attack1 = False
        self.attack2 = False
        self.attacking_count = 0
        self.player_damage = 1

    def draw(self, win):
        if self.walk_count + 1 >= 24:
            self.walk_count = 0

        if self.standing_count >= 16:
            self.standing_count = 0

        if self.attacking_count >= 24:
            self.attacking_count = 0

        if not self.standing:
            win.blit(self.walk_image[self.walk_count // 3], (self.x - 65, self.y - 47))
            self.walk_count += 1

        elif self.standing and self.attack1:
            win.blit(self.attack1_image[self.attacking_count // 3], (self.x - 65, self.y - 47))
            self.attacking_count += 1

        elif self.standing and self.attack2:
            win.blit(self.attack2_image[self.attacking_count // 3], (self.x - 65, self.y - 47))
            self.attacking_count += 1

        else:
            win.blit(self.idle_image[self.standing_count // 3], (self.x - 65, self.y - 47))
            self.standing_count += 1

#        self.hitbox = (self.x, self.y, self.width - 15, self.height - 3)
#        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


