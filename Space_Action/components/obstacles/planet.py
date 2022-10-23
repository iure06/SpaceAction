from Space_Action.components.obstacles.obstacle import Obstacle
from Space_Action.utils.contants import PLANET
from random import randint


class Planet(Obstacle):
    def __init__(self,game):
        self.image = PLANET
        self.type = randint(0 , 13)
        super().__init__(self.image,self.type,game)