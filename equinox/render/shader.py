from  OpenGL.GL.shaders import compileShader,compileProgram
from OpenGL.error import GLError
from pyglet.gl import *

from ctypes import *


class Shader:

    def __init__(self,source,shader_type):
        # self._shader = glCreateShader(shader_type)
        self.source = source
        self.shader_type = shader_type
        # count = len(source)
        # src = (c_char_p * count)(*bytes(source,'utf-8'))
        # glShaderSource(self._shader, count, pointer(src), None)
        # glCompileShader(self._shader)
        self._shader =compileShader(source,shader_type)


    @property 
    def shader(self):
        if not self._shader:
            self.compile()
        print(f"shader =>{self._shader}")
        return self._shader
    


class ShaderProgram:

    def __init__(self):
        self.program = None
        

    

    def compile(self,vertex_shader=None,fragment_shader=None):
        self.program =  glCreateProgram()
        glAttachShader(self.program, vertex_shader.shader)
        glAttachShader(self.program, fragment_shader.shader)
        glLinkProgram(self.program)
       
        print(f"shader program -> {self.program}")

    def bind(self):
        print("PROGRAM: ",self.program)
        glUseProgram(self.program) 
          
        

