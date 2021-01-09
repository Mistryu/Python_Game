import pygame


class Menu:

    fox_image = [pygame.image.load('res/Menu_icons/fox1.png'), pygame.image.load('res/Menu_icons/fox2.png'),
                 pygame.image.load('res/Menu_icons/fox3.png'), ]
    country_ball_image = pygame.image.load('res/Menu_icons/country_ball.png')

    def __init__(self):
        self.width = 950
        self.height = 630
        self.menu_run = True
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.font1 = pygame.font.SysFont("monospace", 50, True)
        self.font2 = pygame.font.SysFont("monospace", 25, True)
        self.font3 = pygame.font.SysFont("monospace", 35, True)
        self.font4 = pygame.font.SysFont("monospace", 20, True)
        self.click = False
        self.lvl_choice = False
        self.base_hp = 650
        self.lvl_difficulty = 1
        self.fox_count = 0
        self.new_game = False

    def draw_text(self, text, font, color, surface, x, y):
        textob = font.render(text, 1, color)
        text_rect = textob.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(textob, text_rect)

    def run_menu(self):
        while self.menu_run:
            self.screen.fill((59, 58, 57))
            self.draw_text("Hello World", self.font1, (255, 255, 255), self.screen, 300, 70)
            self.draw_text("Creator:", self.font2, (255, 255, 255), self.screen, 95, 70)
            self.draw_text("Guy that helped", self.font2, (255, 255, 255), self.screen, 700, 70)
            self.draw_text("Mistryu", self.font4, (255, 255, 255), self.screen, 109, 115)
            self.draw_text("Polish Tortoise", self.font4, (255, 255, 255), self.screen, 720, 115)

            if self.fox_count + 1 >= 162:
                self.fox_count = 0
            else:
                self.fox_count += 1

            self.screen.blit(self.fox_image[self.fox_count // 54], (100, 150))
            self.screen.blit(self.country_ball_image, (750, 150))

            mouse_x, mouse_y = pygame.mouse.get_pos()

            button_1 = pygame.Rect(350, 200, 230, 60)
            button_2 = pygame.Rect(350, 300, 230, 60)
            button_3 = pygame.Rect(350, 400, 230, 60)

            if self.lvl_choice:
                button_ez = pygame.Rect(600, 230, 230, 60)
                button_nr = pygame.Rect(600, 300, 230, 60)
                button_hr = pygame.Rect(600, 370, 230, 60)
                pygame.draw.rect(self.screen, (33, 33, 32), button_ez)
                pygame.draw.rect(self.screen, (33, 33, 32), button_nr)
                pygame.draw.rect(self.screen, (33, 33, 32), button_hr)
                self.draw_text("Easy", self.font3, (255, 255, 255), self.screen, 670, 240)
                self.draw_text("Normal", self.font3, (255, 255, 255), self.screen, 650, 310)
                self.draw_text("Hard", self.font3, (255, 255, 255), self.screen, 670, 380)

                if button_ez.collidepoint((mouse_x, mouse_y)) and self.click:
                    self.lvl_difficulty = 1
                    self.lvl_choice = False
                    self.new_game = True
                    self.menu_run = not self.menu_run

                elif button_nr.collidepoint((mouse_x, mouse_y)) and self.click:
                    self.lvl_difficulty = 2
                    self.lvl_choice = False
                    self.new_game = True
                    self.menu_run = not self.menu_run

                elif button_hr.collidepoint((mouse_x, mouse_y)) and self.click:
                    self.lvl_difficulty = 3
                    self.lvl_choice = False
                    self.new_game = True
                    self.menu_run = not self.menu_run

            if button_1.collidepoint((mouse_x, mouse_y)) and self.click:
                self.menu_run = not self.menu_run

            elif button_2.collidepoint((mouse_x, mouse_y)) and self.click:
                self.lvl_choice = True

            elif button_3.collidepoint((mouse_x, mouse_y)) and self.click:
                pygame.quit()

            pygame.draw.rect(self.screen, (33, 33, 32), button_1)
            pygame.draw.rect(self.screen, (33, 33, 32), button_2)
            pygame.draw.rect(self.screen, (33, 33, 32), button_3)
            self.draw_text("Continue", self.font3, (255, 255, 255), self.screen, 375, 210)
            self.draw_text("New Game", self.font3, (255, 255, 255), self.screen, 375, 310)
            self.draw_text("Exit", self.font3, (255, 255, 255), self.screen, 420, 410)

            self.click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.click = True

            pygame.display.update()

