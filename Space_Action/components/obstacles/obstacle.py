import pygame
from pygame.sprite import Sprite
from Space_Action.utils.contants import SCREEN_WIDTH
from random import randint


class Obstacle(Sprite):
    def __init__(self, image,type,game):
        self.image = image
        self.type = type
        self.game = game
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = randint(200,500)

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < - self.rect.width:
            self.game.score -= 2
            obstacles.pop()

    def draw(self,screen):
        screen.blit(self.image[self.type],(self.rect.x,self.rect.y) )
