import pygame


class Projectile(object):

    spell_image = [pygame.image.load('res/Spell/FB001.png'), pygame.image.load('res/Spell/FB002.png'),
                   pygame.image.load('res/Spell/FB003.png'), pygame.image.load('res/Spell/FB004.png'),
                   pygame.image.load('res/Spell/FB005.png')]

    # Facing can be used for increasing velocity
    def __init__(self, x, y, radius, color, vel, damage, magic_count_speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = vel
        self.magic_count = 0
        self.damage = damage
        self.magic_count_speed = magic_count_speed

    def draw(self, win):
        if self.magic_count >= self.magic_count_speed:
            self.magic_count = 0
        else:
            self.magic_count += 1

        # pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        win.blit(self.spell_image[self.magic_count // 3], (self.x - 40, self.y - 15))

