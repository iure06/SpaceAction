import os

import pygame

pygame.mixer.init()
# Global Constants
TITLE = 'Space Action'
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
FPS = 30
WAY = os.path.join(os.path.dirname(__file__), "..","assets")

# Assets Constants
BG = pygame.image.load(os.path.join(WAY, "others/background.jpg"))
HEART = pygame.image.load(os.path.join(WAY, "others/heart.png"))

# Assets Constants obstacles
METEOR = [
    pygame.image.load(os.path.join(WAY, "obstacles/meteor/meteor1.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/meteor/meteor2.png"))
]

METEOR_SHOWER = [
    pygame.image.load(os.path.join(WAY, "obstacles/meteorShower/meteorShower1.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/meteorShower/meteorShower2.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/meteorShower/meteorShower1.png"))
]

PLANET = [
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet0.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet1.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet2.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet3.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet4.png")),
    pygame.image.load(os.path.join(WAY,"obstacles/planet/planet5.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet6.png")),
    pygame.image.load(os.path.join(WAY,"obstacles/planet/planet7.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet8.png")),
    pygame.image.load(os.path.join(WAY,"obstacles/planet/planet9.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet10.png")),
    pygame.image.load(os.path.join(WAY,"obstacles/planet/planet11.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet12.png")),
    pygame.image.load(os.path.join(WAY, "obstacles/planet/planet13.png"))
]

# Assets Constants ship
SHIP = pygame.image.load(os.path.join(WAY, "ship/ship.png"))

# Assets Constants weapons
BOMB = pygame.image.load(os.path.join(WAY, "weapons/bomb.png"))

LEISURE_SHOOTING = pygame.image.load(os.path.join(WAY, "weapons/leisureShooting.png"))

# Assets Constants music and songs
SOUNDTRACK = os.path.join(WAY, "others/SoundTrack.mp3")

# Assets Constants font
FONT_STYLE = os.path.join(WAY, "others/Silkscreen-Regular.ttf")