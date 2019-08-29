import sys


import tinyobjloader

from .basic import bindIndicesToBuffer, storeDataInVBO,BasicModel,createVAO,unbindVAO


def load_model_from_file(filename):
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
            for v in range(3):
                    vertex_list.append(attrib.vertices[3*vertex_indices[v]])
                    vertex_list.append(attrib.vertices[3*vertex_indices[v]+1])
                    vertex_list.append(attrib.vertices[3*vertex_indices[v]+2])

            
            for v in range(3):
                    normal_list.append(attrib.normals[3*normal_indices[v]])
                    normal_list.append(attrib.normals[3*normal_indices[v]+1])
                    normal_list.append(attrib.normals[3*normal_indices[v]+2])
            # normal_list.append(attrib.normals[3*idx.normal_index])
            # normal_list.append(attrib.normals[3*idx.normal_index+1])
            # normal_list.append(attrib.normals[3*idx.normal_index+2])
        #print(len(vertex_list),vertex_list[0],attrib.normals)
        print(f"vertices = {vertex_list}")
        vaoID = createVAO()
        bindIndicesToBuffer([3*x.vertex_index for x in shape.mesh.indices])
        storeDataInVBO(0,3,attrib.vertices)
        storeDataInVBO(1,3,normal_list)
        unbindVAO()
        return BasicModel(vao=vaoID,size = len(attrib.vertices))