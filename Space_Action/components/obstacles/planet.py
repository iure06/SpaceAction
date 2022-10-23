from Space_Action.components.obstacles.obstacle import Obstacle
from Space_Action.utils.contants import PLANET
from random import randint


class Planet(Obstacle):
    def __init__(self,score):
        self.image = PLANET
        self.type = randint(0 , 13)
        self.score = score
        super().__init__(self.image,self.type ,self.score)