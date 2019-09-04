import sys

import tinyobjloader

from .model import bindIndicesToBuffer, storeDataInVBO,Model,createVAO,unbindVAO
from .mesh import Mesh, ModelMesh

def load_model_from_file(filename):
    reader = tinyobjloader.ObjReader()
    ret = reader.ParseFromFile(filename)
    if ret == False:
        print("Warn:", reader.Warning())
        print("Err:", reader.Error())
        print("Failed to load : ", filename)
        sys.exit(-1)
    if reader.Warning():
        print("Warn:", reader.Warning())

    attrib = reader.GetAttrib()
    print("attrib.vertices = ", len(attrib.vertices))
    print("attrib.normals = ", len(attrib.normals))
    print("attrib.texcoords = ", len(attrib.texcoords))
    shapes = reader.GetShapes()
    print("Num shapes: ", len(shapes))
  
    mesh_info =  []

    for shape in shapes:
        print(shape.name)
        print("num_indices = {}".format(len(shape.mesh.indices)))

        vertices = []
        normals = []
        uvCoords = []

        for idxs in shape.mesh.indices:
            vertices.extend(attrib.vertices[3*idxs.vertex_index:3*idxs.vertex_index+3])
            normals.extend(attrib.vertices[3*idxs.normal_index:3*idxs.normal_index+3])
            uvCoords.extend(attrib.texcoords[2*idxs.texcoord_index:2*idxs.texcoord_index+2])

        mesh_info.append(Mesh(vertices,normals,uvCoords))
    return mesh_info
    # print(f"ordered vertices = {vertices}")
    # sys.exit(-1)
        # vaoID = createVAO()
        # bindIndicesToBuffer([x for x in range(len(shape.mesh.indices))])
        # storeDataInVBO(0,3,vertices)
        # storeDataInVBO(1,3,normals)
        # unbindVAO()
        # return BasicModel(vao=vaoID,size = len(vertices))


def load_model_from_file_1(filename):
    # Create reader.
    reader = tinyobjloader.ObjReader()
    ret = reader.ParseFromFile(filename)
    if ret == False:
        print("Warn:", reader.Warning())
        print("Err:", reader.Error())
        print("Failed to load : ", filename)
        sys.exit(-1)
    if reader.Warning():
        print("Warn:", reader.Warning())

    attrib = reader.GetAttrib()
    print("attrib.vertices = ", len(attrib.vertices))
    print("attrib.normals = ", len(attrib.normals))
    print("attrib.texcoords = ", len(attrib.texcoords))

    materials = reader.GetMaterials()
    print("Num materials: ", len(materials))
    for m in materials:
        print(m.name)
        print(m.diffuse)

    shapes = reader.GetShapes()
    print("Num shapes: ", len(shapes))
    for shape in shapes:
        print(shape.name)
        print("num_indices = {}".format(len(shape.mesh.indices)))
        #for (i, idx) in enumerate(shape.mesh.indices):
        #    print("[{}] v_idx {}".format(i, idx.vertex_index))
        #    print("[{}] vn_idx {}".format(i, idx.normal_index))
        #    print("[{}] vt_idx {}".format(i, idx.texcoord_index))

        v_idx = [x.vertex_index for x in shape.mesh.indices]
        print(f"indices = [{v_idx}]")
        print(f"vertices = {attrib.vertices}")
        vertex_list = []
        normal_list = [0,] * len(shape.mesh.indices)
        for face in range(len(shape.mesh.indices)//3):
            idx = (shape.mesh.indices[3*face],
            shape.mesh.indices[3*face+1],
            shape.mesh.indices[3*face+2])

            vertex_indices  = [x.vertex_index for x in idx]
            normal_indices  = [x.normal_index for x in idx]
            print(f"[{face}] = ( {vertex_indices}, {normal_indices})")
            #print(idx.vertex_index,idx.normal_index,)
            
            p1 = glm.vec3(attrib.vertices[3*vertex_indices[0]],
            attrib.vertices[3*vertex_indices[0]+1],
            attrib.vertices[3*vertex_indices[0]+2])

            p2 = glm.vec3(attrib.vertices[3*vertex_indices[1]],
            attrib.vertices[3*vertex_indices[1]+1],
            attrib.vertices[3*vertex_indices[1]+2])

            p3 = glm.vec3(attrib.vertices[3*vertex_indices[2]],
            attrib.vertices[3*vertex_indices[2]+1],
            attrib.vertices[3*vertex_indices[2]+2])

            for v in range(3):
                    vertex_list.append(attrib.vertices[3*vertex_indices[v]])
                    vertex_list.append(attrib.vertices[3*vertex_indices[v]+2])
                    vertex_list.append(attrib.vertices[3*vertex_indices[v]+1])

            
            
            for v in range(3):
                    normal_list.append(attrib.normals[3*normal_indices[v]])
                    normal_list.append(attrib.normals[3*normal_indices[v]+2])
                    normal_list.append(attrib.normals[3*normal_indices[v]+1])
            
        print(f"vertices = {vertex_list}")
        vaoID = createVAO()
        bindIndicesToBuffer([x for x in range(len(shape.mesh.indices))])
        storeDataInVBO(0,3,vertex_list)
        storeDataInVBO(1,3,normal_list)
        unbindVAO()
        return BasicModel(vao=vaoID,size = len(attrib.vertices))