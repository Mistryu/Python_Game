import Enemy
import pygame


class Demios(Enemy.Enemy):
    demios_walk_image = (pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 1.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 2.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 3.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 4.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 5.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 6.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 7.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 8.png'),
                         pygame.image.load('res/Enemies/Demios/Demios Move/Demios Move 9.png'))

    demios_attack_image = (pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 1.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 2.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 3.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 4.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 5.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 6.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 7.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 8.png'),
                           pygame.image.load('res/Enemies/Demios/Demios_attack/Demios Growl 9.png'))

    demios_dead_image = (pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_1.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_2.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_3.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_4.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_5.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_6.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_7.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_8.png'),
                         pygame.image.load('res/Enemies/Demios/Demios_dead/Demios_dead_9.png'))

    def __init__(self, x, y, width, height, vel, health, damage):
        super().__init__(x, y, width, height, vel, health, damage)
        self.hitbox = (self.x, self.y, self.width, self.height + 10)
        self.attack_animation_counter = 0

    def draw(self, win):

        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.attack_animation_counter + 1 >= 27:
            self.attack_animation_counter = 0

        if self.not_killed:
            if self.x > self.end:
                self.x -= self.vel
                win.blit(self.demios_walk_image[self.walk_count // 3], (self.x - 35, self.y - 60))
                self.walk_count += 1
            else:
                win.blit(self.demios_attack_image[self.attack_animation_counter // 3], (self.x - 35, self.y - 60))
                self.attack_animation_counter += 1

            self.hitbox = (self.x - 4, self.y - 15, self.width, self.height + 10)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        elif self.dead_counter <= 26:
            win.blit(self.demios_dead_image[self.dead_counter // 3], (self.x - 35, self.y - 60))
            self.dead_counter += 1
            self.hitbox = (0, 0, 0, 0)
        else:
            self.dead = True

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12, 50, 10))
        pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12,
                                            self.health * 6.5, 10))
