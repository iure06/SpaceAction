import pygame
from pygame.sprite import Sprite
from Space_Action.utils.contants import SHIP


class Ship(Sprite):
    def __init__(self):
        self.image = SHIP
        self.ship_rect = self.image.get_rect()
        self.ship_rect.x = 80
        self.ship_rect.y = 200
        self.shipUp = False
        self.shipDown = False
        self.shipShot = False

    def update(self, user_input):
        if self.shipUp:
            self.ship_up()
        elif self.shipDown:
            self.ship_down()
        elif self.shipShot:
            self.ship_shot()

        if user_input[pygame.K_UP] and not self.shipDown:
            self.shipUp = True
            self.shipDown = False
            self.shipShot = False
        elif user_input[pygame.K_DOWN] and not self.shipUp:
            self.shipUp = False
            self.shipDown = True
            self.shipShot = False
        elif user_input[pygame.K_SPACE]:
            self.shipUp = False
            self.shipDown = False
            self.shipShot = True


    def ship_up(self):
        if self.ship_rect.y >  0:
            self.ship_rect.y -= 5
        self.shipUp = False

    def ship_down(self):
        if self.ship_rect.y < 390:
            self.ship_rect.y += 5
        self.shipDown = False

    def ship_shot(self):
        pass

    def draw(self,screen):
        screen.blit(self.image, (self.ship_rect.x, self.ship_rect.y))
