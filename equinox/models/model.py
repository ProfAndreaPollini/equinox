from __future__ import annotations
from abc import ABC, abstractmethod
from ctypes import sizeof, c_void_p,pointer


import pyglet
from random import random
import glm
from pyglet.gl import *
import tinyobjloader


from .mesh import Mesh, ModelMesh,RawMesh,TexturedMesh





vaos = []
vbos = []

def createVAO():
    vao_id = GLuint()
    glGenVertexArrays(1,vao_id)
    glBindVertexArray(vao_id)
    vaos.append(vao_id)
    #print("vao -> ",vao_id)
    return vao_id

def unbindVAO():
    #glBindVertexArray(0)
    pass

def cleanup():
    for vao in vaos:
        glDeleteVertexArrays(1,vao)
    for vbo in vbos:
        glDeleteVertexArrays(1,vbo)

def createVBO():
    vbo_id = GLuint()
    glGenBuffers(1,vbo_id)
    vbos.append(vbo_id)
    #print("vbo -> ",vbo_id)
    return vbo_id

def storeDataInVBO(pos,size,data):
    buffer = (GLfloat * len(data))(*data)
    
    vboID = createVBO()
    #print(f"VBO[{pos} | {vboID}] = {data[:10]} ({sizeof(buffer)})")
    glBindBuffer(GL_ARRAY_BUFFER,vboID)
    glBufferData(GL_ARRAY_BUFFER,sizeof(buffer),buffer,GL_STATIC_DRAW)
    glEnableVertexAttribArray(pos)
    glVertexAttribPointer(pos,size,GL_FLOAT,GL_FALSE,0,0)
     #glEnableVertexAttribArray(pos)
    glBindBuffer(GL_ARRAY_BUFFER,0)
    
def bindIndicesToBuffer(indices):
    
    vboID = createVBO()
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,vboID)
    buffer =(GLuint * len(indices))(*indices)
    #print(f"bindIndicesToBuffer({sizeof(buffer)}|{vboID}) -> {indices}")
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,sizeof(buffer),buffer,GL_STATIC_DRAW)


class Model:

    
    def vao_from_RawMesh(self, mesh: RawMesh):
        vaoID = createVAO()
        bindIndicesToBuffer([i for i in range(len(mesh.vertices))])
        storeDataInVBO(0, 3, mesh.vertices)
        storeDataInVBO(1, 3, mesh.normals)
        unbindVAO()
        Mesh.registry[id(mesh)] = [mesh,vaoID]
        self.vaos.append(vaoID)

    def __init__(self):
        self.mesh_data: ModelMesh
        self.vaos = []

    @staticmethod
    def model_from_mesh(model_mesh: ModelMesh):
        model = Model()
        model.mesh_data = model_mesh
        return model


    def load(self):
        
        for mesh in self.mesh_data.mesh_list:
            method_name = str(type(mesh)).split(".")[-1].split("'")[0]
            getattr(self, 'vao_from_'+method_name)(mesh)
            

    def get_mesh_info(self):
        pass
        #for mesh in self.mesh_data.mesh_list:
  
    def draw(self, shader):
        
        for i, vao in enumerate(self.vaos):
            
            glBindVertexArray(self.vaos[i])
            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(1)
            glEnableVertexAttribArray(2)
            #print(len(self.mesh_data.mesh_list[i].vertices))
            glDrawElements(GL_TRIANGLES, int(len(self.mesh_data.mesh_list[i].vertices)), GL_UNSIGNED_INT, 0)
            glDisableVertexAttribArray(2)
            glDisableVertexAttribArray(1)
            glDisableVertexAttribArray(0)
            glBindVertexArray(0)