import pygame
import random
import os

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))


class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP_IMG = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM_IMG = PIPE_IMG

        self.end = x + self.PIPE_TOP_IMG.get_width()
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP_IMG.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL
        self.end = self.x + self.PIPE_TOP_IMG.get_width()

    def draw(self, win):
        win.blit(self.PIPE_TOP_IMG, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM_IMG, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP_IMG)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM_IMG)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        t_point = bird_mask.overlap(bottom_mask, bottom_offset)
        b_point = bird_mask.overlap(top_mask, top_offset)

        return t_point or b_point
