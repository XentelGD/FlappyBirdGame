import object
import pygame

import settings
import tools


class Bird(object.Object):

    def __init__(self, x, y, width, height, texture):
        self.gravity = 0
        self.speed_y = 0

        super().__init__(x, y, width, height, texture)

        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 10)

    def start(self):
        self.speed_y = 0
        self.gravity = settings.GRAVITY

    def jump(self, size):
        self.speed_y = -size

    def draw(self, window, clock):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 10)

        window.blit(self.texture, (self.x, self.y))

    def update(self, window, clock):

        delta_time = 0
        try:
            delta_time = 120 / clock.get_fps()
        except:
            ...

        if self.y + self.height > settings.HEIGHT and not tools.is_clicked:
            self.speed_y = 0

        if self.y < 0:
            self.speed_y = 2

        self.y += self.speed_y * delta_time
        self.speed_y += self.gravity * delta_time


