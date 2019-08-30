
from typing import List


class Mesh:

    def __init__(self, vertices, normals, texture_coords=None):
        if not vertices:
            raise Exception("vertices are needed in order to construct a Mesh instance")
        
        self.vertices = vertices 
        self.normals = normals
        self.texture_coords = texture_coords

    
class ModelMesh:
    def __init__(self):
        self.mesh_list: List[Mesh] = []
    

    def add(self, mesh: Mesh): 
        self.mesh_list.append(mesh)

    