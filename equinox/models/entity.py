"""Entity Module

This module defines the Entity concept. An Entity is an object that will be displayed on the screen
"""
from random import random

import glm

class Entity:
    def __init__(self, model):
        self.model = model
        self.pos = glm.vec3(0.0, 0.0, 0.0)
        self.angle = glm.vec3(0.0, 0.0, 0.0)#glm.vec3(random()*90.0,random()*90.0,random()*90.0)
        self.scale = glm.vec3(1.0)
        self.update()

    def scale_by(self, v: glm.vec3):
        self.scale = v

    def rotate_by_vector(self, v: glm.vec3):
        self.angle.x += v.x
        self.angle.y += v.y
        self.angle.z += v.z

    def rotate(self, x: float, y: float, z: float):
        self.angle.x += x 
        self.angle.y += y 
        self.angle.z += z

    def move(self, dx=0, dy=0, dz=0):
        self.pos += glm.vec3(dx, dy, dz)

    def update(self):
        self.model_matrix = glm.mat4(1.0)
        self.model_matrix = glm.translate(self.model_matrix, self.pos)
        self.model_matrix = glm.scale(self.model_matrix, self.scale)
        self.model_matrix = glm.rotate(self.model_matrix,\
             glm.radians(self.angle.x), glm.vec3(1.0, 0.0, 0.0))
        self.model_matrix = glm.rotate(self.model_matrix,\
             glm.radians(self.angle.y), glm.vec3(0.0, 1.0, 0.0))
        self.model_matrix = glm.rotate(self.model_matrix,\
             glm.radians(self.angle.z), glm.vec3(0.0, 0.0, 1.0))

    def draw(self, shader):
        shader.setUniformMat4("modelMatrix", self.model_matrix)
        self.model.draw(shader)
