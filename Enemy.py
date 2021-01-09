class Enemy(object):
    def __init__(self, x, y, width, height, vel, health, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = 150
        self.walk_count = 0
        self.vel = vel
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = health
        self.not_killed = True
        self.attack_counter = 0
        self.damage = damage
        self.dead_counter = 0
        self.dead = False
        self.player_damage = 1

    def move(self):
        if self.x + self.vel < self.end:
            self.x += self.vel
        else:
            self.vel = 0

    def hit(self, player_damage):
        if self.health - player_damage > 0:
            self.health -= player_damage
        else:
            self.not_killed = False
