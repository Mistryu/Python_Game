import pygame
import random

import Player
import Projectile
from Slime import Slime
from Owl import Owl
from Golem import Golem
from Demios import Demios
from Clorfos import Clorfos
from Boss import Boss
import Menu

pygame.init()

# Window
wind_width = 950
wind_height = 630
wind = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption("42 Battles")
back_ground = pygame.image.load('res/background.jpg')
# pygame.mixer.music.load("res/music.mp3") # You can add music here
# pygame.mixer.music.play(-1)
my_font = pygame.font.SysFont("monospace", 25, True)

attack_2_image = [pygame.image.load('res/Spell3/BFX003_01.png'), pygame.image.load('res/Spell3/BFX003_02.png'),
                  pygame.image.load('res/Spell3/BFX003_03.png')]

clock = pygame.time.Clock()
player = Player.Player()
menu = Menu.Menu()

wind.blit(back_ground, (0, 0))


# Redrawing window
def redraw_wind():
    wind.blit(back_ground, (0, 0))
    player.draw(wind)
    wall.draw_base_hp()
    menu.draw_text("Base HP: ", my_font, (255, 255, 255), wind, 53, 595)
    menu.draw_text(f"Score: {score}", my_font, (255, 255, 255), wind, 53, 15)
    menu.draw_text(f"Level: {lvl}", my_font, (255, 255, 255), wind, 753, 15)

    if attack1_count >= 20 and attack2_unlocked:
        menu.draw_text("Second Attack: Ready!", my_font, (255, 255, 255), wind, 353, 15)

    for enemy in enemies:
        enemy.draw(wind)
        if lvl == 5 and enemy.__class__ == Clorfos:
            for projectile in enemy.bullets:
                projectile.draw(wind)

    for bull in bullets:
        bull.draw(wind)

    pygame.display.update()


class Wall(object):
    def __init__(self):
        self.x = 200
        self.y = 500
        self.hitbox = (100, 90, 50, 500)
        self.hp = 650

    def draw_base_hp(self):
        pygame.draw.rect(wind, (255, 0, 0), (200, 600, 650, 20))
        pygame.draw.rect(wind, (0, 100, 0), (200, 600, self.hp, 20))


# Game
run = True
attack2_unlocked = False
bullets = []
bullet_vel = 10
enemies = []
shoot_loop = 1
attack1_count = 0
score = 0
enemies_on_map = 0
lvl = 1
spawn_rate = 0
slime_count = 10
owl_count = 0
clorfos_count = 0
demios_count = 0
golem_count = 0
boss_count = 0
difficulty_increase = 1  # Increases the amount of enemies
enemy_count = slime_count + owl_count + clorfos_count + demios_count + golem_count + boss_count
wall = Wall()

while run:
    clock.tick(25)

    if menu.menu_run:
        menu.run_menu()
    if wall.hp <= 0:
        menu.menu_run = True
        wall.hp = 650

    # New game difficulty
    if menu.new_game:
        score = 0
        wall.hp = 650
        slime_count = 10
        owl_count = 0
        clorfos_count = 0
        demios_count = 0
        golem_count = 0
        boss_count = 0
        enemy_count = 10
        lvl = 1
        enemies.clear()
        bullets.clear()
        
        if menu.lvl_difficulty == 1:
            menu.new_game = False
            difficulty_increase = 1

        elif menu.lvl_difficulty == 2:
            menu.new_game = False
            difficulty_increase = 1.5

        else:
            menu.new_game = False
            difficulty_increase = 2

    # Spawner
    if spawn_rate == 0:
        if not slime_count <= 0:
            enemies.append(Slime(1000, random.randint(100, 500), 30, 50, 3, 2, 2))
            slime_count -= 1
            enemies_on_map += 1

        if not owl_count <= 0:
            enemies.append(Owl(1000, random.randint(100, 500), 30, 50, 5, 2, 2))
            owl_count -= 1
            enemies_on_map += 1

        if not golem_count <= 0:
            enemies.append(Golem(1000, random.randint(100, 500), 30, 50, 2, 5, 4))
            golem_count -= 1
            enemies_on_map += 1

        if not demios_count <= 0:
            enemies.append(Demios(1000, random.randint(100, 500), 30, 50, 2, 8, 5))
            demios_count -= 1
            enemies_on_map += 1

        if lvl == 5 and clorfos_count != 0:
            enemies.append(Clorfos(600, (25 + clorfos_count * 150), 30, 120, 2, 50, 0.5))
            clorfos_count -= 1
            enemies_on_map += 1

        if lvl == 5 and boss_count == 1:
            boss = Boss(700, 250, 30, 200, 2, 100, 2)

            if menu.lvl_difficulty == 1:
                boss.image = boss.boss_easy_image
            elif menu.lvl_difficulty == 2:
                boss.image = boss.boss_normal_image
            else:
                boss.image = boss.boss_normal_image

            enemies.append(boss)
            enemies_on_map += 1
            boss_count = 0

        spawn_rate += 1
    # Spawn speed limit

    elif spawn_rate != 130:
        spawn_rate += 1
    elif spawn_rate == 130:
        spawn_rate = 0

    if 0 < shoot_loop <= 3:
        shoot_loop += 1
    elif shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Player Bullet
    for bul in bullets:
        for enem in enemies:
            if bul.y - bul.radius < enem.hitbox[1] + enem.hitbox[3] and bul.y + bul.radius > enem.hitbox[1] \
                    and enem.not_killed:
                if bul.x - bul.radius < enem.hitbox[0] + enem.hitbox[2] and bul.x + bul.radius > enem.hitbox[0]:

                    # If bullet hit the enemy
                    enem.hit(player.player_damage)
                    if bul in bullets and (bul.vel != 40 or bul.x >= 900):
                        bullets.remove(bul)

                    if not enem.not_killed:
                        score += 1
                        enemies_on_map -= enemies_on_map
                        enemy_count -= 1
                        if enem.dead:
                            enemies.remove(enem)
                            break

        if wind_width > bul.x > 0:
            bul.x += bul.vel

        elif bul in bullets:
            bullets.remove(bul)
            break

    # Enemy attack
    for enem in enemies:
        if enem.x <= enem.end and enem.not_killed:
            if enem.attack_counter == 0:
                wall.hp -= enem.damage
                enem.attack_counter += 1
            elif enem.attack_counter != 30:
                enem.attack_counter += 1
            else:
                enem.attack_counter = 0

        # Clorfos attack
        if lvl == 5 and enem.__class__ == Clorfos and enem.not_killed:
            for bul in enem.bullets:
                if bul.x <= 150:
                    if bul in enem.bullets:
                        enem.bullets.remove(bul)
                        wall.hp -= enem.damage
                else:
                    bul.x += bul.vel

    # Next lvl
    if enemy_count == 0:
        lvl += 1
        if lvl == 2:            # TODO: make a function so you DRY
            slime_count = 4 * difficulty_increase
            owl_count = 6 * difficulty_increase
            bullet_vel = 20
            golem_count = 0
            enemy_count = slime_count + owl_count + clorfos_count + demios_count + golem_count + boss_count

        elif lvl == 3:
            player.player_damage = 2
            slime_count = 4 * difficulty_increase
            owl_count = 6 * difficulty_increase
            golem_count = 6 * difficulty_increase
            enemy_count = slime_count + owl_count + clorfos_count + demios_count + golem_count + boss_count

        elif lvl == 4:
            attack2_unlocked = True
            slime_count = 0
            owl_count = 2 * difficulty_increase
            golem_count = 2 * difficulty_increase
            demios_count = 4 * difficulty_increase
            enemy_count = slime_count + owl_count + clorfos_count + demios_count + golem_count + boss_count

        elif lvl == 5:
            player.player_damage = 3
            slime_count = 2 * difficulty_increase
            owl_count = 2 * difficulty_increase
            golem_count = 4 * difficulty_increase
            demios_count = 4 * difficulty_increase
            clorfos_count = 3
            boss_count = 1
            enemy_count = slime_count + owl_count + clorfos_count + demios_count + golem_count + boss_count
        else:
            menu.menu_run = True

    keys = pygame.key.get_pressed()

    # Event handler
    if not player.attack1 and not player.attack2:
        if keys[pygame.K_UP] and player.y > 90:
            player.y -= player.vel
            player.standing = False

        elif keys[pygame.K_DOWN] and player.y < wind_height - player.width - 40:
            player.y += player.vel
            player.standing = False

        elif keys[pygame.K_SPACE]:
            attack1_count += 1
            player.attack1 = True
            player.standing = True

        elif keys[pygame.K_z] and attack2_unlocked:
            player.attack2 = True
            player.standing = True

        elif keys[pygame.K_p]:
            menu.menu_run = not menu.menu_run

        else:
            walk_count = 0
            player.standing = True

    # Player 1 attack activation
    elif shoot_loop == 0 and player.attacking_count == 13 and player.attack1:
        bullet = Projectile.Projectile(player.x + player.width / 2 + 45,
                                       player.y + player.height / 2 - 20,
                                       4, (3, 53, 252), bullet_vel, player.player_damage, 12)
        bullets.append(bullet)
        shoot_loop = 1
        attack1_count += 1

    # Player 2 attack activation
    elif shoot_loop == 0 and player.attacking_count == 13 and player.attack2 and attack1_count >= 20:
        bullet = Projectile.Projectile(player.x + player.width / 2 + 45,
                                       player.y + player.height / 2 - 20,
                                       10, (3, 53, 252), 40, player.player_damage * 3, 12)
        bullet.spell_image = attack_2_image
        bullet.magic_count_speed = 8
        bullets.append(bullet)
        shoot_loop = 1
        attack1_count = 0

    else:
        if player.attacking_count == 23:
            player.attack1 = False
            player.attack2 = False

    redraw_wind()


pygame.quit()
