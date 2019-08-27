import logging
from  OpenGL.GL.shaders import compileShader,compileProgram
from OpenGL.error import GLError
import OpenGL
from pyglet.gl import *
import pyglet

import glm

from .shader import Shader,ShaderProgram

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

def renderer_init(window):
    logger.warn(f"renderer_init({window.width}, {window.height})")
    #glViewport(0,0,window.width, window.height)
    
     

    

class Renderer:

        def __init__(self):
            self.vertex_shader_source = """
            #version 330
            in layout(location = 0) vec3 position;

            uniform mat4 modelMatrix;
            uniform mat4 viewMatrix;
            uniform mat4 projectMatrix;

            void main()
                {
                    gl_Position = projectMatrix*viewMatrix*modelMatrix*vec4(position,1.0f);
                    
                }
            """

            self.fragment_shader_source = """
            #version 330
            
            out vec4 outColor;
            
            void main()
                {
                    outColor = vec4(0.0,0.0,1.0,0.1);
                    
                }
            """

            #self.program = 
            
            self.shader = compileProgram(
               compileShader(self.vertex_shader_source, GL_VERTEX_SHADER),
                compileShader(self.fragment_shader_source, GL_FRAGMENT_SHADER))

        
            

        def prepare(self):
            glClearColor(1.0,0.0,0.0,1.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        def render(self,camera,models):
            print("program -> ",self.shader)
            glUseProgram(self.shader)
            viewMatrixLoc = OpenGL.GL.glGetUniformLocation(self.shader, 'viewMatrix')
            glUniformMatrix4fv(viewMatrixLoc, 1, GL_FALSE, glm.value_ptr(camera.viewMatrix()));
            

            projectMatrixLoc = OpenGL.GL.glGetUniformLocation(self.shader, 'projectMatrix')
            glUniformMatrix4fv(projectMatrixLoc, 1, GL_FALSE, glm.value_ptr(camera.projectMatrix()));
           
            for model in models:
                self.render_model(model)

        def render_model(self,model):
            
            
            modelMatrixLoc = OpenGL.GL.glGetUniformLocation(self.shader, 'modelMatrix')
            glUniformMatrix4fv(modelMatrixLoc, 1, GL_FALSE, glm.value_ptr(model.modelMatrix));
            
             
            print("vao =>",model.vao,model.size,modelMatrixLoc)
            glBindVertexArray(model.vao)
            glEnableVertexAttribArray(0)
            glDrawArrays(GL_TRIANGLES,0,int(model.size))
            glDisableVertexAttribArray(0)
            glBindVertexArray(0)

