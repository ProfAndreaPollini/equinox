import logging
from abc import ABC, abstractmethod


from  OpenGL.GL.shaders import compileShader,compileProgram
from OpenGL.error import GLError
import OpenGL
from pyglet.gl import * # pylint: disable=unused-wildcard-import
import pyglet

import glm

from equinox.shaders import BasicShader,LightingShader

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

def renderer_init(window):
    logger.warn(f"renderer_init({window.width}, {window.height})")
    
class BaseRenderer(ABC):

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def render(self,*args,**kwargs):
        pass

# class MasterRenderer:

#     def __init__(self):
#         self.renderers = []

#     def add(self, renderer : BaseRenderer):
#         self.renderers.append(renderer)

class Renderer(BaseRenderer):

        def __init__(self):
            self.shader = BasicShader()
            self.lightingShader = LightingShader()
            glEnable(GL_DEPTH_TEST)
            glDepthFunc(GL_LESS)
            

        def use(self):
            glClearColor(0.0,0.0,0.0,1.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        def render(self, camera, entities):
            self.lightingShader.bind(camera)
            self.lightingShader.setUniformVec3("lightPos", glm.vec3(0.0,4.0,3.0))
            
            for entity in entities:
                entity.draw(self.lightingShader)

        

