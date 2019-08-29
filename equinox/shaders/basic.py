import os, os.path

from .core import BaseShader

class BasicShader(BaseShader):

    def __init__(self):
        
        super().__init__(
            os.path.join(os.path.dirname(__file__),"data/basic_vs.glsl"),
            os.path.join(os.path.dirname(__file__),"data/basic_fs.glsl"))

class LightingShader(BaseShader):
    
    def __init__(self):
        
        super().__init__(
            os.path.join(os.path.dirname(__file__),"data/basic_light_vs.glsl"),
            os.path.join(os.path.dirname(__file__),"data/basic_light_fs.glsl"))