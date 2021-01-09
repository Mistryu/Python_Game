import Enemy
import pygame


class Golem(Enemy.Enemy):
    golem_walk_image = (pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_1.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_2.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_3.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_4.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_5.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_6.png'))

    golem_attack_image = (pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 1.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 2.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 3.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 4.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 5.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 6.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 7.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 8.png'),
                          pygame.image.load('res/Enemies/Golem/Golem attack/Golem Attack 9.png'))

    golem_dead_image = (pygame.image.load('res/Enemies/Golem/Golem_dead/Golem_walk_1.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_2.png'),
                        pygame.image.load('res/Enemies/Golem/Golem_move/Golem_walk_3.png'))

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
                win.blit(self.golem_walk_image[self.walk_count // 3], (self.x - 35, self.y - 60))
                self.walk_count += 1
            else:
                win.blit(self.golem_attack_image[self.attack_animation_counter // 3], (self.x - 35, self.y - 60))
                self.attack_animation_counter += 1

            self.hitbox = (self.x - 4, self.y - 15, self.width, self.height + 10)
           # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        elif self.dead_counter <= 8:
            win.blit(self.golem_dead_image[self.dead_counter // 3], (self.x - 35, self.y - 60))
            self.dead_counter += 1
            self.hitbox = (0, 0, 0, 0)
        else:
            self.dead = True

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12, 50, 10))
        pygame.draw.rect(win, (0, 100, 0), (self.hitbox[0] - 10, self.hitbox[1] - 12,
                                            self.health * 10, 10))
