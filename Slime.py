import Enemy
import pygame


class Slime(Enemy.Enemy):
    slime_walk_image = (pygame.image.load('res/Enemies/Slime/Slime_walk/slime_walk_1.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_walk/slime_walk_2.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_walk/slime_walk_3.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_walk/slime_walk_4.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_walk/slime_walk_5.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_walk/slime_walk_6.png'))

    slime_attack_image = (pygame.image.load('res/Enemies/Slime/Slime_attack/slime_attack_1.png'),
                          pygame.image.load('res/Enemies/Slime/Slime_attack/slime_attack_2.png'),
                          pygame.image.load('res/Enemies/Slime/Slime_attack/slime_attack_3.png'))

    slime_dead_image = (pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_1.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_2.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_3.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_4.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_5.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_6.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_7.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_8.png'),
                        pygame.image.load('res/Enemies/Slime/Slime_dead/slime_dead_9.png'))

    def __init__(self, x, y, width, height, vel, health, damage):
        super().__init__(x, y, width, height, vel, health, damage)
        self.hitbox = (self.x, self.y, self.width, self.height + 10)
        self.attack_animation_counter = 0

    def draw(self, win):

        if self.walk_count + 1 >= 18:
            self.walk_count = 0

        if self.attack_animation_counter + 1 >= 18:
            self.attack_animation_counter = 0

        if self.not_killed:
            if self.x > self.end:
                self.x -= self.vel
                win.blit(self.slime_walk_image[self.walk_count // 3], (self.x - 35, self.y - 60))
                self.walk_count += 1

            else:
                win.blit(self.slime_attack_image[self.attack_animation_counter // 6], (self.x - 35, self.y - 60))
                self.attack_animation_counter += 1

            self.hitbox = (self.x, self.y + 10, self.width, self.height)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        # dead animation
        elif self.dead_counter <= 26:
            win.blit(self.slime_dead_image[self.dead_counter // 3], (self.x - 35, self.y - 60))
            self.dead_counter += 1
            self.hitbox = (0, 0, 0, 0)
        else:
            self.dead = True

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12, 50, 10))
        pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12,
                                            25 * self.health, 10))
