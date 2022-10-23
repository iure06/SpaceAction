from Space_Action.components.obstacles.obstacle import Obstacle
from random import randint
from Space_Action.utils.contants import METEOR


class Meteor(Obstacle):
    def __init__(self,game):
        self.image = METEOR
        self.type = randint(0,1)
        super().__init__(self.image,self.type,game)