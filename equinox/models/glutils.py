from __future__ import annotations
from abc import ABC, abstractmethod
from ctypes import sizeof, c_void_p,pointer


import pyglet
from random import random
import glm
from pyglet.gl import *
import tinyobjloader





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

