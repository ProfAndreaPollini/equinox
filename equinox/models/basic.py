from __future__ import annotations
from abc import ABC, abstractmethod
from ctypes import sizeof, c_void_p,pointer


import pyglet
from random import random
import glm
from pyglet.gl import *
import tinyobjloader


from .mesh import Mesh, ModelMesh



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


class Model(ABC):

    def __init__(self):
        self.pos = glm.vec3(2.0*random()-1,1.0,2.0*random()-1)
        #glm.mat4 model = glm.mat4(1.0f)
        #model = glm.rotate(model, glm.radians(-55.0f), glm.vec3(1.0f, 0.0f, 0.0f))
        self.angle = glm.vec3(0.0,0.0,0.0)#glm.vec3(random()*90.0,random()*90.0,random()*90.0)
        self.scale = glm.vec3(1.0)
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
    
    @staticmethod
    def mesh_from_file(filename: str):
        reader = tinyobjloader.ObjReader()
        ret = reader.ParseFromFile(filename)
        if ret == False:
            print("Warn:", reader.Warning())
            print("Err:", reader.Error())
            print("Failed to load : ", filename)
            
        if reader.Warning():
            print("Warn:", reader.Warning())

        attrib = reader.GetAttrib()
        print("attrib.vertices = ", len(attrib.vertices))
        print("attrib.normals = ", len(attrib.normals))
        print("attrib.texcoords = ", len(attrib.texcoords))
        shapes = reader.GetShapes()
        print("Num shapes: ", len(shapes))
    
        model_mesh =  ModelMesh()

        for shape in shapes:
            print(shape.name)
            print("num_indices = {}".format(len(shape.mesh.indices)))

            vertices = []
            normals = []
            uvCoords = []

            for idxs in shape.mesh.indices:
                vertices.extend(attrib.vertices[3*idxs.vertex_index:3*idxs.vertex_index+3])
                normals.extend(attrib.vertices[3*idxs.normal_index:3*idxs.normal_index+3])
                uvCoords.extend(attrib.texcoords[2*idxs.texcoord_index:2*idxs.texcoord_index+2])
            
            for i in range(len(vertices)//9):
                p0 = glm.vec3(*vertices[9*i:9*i+3])
                p1 = glm.vec3(*vertices[9*i+3:9*i+6])
                p2 = glm.vec3(*vertices[9*i+6:9*i+9])
                v0 = p1-p0
                v1 = p2-p0
                N = glm.normalize(glm.cross(v0,v1))
                
                normals[9*i] = N.x
                normals[9*i+1] = N.y
                normals[9*i+2] = N.z
                normals[9*i+3] = N.x
                normals[9*i+4] = N.y
                normals[9*i+5] = N.z
                normals[9*i+6] = N.x
                normals[9*i+7] = N.y
                normals[9*i+8] = N.z
            #print(f"Adding mesh of {len(vertices),")
            model_mesh.add(Mesh(vertices,normals,uvCoords))
        return model_mesh

    @staticmethod
    @abstractmethod
    def model_from_mesh(self,filename):
        pass

    
    @abstractmethod
    def load(self):
        pass

class BasicModel(Model):

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

    @staticmethod
    def create(indices,vertices,normals):
        model_mesh = ModelMesh()
        model_mesh.add(Mesh())
        model = BasicModel()
        model.mesh_data = model_mesh
        return model

    def __init__(self, vao=0,size=0):
        super().__init__()
        self.vao = vao
        self.size = size
        
    
            
    @staticmethod
    def model_from_mesh(model_mesh: ModelMesh):
        model = BasicModel()
        model.mesh_data = model_mesh
        return model

    def _vao_from_mesh(self,aMesh: Mesh):
        vaoID = createVAO()
        bindIndicesToBuffer([i for i in range(len(aMesh.vertices))])
        storeDataInVBO(0,3,aMesh.vertices)
        storeDataInVBO(1,3,aMesh.normals)
        unbindVAO()
        self.vaos.append(vaoID)

    def load(self):
        self.vaos = []
        for mesh in self.mesh_data.mesh_list:
            self._vao_from_mesh(mesh)

    def draw(self):
        for i,vao in enumerate(self.vaos):
            glBindVertexArray(self.vaos[i])
            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(1)
            glEnableVertexAttribArray(2)
            #print(len(self.mesh_data.mesh_list[i].vertices))
            glDrawElements(GL_TRIANGLES,int(len(self.mesh_data.mesh_list[i].vertices)),GL_UNSIGNED_INT,0)
            glDisableVertexAttribArray(2)
            glDisableVertexAttribArray(1)
            glDisableVertexAttribArray(0)
            glBindVertexArray(0)