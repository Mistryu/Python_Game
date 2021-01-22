import Enemy
import pygame


class Boss(Enemy.Enemy):
    boss_easy_image = [pygame.image.load('res/Enemies/bosses/Arcane Golem.png')]
    boss_normal_image = [pygame.image.load('res/Enemies/bosses/Boss Darkness Titan Ilnoct.png')]
    boss_hard_image = [pygame.image.load('res/Enemies/bosses/country_ball_boss.png')]

    def __init__(self, x, y, width, height, vel, health, damage):
        super().__init__(x, y, width, height, vel, health, damage)
        self.hitbox = (self.x, self.y, self.width, self.height + 10)
        self.image = self.boss_hard_image

    def draw(self, win):

        if self.not_killed:
            self.hitbox = (self.x + 40, self.y - 10, self.width, self.height)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
            win.blit(self.image[0], (self.x - 35, self.y - 60))

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12, 200, 10))
            pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12,
                                                (self.health * 2), 10))
        else:
            self.dead = True
