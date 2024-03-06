import pygame, math
from pygame.sprite import Sprite
from pygame.locals import *
import random

class Asteroid(Sprite):
    def __init__(self,cont):
        Sprite.__init__(self)
        self.vel = [random.randint(-2,2), random.randint(-2,2)]
        self.contenedor = cont
        self.angulo = 0
        self.rotacion = 0
        self.rotacion = random.randint(-20,20)
        self.image_base = pygame.image.load("imagenes/asteroide.png")
        self.image = self.image_base
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randint(0,self.contenedor[0]),random.randint(0,self.contenedor[1]))
        self.explosion = pygame.mixer.Sound('sonido/explosion.mp3')
        self.explosion.set_volume(0.05)
    
    def update(self):
        self.angulo += self.rotacion
        centerx = self.rect.centerx
        centery = self.rect.centery
        self.image = pygame.transform.rotate(self.image_base, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.rect = self.rect.move(self.vel)
        self.rect.x =  self.rect.x % self.contenedor[0]
        self.rect.y =  self.rect.y % self.contenedor[1]
    
    def exploter(self):
        self.image = pygame.image.load("imagenes/explosion.png")
        self.explosion.play()

