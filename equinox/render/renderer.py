import logging
from abc import ABC, abstractmethod


from  OpenGL.GL.shaders import compileShader,compileProgram
from OpenGL.error import GLError
import OpenGL
from pyglet.gl import * # pylint: disable=unused-wildcard-import
import pyglet

import glm

from equinox.shaders import BasicShader,LightingShader,BaseShader,TexturedShader
from equinox.models.mesh import Mesh
from equinox.models import Entity


logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)


class BaseRenderer(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def render(self,*args,**kwargs):
        pass


class Renderer:

    def __init__(self, shader=None):
        self.shader = shader
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        
    def prepare(self,camera):
        self.shader.start()
        self.shader.set_camera(camera)
        self.shader.setUniformVec3("lightPos", glm.vec3(0.0, 4.0, 3.0))

    def cleanup(self):
        self.shader.stop()

    def prepareMaterial(self, material_info):
        if material_info.color:
            self.shader.setUniformVec3("objectColor", material_info.color)
        else:
            
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(material_info.texture.texture.target, material_info.texture.texture.id)
    
    # def renderEntity(self):
    #     pass
    #     #print(len(self.mesh_data.mesh_list[i].vertices))
        
    def renderEntities(self, entities,material_info,mesh,vao):
        

        glBindVertexArray(vao)
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)
        self.prepareMaterial(material_info)

        for entity in entities:
            self.shader.setUniformMat4("modelMatrix", entity.model_matrix)
            #self.shader.setUniformVec3("objectColor", material_info.color)
            
            #self.renderEntity(self.shader)
            glDrawElements(GL_TRIANGLES, int(len(mesh.vertices)), GL_UNSIGNED_INT, 0)
        glDisableVertexAttribArray(2)
        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)


        #self.shader.stop()
        

class MasterRenderer:

    def __init__(self):
        
       
        self.shader = LightingShader()
        self.texturedShader = TexturedShader()
        self.renderer = Renderer(self.shader)

    def prepare(self):
        glClearColor(0.0, 0.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    def render(self, camera):
        
        
        for mesh_id,entities in Entity.entities.items():
            mesh:Mesh = Mesh.registry[mesh_id][0]
            mesh_vao  = Mesh.registry[mesh_id][1]
            if mesh.material_info.color:
                self.renderer.shader = self.shader
            elif mesh.material_info.texture:
                self.renderer.shader = self.texturedShader
            self.renderer.prepare(camera)
            #print(f"{mesh_id} [{mesh_vao}] => {mesh.material_info}")
            self.renderer.renderEntities(entities, mesh.material_info, mesh, mesh_vao)
        self.renderer.cleanup()


    def cleanUp(self):
        pass
