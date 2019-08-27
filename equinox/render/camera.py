

from pyglet.gl import *
import glm

class Camera:

    def __init__(self,W,H):
        self.screenWidth = W
        self.screenHeight = H

    
    def viewMatrix(self):
        view = glm.mat4(1.0)
        # note that we're translating the scene in the reverse direction of where we want to move
        view = glm.translate(view, glm.vec3(0.0, 0.0, -1.0))
        #print(view)
        return view

    def projectMatrix(self):
        projection = glm.perspective(glm.radians(45.0), self.screenWidth / self.screenHeight, 0.1, 100.0);
        return projection