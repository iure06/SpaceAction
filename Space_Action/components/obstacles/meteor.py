from Space_Action.components.obstacles.obstacle import Obstacle
from random import randint
from Space_Action.utils.contants import METEOR


class Meteor(Obstacle):
    def __init__(self,score):
        self.image = METEOR
        self.type = randint(0,1)
        self.score = score
        super().__init__(self.image,self.type,self.score)