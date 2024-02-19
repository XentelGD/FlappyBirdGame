import pygame


class Object:
    def __init__(self, x, y, width, height, texture):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture = texture
        self.resize(width, height)
        self.start()

    def start(self): ...

    def draw(self, window, clock):
        window.blit(self.texture, (self.x, self.y))
        ...

    def update(self, window, clock):

        ...

    def resize(self, width, height):
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def rotate(self, angle):
        self.texture = pygame.transform.rotate(self.texture, angle)
