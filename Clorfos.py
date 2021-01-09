import Enemy
import pygame
import Projectile


class Clorfos(Enemy.Enemy):
    clorfos_walk_image = (pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 1.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 2.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 3.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 4.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 5.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 6.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 7.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 8.png'),
                          pygame.image.load('res/Enemies/Clorfos/Clorfos Attack/Clorfos Attack 9.png'))

    spell_image = [pygame.image.load('res/Spell2/I5050-1.png'), pygame.image.load('res/Spell2/I5050-2.png'),
                   pygame.image.load('res/Spell2/I5050-3.png'), pygame.image.load('res/Spell2/I5050-4.png'),
                   pygame.image.load('res/Spell2/I5050-5.png'), pygame.image.load('res/Spell2/I5050-6.png'),
                   pygame.image.load('res/Spell2/I5050-7.png'), pygame.image.load('res/Spell2/I5050-8.png'),
                   pygame.image.load('res/Spell2/I5050-9.png'), pygame.image.load('res/Spell2/I5050-10.png'),
                   pygame.image.load('res/Spell2/I5050-11.png')]

    def __init__(self, x, y, width, height, vel, health, damage):
        super().__init__(x, y, width, height, vel, health, damage)
        self.hitbox = (self.x, self.y, self.width, self.height + 10)
        self.attack_animation_counter = 30
        self.shoot_loop = 1
        self.bullets = []

    def draw(self, win):
        if self.attack_animation_counter + 1 >= 81:
            self.attack_animation_counter = 0

        if self.not_killed:
            win.blit(self.clorfos_walk_image[self.attack_animation_counter // 9], (self.x - 35, self.y - 60))
            self.attack_animation_counter += 1

            self.hitbox = (self.x - 4, self.y - 40, self.width, self.height + 10)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12, 50, 10))
            pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12,
                                                self.health, 10))
        else:
            self.dead = True

        self.attack()

    def move(self):
        pass

    def attack(self):
        if self.shoot_loop >= 81:
            self.shoot_loop = 0

        if self.shoot_loop == 0 and not self.dead:
            bul = Projectile.Projectile(round(self.x + self.width // 2 - 15),
                                        round(self.y + self.height // 2 - 85),
                                        4, (3, 53, 252), -30, 5, 32)
            bul.spell_image = self.spell_image
            bul.magic_count_speed = 32
            self.bullets.append(bul)
            self.shoot_loop += 1

        else:
            self.shoot_loop += 1
