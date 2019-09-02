
from typing import List
from dataclasses import dataclass

import glm
import tinyobjloader

@dataclass
class MaterialInfo:
    color: glm.vec3 = None

class Mesh:
    """A mesh contains the geometrical + texture coordinates info that are contained in a Model. 
    Every model can share the mesh with other models"""
    def __init__(self, vertices: List[float], normals: List[float], material_info: MaterialInfo):
        if not vertices:
            raise Exception("vertices are needed in order to construct a Mesh instance")
        
        self.vertices = vertices
        self.normals = normals
        self.material_info = material_info
        

    @staticmethod
    def mesh_from_file(filename: str):
        reader = tinyobjloader.ObjReader()
        ret = reader.ParseFromFile(filename)
        if ret == False:
            print("Warn:", reader.Warning())
            print("Err:", reader.Error())
            print("Failed to load : ", filename)
            
        if reader.Warning():
            print("Warn:", reader.Warning())

        attrib = reader.GetAttrib()
        print("attrib.vertices = ", len(attrib.vertices))
        print("attrib.normals = ", len(attrib.normals))
        print("attrib.texcoords = ", len(attrib.texcoords))
        shapes = reader.GetShapes()
        print("Num shapes: ", len(shapes))
        print("Num materials: ", len(reader.GetMaterials()))
        model_mesh =  ModelMesh()
        print(f"material: {reader.GetMaterials()[0].ambient}")

        for num_shape, shape in enumerate(shapes):
            print(shape.name)
            print("num_indices = {}".format(len(shape.mesh.indices)))
            print(f"material = [{reader.GetMaterials()[num_shape].ambient}]")
            print(f"material = [{reader.GetMaterials()[num_shape].ambient_texname}]")
            

            vertices = []
            normals = []
            uvCoords = []

            for idxs in shape.mesh.indices:
                vertices.extend(attrib.vertices[3*idxs.vertex_index:3*idxs.vertex_index+3])
                normals.extend(attrib.vertices[3*idxs.normal_index:3*idxs.normal_index+3])
                uvCoords.extend(attrib.texcoords[2*idxs.texcoord_index:2*idxs.texcoord_index+2])
            
            for i in range(len(vertices)//9):
                p0 = glm.vec3(*vertices[9*i:9*i+3])
                p1 = glm.vec3(*vertices[9*i+3:9*i+6])
                p2 = glm.vec3(*vertices[9*i+6:9*i+9])
                v0 = p1-p0
                v1 = p2-p0
                N = glm.normalize(glm.cross(v0,v1))
                
                normals[9*i] = N.x
                normals[9*i+1] = N.y
                normals[9*i+2] = N.z
                normals[9*i+3] = N.x
                normals[9*i+4] = N.y
                normals[9*i+5] = N.z
                normals[9*i+6] = N.x
                normals[9*i+7] = N.y
                normals[9*i+8] = N.z
            #print(f"Adding mesh of {len(vertices),")
            material_info = MaterialInfo()
            mesh = None
            if not reader.GetMaterials()[num_shape].ambient_texname == "":
                mesh = TexturedMesh(vertices, normals, uvCoords, material_info)
            else:
                material_info.color = glm.vec3(*reader.GetMaterials()[num_shape].diffuse)
                print(f"material_info.color = {material_info.color}")
                mesh = RawMesh(vertices, normals, material_info)
            model_mesh.add(mesh)
        return model_mesh
 
class RawMesh(Mesh):
    """Mesh with only geometrical info"""
    pass
    #def __init__(self, vertices: List[float], normals: List[float], material_info: MaterialInfo):
    #    super().__init__(vertices, normals, material_info)



class TexturedMesh(Mesh):
    """a raw mesh with texture informations"""

    def __init__(self, vertices: List[float], normals: List[float], texture_coords: List[float], material_info: MaterialInfo):
        super().__init__(vertices, normals, material_info)
        self.texture_coords = texture_coords
   


class ModelMesh:
    """A ModelMesh contains the mesh (more than one) that build up a single model"""
    def __init__(self):
        self.mesh_list: List[Mesh] = []

    def add(self, mesh: Mesh,):
        """Add a mesh to this ModelMesh object"""
        self.mesh_list.append(mesh)
    