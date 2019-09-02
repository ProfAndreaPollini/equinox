# from ctypes import sizeof, c_void_p,pointer
# import pyglet
# from random import random
# import glm
# from pyglet.gl import *

# from .basic import bindIndicesToBuffer, storeDataInVBO,BasicModel,createVAO,unbindVAO

# class Cube(BasicModel):
#     vertices = (
#     .5, .5, .5,  -.5, .5, .5,  -.5,-.5, .5,  .5,-.5, .5, # v0,v1,v2,v3 (front)
#      .5, .5, .5,   .5,-.5, .5,   .5,-.5,-.5,  .5, .5,-.5, # v0,v3,v4,v5 (right)
#      .5, .5, .5,   .5, .5,-.5,  -.5, .5,-.5, -.5, .5, .5, # v0,v5,v6,v1 (top)
#     -.5, .5, .5,  -.5, .5,-.5,  -.5,-.5,-.5, -.5,-.5, .5, # v1,v6,v7,v2 (left)
#     -.5,-.5,-.5,   .5,-.5,-.5,   .5,-.5, .5, -.5,-.5, .5, # v7,v4,v3,v2 (bottom)
#      .5,-.5,-.5,  -.5,-.5,-.5,  -.5, .5,-.5,  .5, .5,-.5  # v4,v7,v6,v5 (back)
#     )

#     normals = (
#      0, 0, 1,   0, 0, 1,   0, 0, 1,   0, 0, 1,  # v0,v1,v2,v3 (front)
#      1, 0, 0,   1, 0, 0,   1, 0, 0,   1, 0, 0,  # v0,v3,v4,v5 (right)
#      0, 1, 0,   0, 1, 0,   0, 1, 0,   0, 1, 0,  # v0,v5,v6,v1 (top)
#     -1, 0, 0,  -1, 0, 0,  -1, 0, 0,  -1, 0, 0,  # v1,v6,v7,v2 (left)
#      0,-1, 0,   0,-1, 0,   0,-1, 0,   0,-1, 0,  # v7,v4,v3,v2 (bottom)
#      0, 0,-1,   0, 0,-1,   0, 0,-1,   0, 0,-1   # v4,v7,v6,v5 (back)
#     )

#     indices = (
#     0, 1, 2,   2, 3, 0,    # v0-v1-v2, v2-v3-v0 (front)
#     4, 5, 6,   6, 7, 4,    # v0-v3-v4, v4-v5-v0 (right)
#     8, 9,10,  10,11, 8,    # v0-v5-v6, v6-v1-v0 (top)
#     12,13,14,  14,15,12,   # v1-v6-v7, v7-v2-v1 (left)
#     16,17,18,  18,19,16,   # v7-v4-v3, v3-v2-v7 (bottom)
#     20,21,22,  22,23,20    # v4-v7-v6, v6-v5-v4 (back)
#     )

#     @staticmethod
#     def create():
#         vaoID = createVAO()
#         bindIndicesToBuffer(Cube.indices)
#         storeDataInVBO(0,3,Cube.vertices)
#         storeDataInVBO(1,3,Cube.normals)
#         unbindVAO()
#         return BasicModel(vao=vaoID,size = len(Cube.vertices))