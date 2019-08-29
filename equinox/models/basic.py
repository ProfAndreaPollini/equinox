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


class BasicModel:

    @staticmethod
    def create(vertices):
        vaoID = createVAO()
        storeDataInVBO(0,3,vertices)
        unbindVAO()
        return BasicModel(vao=vaoID,size = len(vertices)/3)

    @staticmethod
    def create(vertices,normals):
        vaoID = createVAO()
        storeDataInVBO(0,3,vertices)
        storeDataInVBO(1,3,normals)
        unbindVAO()
        return BasicModel(vao=vaoID,size = len(vertices)/3)


    def __init__(self, vao=0,size=0):
        self.vao = vao
        self.size = size
        self.pos = glm.vec3(2.0*random()-1,2.0*random()-1,2.0*random()-1)
        #glm.mat4 model = glm.mat4(1.0f)
        #model = glm.rotate(model, glm.radians(-55.0f), glm.vec3(1.0f, 0.0f, 0.0f))
        self.angle = glm.vec3(random()*90.0,random()*90.0,random()*90.0)
        self.scale = glm.vec3(0.4*random()+0.1)
        self.color = glm.vec3(random(),random(),random())
        self.update()

    def scale(self,scale_vec3):
        self.scale = scale_vec3

    def rotate(self,v):
        self.angle.x += v.x 
        self.angle.y += v.y 
        self.angle.z += v.z 

    def rotate(self,x,y,z):
        self.angle.x += x 
        self.angle.y += y 
        self.angle.z += z

    def move(self,dx=0,dy=0,dz=0):
        self.pos += glm.vec3(dx,dy,dz)
        

    def update(self):
        self.modelMatrix = glm.mat4(1.0)
        self.modelMatrix = glm.translate(self.modelMatrix,self.pos);
        self.modelMatrix = glm.scale(self.modelMatrix,self.scale );
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(self.angle.x), glm.vec3(1.0, 0.0, 0.0)); 
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(self.angle.y), glm.vec3(0.0, 1.0, 0.0)); 
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(self.angle.z), glm.vec3(0.0, 0.0, 1.0)); 
    