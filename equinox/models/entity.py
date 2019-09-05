"""Entity Module

This module defines the Entity concept. An Entity is an object that will be displayed on the screen
"""

import weakref
from random import random

import glm

class Entity:

    entities = {}
    
    def __init__(self, model_mesh, pos = glm.vec3(0.0, 0.0, 0.0), angle = glm.vec3(0.0, 0.0, 0.0),scale = glm.vec3(1.0) ):
        self.model_mesh = model_mesh
        self.pos = pos
        self.angle = angle
        self.scale = scale
        self.update()
        #model_name = str(self.model).split('.')[-1].split()[0]
 
        print(f"XXX -> {[str(id(x)) for x in self.model_mesh.mesh_list]}")
        for mesh_id in [id(x) for x in self.model_mesh.mesh_list]:
            if mesh_id not in Entity.entities:
                Entity.entities[mesh_id] = [self,]
            else:
                Entity.entities[mesh_id].append(self)

        #print(f"ENTITIES = [{Entity.entities}]") 

    def scale_by(self, v: glm.vec3):
        self.scale = v
        self.update()

    def rotate_by_vector(self, v: glm.vec3):
        self.angle.x += v.x
        self.angle.y += v.y
        self.angle.z += v.z
        self.update()

    def rotate(self, x: float, y: float, z: float):
        self.angle.x += x 
        self.angle.y += y 
        self.angle.z += z
        self.update()

    def move_to(self, v: glm.vec3):
        self.pos = v
        self.update()

    def move(self, dx: float, dy: float, dz: float):
        self.pos += glm.vec3(dx, dy, dz)
        self.update()

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

    #def draw(self, shader):
        
    #    self.model.draw(shader)
