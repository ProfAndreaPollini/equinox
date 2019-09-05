# import os
# import os.path

# from equinox.mesh import TexturedMesh
# from equinox.models.texture import Texture


# import glm

# from random import random
# from .glutils import bindIndicesToBuffer, storeDataInVBO,createVAO,unbindVAO


# class Terrain(TexturedMesh):
    
#     def __init__(self):
#         self.texture = Texture(os.path.join(os.path.dirname(__file__), "textures","grass.png"))
#         print(f"TEXTURE = [{self.texture.id}] -> {self.texture.target}")
#         self.vertices = (
#             -1.0, 0.0, 1.0,
#             -1.0, 0.0, -1.0,
#              1.0, 0.0, -1.0,
#              1.0, 0.0,  1.0,
#         )
#         self.normals = (
#             0.0, 1.0, 0.0,
#             0.0, 1.0, 0.0,
#             0.0, 1.0, 0.0,
#             0.0, 1.0, 0.0
#         )
#         self.indices = (
#             0,1,2,
#             2,3,0
#         )
        
    


