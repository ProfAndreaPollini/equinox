import logging
from  OpenGL.GL.shaders import compileShader,compileProgram
from OpenGL.error import GLError
import OpenGL
from pyglet.gl import *
import pyglet

import glm

from ..shaders import BasicShader,LightingShader

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

def renderer_init(window):
    logger.warn(f"renderer_init({window.width}, {window.height})")
    

class Renderer:

        def __init__(self):
            self.shader = BasicShader()
            self.lightingShader = LightingShader()
            

        def prepare(self):
            glClearColor(0.0,0.0,0.0,1.0)
            glEnable(GL_DEPTH_TEST); 
            glDepthFunc(GL_LESS);
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        def render(self,camera,models):
            self.lightingShader.bind(camera)
            self.lightingShader.setUniformVec3("viewPos",camera.pos)
            self.lightingShader.setUniformMat4("viewMatrix",camera.viewMatrix())
            self.lightingShader.setUniformMat4("projectMatrix",camera.projectMatrix())
            self.lightingShader.setUniformVec3("lightPos",glm.vec3(0.0,4.0,0.0))
            
            for model in models:
                self.lightingShader.setUniformMat4("modelMatrix",model.modelMatrix)
                self.lightingShader.setUniformVec3("objectColor",model.color)
                
                

                glBindVertexArray(model.vao)
                glEnableVertexAttribArray(0)
                glEnableVertexAttribArray(1)
                glEnableVertexAttribArray(2)
                
                glDrawElements(GL_TRIANGLES,int(model.size),GL_UNSIGNED_INT,0)
                glDisableVertexAttribArray(2)
                glDisableVertexAttribArray(1)
                glDisableVertexAttribArray(0)
                glBindVertexArray(0)

        

