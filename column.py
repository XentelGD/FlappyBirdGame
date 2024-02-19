import pygame
import settings
import tools
import object


class Column(object.Object):
    def __init__(self, x, y, width, height, texture, texture2):
        super().__init__(x, y, width, height, texture)

        self.texture = pygame.transform.scale(texture, (width, height))
        self.texture2 = pygame.transform.scale(texture2, (width, height))

        self.hitbox1 = (self.x, self.y - 500, self.width, self.height)
        self.hitbox2 = (self.x, self.y + 500, self.width, self.height)

        self.can_give_score = True
        ...

    def draw(self, window, clock):
        window.blit(self.texture, (self.x, self.y - 500))
        window.blit(self.texture2, (self.x, self.y + 500))

        self.hitbox1 = (self.x, self.y - 500, self.width, self.height)
        self.hitbox2 = (self.x, self.y + 500, self.width, self.height)


    def update(self, window, clock):



        delta_time = 0
        try:
            delta_time = 120 / clock.get_fps()
        except:
            ...

        self.x -= settings.SPEED * delta_time

    def collide_rect(self, rect):

        rect1 = pygame.rect.Rect(rect[0], rect[1], rect[2], rect[3])
        hitbox1_ = pygame.rect.Rect(self.hitbox1[0], self.hitbox1[1], self.hitbox1[2], self.hitbox1[3])
        hitbox2_ = pygame.rect.Rect(self.hitbox2[0], self.hitbox2[1], self.hitbox2[2], self.hitbox2[3])

        if hitbox1_.colliderect(rect1) or hitbox2_.colliderect(rect1):
            return True
        return False
