import pygame
import os

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png"))),
]


class Bird:

    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    MIN_ROTATION = -45
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        self.tick_count = 0
        self.vel = 0
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5  # pygame need a negative velocity to go up
        self.tick_count = 0

    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        d = d if d < 16 else 16  # Cap the fall speed
        d = d - 2 if d > 0 else d  # Increase the jump

        self.y = self.y + d

        if d < 0:
            if self.rotation < self.MAX_ROTATION:
                self.rotation = self.MAX_ROTATION
        else:
            if self.rotation > self.MIN_ROTATION:
                self.rotation -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count % 3 == 0:
            self.img = self.IMGS[0]
        if self.img_count % 3 == 1:
            self.img = self.IMGS[1]
        if self.img_count % 3 == 2:
            self.img = self.IMGS[2]

        if self.rotation <= 0:  # No flapping while falling
            self.img = self.IMGS[1]

        rotated_image = pygame.transform.rotate(self.img, self.rotation)
        new_rect = rotated_image.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center
        )
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
