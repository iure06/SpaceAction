from time import sleep
import pygame
from Space_Action.components.obstacles.obstacle_manager import Obstacle_manage
from Space_Action.components.ship import Ship
from Space_Action.utils.contants import (BG, FONT_STYLE, FPS, HEART,
                                         SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, SOUNDTRACK)


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 15
        self.x_pos_bg = -50
        self.y_pos_bg = 0
        self.score = 0
        self.life = 5

        self.player = Ship()
        self.obstacle_manager = Obstacle_manage()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            if self.life == 0:
                self.playing = False
                pygame.mixer.music.pause()
                self.execute()

            self.events()
            self.update()
            self.draw()
                
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.update_life()

    def update_score(self):
        self.text_format(f"Score: {self.score}", 1100, 30,20, "#FF0000")

    def update_life(self):
        posicion = 20
        for life in range(0 , self.life):
            self.screen.blit(HEART,(posicion, self.y_pos_bg + 10))
            posicion += 40

    def draw(self):
        self.clock.tick(FPS)
        self.screen.blit(BG,(self.x_pos_bg,self.y_pos_bg))
        self.update_score()
        self.update_life()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip() 

    def show_menu(self):
        self.screen.fill("#FFFFFF")
        if self.life == 5:
            self.text_format('Press any key to start', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        elif self.life == 0:
            self.text_format('Gamer Over', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50)
            self.text_format('Press any key to start', SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50 / 2)
            
        
        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.life = 5
                self.score = 0
                self.play_music()
                self.run()

    def play_music(self):
        pygame.mixer.music.load(SOUNDTRACK)
        pygame.mixer_music.play(-1)

    def text_format(self, content, screen_x, screen_y,size = 30 , color = "#000000"):
        font = pygame.font.Font(FONT_STYLE,size)
        text = font.render(content, True, color)
        text_rect = text.get_rect()
        text_rect.center = (screen_x, screen_y)
        self.screen.blit(text, text_rect)