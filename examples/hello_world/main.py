import os, os.path
from equinox.core import equinox_create_window,equinox_run,key
from equinox.models import Model,cleanup,load_model_from_file,Entity,Mesh
from equinox.render import  Camera, MasterRenderer
 
import glm

from random import random

vertices = (
    -0.5,0.5,0.0,
    -0.5,-0.5,0.0,
    0.5,0.5,0.0
)

normals = (
    0.0,0.0,1.0,
    0.0,0.0,1.0,
    0.0,0.0,1.0
)

W = 1600
H = 800

# Direct OpenGL commands to this window.
window, fps_display = equinox_create_window(W,H,debug_fps=True)

models = []
tree_mesh =  Mesh.mesh_from_file(os.path.join(os.path.dirname(__file__),"tree.obj"))


terrain_mesh = Mesh.mesh_from_file(os.path.join(os.path.dirname(__file__),"terrain.obj"))
terrain = Entity(terrain_mesh)
terrain.pos = glm.vec3(-20, 0, -20)


for i in range(100):
   
    tree = Entity(tree_mesh)
    
    tree.move_to(glm.vec3(200*random()-100,0.0,200*random()-100))
    print(f"tree ({tree}) [{i}] = {tree.pos}")
    terrain.move_to(glm.vec3(20*random()-10,0.0,20*random()-10))
    models.append(tree)

models.append(terrain)

renderer = MasterRenderer()
camera = Camera(W, H)


@window.event
def on_draw():

    renderer.prepare()

    renderer.render(camera)

   

@window.event  
def on_key_press(symbol, modifiers):
    print("KEYPRESSED: ",symbol, modifiers)
    cameraSpeed = 0.05


    if symbol == key.W:
        camera.pos += cameraSpeed * camera.front*2
    if symbol == key.S:
        camera.pos -= cameraSpeed * camera.front*2
    if symbol == key.A:
        camera.pos -= glm.normalize(glm.cross(camera.front, camera.up)) * cameraSpeed
    if symbol == key.D:
        camera.pos += glm.normalize(glm.cross(camera.front, camera.up)) * cameraSpeed
    
    

@window.event 
def on_mouse_motion(x, y, dx, dy):
    sensitivity = 0.05
    xoffset = dx
    yoffset = dy
    xoffset *= sensitivity
    yoffset *= sensitivity



def update(dt):
    pass#[update_model(model) for model in models]#if model != terrainModel] 

def update_model(model):
    
    dx = 2.0*random()-1
    dy =  2.0*random()-1
    dz = 2.0*random()-1

    model.rotate(dx,dy,dz)

    if (dx >= 0.0): 
        dx = 0.01 
    else: dx = -0.01

    if (dy >= 0.0): 
        dy = 0.01 
    else: dy = -0.01

    if (dz >= 0.0): 
        dz = 0.01 
    else: dz = -0.01
    model.rotate(dx,dy,dz)
    model.move(dx,dy,dz)
    model.update()

equinox_run(update)

cleanup()
