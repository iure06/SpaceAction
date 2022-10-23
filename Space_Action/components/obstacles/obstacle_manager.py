from random import randint
from Space_Action.components.obstacles.planet import Planet
from Space_Action.components.obstacles.meteor import Meteor


class Obstacle_manage:
    def __init__(self):
        self.obstacles = []

    def update(self,game):
        if len(self.obstacles) == 0:
            obstacleDraw = randint(0,1)

            if obstacleDraw == 0:
                self.obstacles.append(Planet(game))
            elif obstacleDraw == 1:
                self.obstacles.append(Meteor(game))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.ship_rect.colliderect(obstacle.rect):
                game.life -= 1
                self.obstacles.remove(obstacle)

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []