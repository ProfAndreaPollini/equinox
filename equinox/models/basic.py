from ctypes import sizeof, c_void_p,pointer
import pyglet
from random import random
import glm
from pyglet.gl import *
vaos = []
vbos = []

def createVAO():
    vao_id = GLuint()
    glGenVertexArrays(1,vao_id)
    glBindVertexArray(vao_id)
    vaos.append(vao_id)
    print("vao -> ",vao_id)
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
    print("vbo -> ",vbo_id)
    return vbo_id

def storeDataInVBO(pos,size,data):
    buffer = (GLfloat * len(data))(*data)
    
    vboID = createVBO()
    print(f"VBO[{pos} | {vboID}] = {data[:10]} ({sizeof(buffer)})")
    glBindBuffer(GL_ARRAY_BUFFER,vboID)
    glBufferData(GL_ARRAY_BUFFER,sizeof(buffer),buffer,GL_STATIC_DRAW)
    glEnableVertexAttribArray(pos)
    glVertexAttribPointer(pos,size,GL_FLOAT,GL_FALSE,0,0)
     #glEnableVertexAttribArray(pos)
    glBindBuffer(GL_ARRAY_BUFFER,0)
    

class BasicModel:

    @staticmethod
    def create(vertices):
        vaoID = createVAO()
        storeDataInVBO(0,3,vertices)
        unbindVAO()
        return BasicModel(vao=vaoID,size = len(vertices)/3)


    def __init__(self, vao=0,size=0):
        self.vao = vao
        self.size = size
        self.pos = glm.vec3(2.0*random()-1,2.0*random()-1,2.0*random()-1)
        #glm.mat4 model = glm.mat4(1.0f)
        #model = glm.rotate(model, glm.radians(-55.0f), glm.vec3(1.0f, 0.0f, 0.0f))
        self.z_angle = 0
        self.scale = 0.4*random()+0.1
        self.update()

    def rotate(self,v):
        self.z_angle += v 

    def move(self,dx=0,dy=0,dz=0):
        self.pos += glm.vec3(dx,dy,dz)
        

    def update(self):
        self.modelMatrix = glm.mat4(1.0)
        self.modelMatrix = glm.translate(self.modelMatrix,self.pos);
        self.modelMatrix = glm.scale(self.modelMatrix, glm.vec3(self.scale));
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(self.z_angle), glm.vec3(0.0, 0.0, 1.0)); 
        
    