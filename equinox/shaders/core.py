from  OpenGL.GL.shaders import compileShader,compileProgram
from OpenGL.error import GLError
import OpenGL
from pyglet.gl import *

from ctypes import *
import glm



class BaseShader:

    def __init__(self,vertex_shader=None,fragment_shader=None):
        vertex_shader_source = ""
        fragment_shader_source = ""
        #read the vertex shader
        with open(vertex_shader,'r') as vs_file:
            vertex_shader_source = vs_file.read()
        
        #read fragment shader
        with open(fragment_shader,'r') as vs_file:
            fragment_shader_source = vs_file.read()

        uniforms_list = []
        for source in [vertex_shader_source,fragment_shader_source]:
            uniforms_list.extend([ y.split(" ")[-1][:-1] for y in [x.strip() for x in source.split("\n")] if y.startswith("uniform")])


        self.program = compileProgram(
               compileShader(vertex_shader_source, GL_VERTEX_SHADER),
                compileShader(fragment_shader_source, GL_FRAGMENT_SHADER))

        self.uniforms = {}
        for uniform in uniforms_list:
            self.uniforms[uniform] = OpenGL.GL.glGetUniformLocation(self.program, uniform)

        
    def setUniformMat4(self,uniform_name,mat):
        glUniformMatrix4fv(self.uniforms[uniform_name], 1, GL_FALSE, glm.value_ptr(mat))

    def setUniformVec3(self,uniform_name,vec):
        glUniform3fv(self.uniforms[uniform_name], 1, glm.value_ptr(vec))

    

    def bind(self,camera):
       
        glUseProgram(self.program) 
        #self.setUniformMat4('viewMatrix',camera.viewMatrix)
        #self.setUniformMat4('projectMatrix',camera.projectMatrix())  
          
    @property
    def shader(self):
        return self.program
        

