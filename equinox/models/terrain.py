from equinox.core import equinox_create_window,equinox_run,key
from equinox.models import Model,cleanup
from equinox.render import Renderer,renderer_init,Camera

import glm

from random import random
from .model import bindIndicesToBuffer, storeDataInVBO,createVAO,unbindVAO


class Terrain(Model):
    
    def __init__(self,n_vertex):
        self.vertices = (
            -1.0, 0.0, 1.0,
            -1.0, 0.0, -1.0,
             1.0, 0.0, -1.0,
             1.0, 0.0,  1.0,
        )
        self.normals = (
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0
        )
        self.indices = (
            0,1,2,
            2,3,0
        )
        
    
    def create(self):
        # vaoID = createVAO()
        # bindIndicesToBuffer(self.indices)
        # storeDataInVBO(0,3,self.vertices)
        # storeDataInVBO(1,3,self.normals)
        # unbindVAO()
        # model= BasicModel(vao=vaoID,size = len(self.vertices))
        # model.scale = glm.vec3(10,1,10)
        # #model.pos = glm.vec3(100,0,-100)
        # model.update()
        
        return model

