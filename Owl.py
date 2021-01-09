import Enemy
import pygame


class Owl(Enemy.Enemy):
    owl_walk_image = (pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_1.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_2.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_3.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_4.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_5.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_6.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_7.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_8.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_walk/owl_walk_9.png'))

    owl_attack_image = (pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_1.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_2.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_3.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_4.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_5.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_6.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_7.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_8.png'),
                        pygame.image.load('res/Enemies/Owl/Owl_attack/owl_attack_9.png'))

    owl_dead_image = (pygame.image.load('res/Enemies/Owl/Owl_dead/owl_dead_1.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_dead/owl_dead_2.png'),
                      pygame.image.load('res/Enemies/Owl/Owl_dead/owl_dead_3.png'))

    def __init__(self, x, y, width, height, vel, health, damage):
        super().__init__(x, y, width, height, vel, health, damage)
        self.hitbox = (self.x, self.y, self.width, self.height + 10)
        self.attack_animation_counter = 0

    def draw(self, win):

        if self.walk_count + 1 >= 18:
            self.walk_count = 0
        if self.attack_animation_counter + 1 >= 27:
            self.attack_animation_counter = 0

        if self.not_killed:
            if self.x > self.end:
                self.x -= self.vel
                win.blit(self.owl_walk_image[self.walk_count // 2], (self.x - 35, self.y - 60))
                self.walk_count += 1
            else:
                win.blit(self.owl_attack_image[self.attack_animation_counter // 3], (self.x - 35, self.y - 60))
                self.attack_animation_counter += 1

            self.hitbox = (self.x - 4, self.y - 15, self.width, self.height + 10)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        elif self.dead_counter <= 8:
            win.blit(self.owl_dead_image[self.dead_counter // 3], (self.x - 35, self.y - 60))
            self.dead_counter += 1
            self.hitbox = (0, 0, 0, 0)
        else:
            self.dead = True

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12, 50, 10))
        pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12,
                                            self.health * 25, 10))
