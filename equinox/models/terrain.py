from equinox.core import equinox_create_window,equinox_run,key
from equinox.models import BasicModel,cleanup,Cube
from equinox.render import Renderer,renderer_init,Camera

import glm

from random import random
from .basic import bindIndicesToBuffer, storeDataInVBO,BasicModel,createVAO,unbindVAO


class Terrain(BasicModel):
    
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
        # VERTEX_COUNT = 100
        # SIZE = 100
        # vertexPointer = 0
        # self.vertices = [0,]*(3*VERTEX_COUNT * VERTEX_COUNT)
        # self.normals  = [0,]*(3*VERTEX_COUNT * VERTEX_COUNT)
        # self.indices  = [0,]* (3*6 * (VERTEX_COUNT - 1) * (VERTEX_COUNT - 1))

        # for i in range(VERTEX_COUNT):
        #     for j in range(VERTEX_COUNT):
        #         self.vertices[vertexPointer] =  float(j) / (VERTEX_COUNT - 1) * SIZE
        #         self.vertices[vertexPointer+1] = 0.0#0.03*random()
        #         self.vertices[vertexPointer+2] = float(i) / (VERTEX_COUNT - 1) * SIZE 
        #         self.normals[vertexPointer] = 0.0
        #         self.normals[vertexPointer+1] = 1.0
        #         self.normals[vertexPointer+2] = 0.0
        #         vertexPointer += 3
        # print(self.vertices)	
		# 		#textureCoords[vertexPointer * 2] = (float)j / ((float)VERTEX_COUNT - 1);
		# 		#textureCoords[vertexPointer * 2 + 1] = (float)i / ((float)VERTEX_COUNT - 1);
			
        # pointer = 0;
        # for gz in range(VERTEX_COUNT):
        #     for gx in range(VERTEX_COUNT):
        #         topLeft = (gz * VERTEX_COUNT) + gx;
        #         topRight = topLeft + 1;
        #         bottomLeft = ((gz + 1) * VERTEX_COUNT) + gx;
        #         bottomRight = bottomLeft + 1;
        #         self.indices[pointer] = topLeft; pointer += 1
        #         self.indices[pointer] = bottomLeft; pointer += 1
        #         self.indices[pointer] = topRight; pointer += 1
        #         self.indices[pointer] = topRight; pointer += 1
        #         self.indices[pointer] = bottomLeft; pointer += 1
        #         self.indices[pointer] = bottomRight; pointer += 1
			
		
    
    def create(self):
        vaoID = createVAO()
        bindIndicesToBuffer(self.indices)
        storeDataInVBO(0,3,self.vertices)
        storeDataInVBO(1,3,self.normals)
        unbindVAO()
        model= BasicModel(vao=vaoID,size = len(self.vertices))
        model.scale = glm.vec3(10,1,10)
        #model.pos = glm.vec3(100,0,-100)
        model.update()
        return model

