from equinox.core import equinox_create_window,equinox_run,key
from equinox.models import BasicModel,cleanup,Cube,Terrain,load_model_from_file
from equinox.render import Renderer,renderer_init,Camera

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
window,fps_display = equinox_create_window(W,H,debug_fps=True)

models = []

# for i in range(10):
#    models.append(load_model_from_file("cube.obj"))#Cube.create())
models.append(load_model_from_file("cube.obj"))
terrain = Terrain(800)
terrainModel  = terrain.create()
models.append(terrainModel)

renderer = Renderer()
camera = Camera(W,H)




@window.event
def on_draw():
    
    renderer.prepare()
   
    renderer.render(camera,models)
    #fps_display.draw()
   

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
    
    #camera.update()

@window.event 
def on_mouse_motion(x, y, dx, dy):
    sensitivity = 0.05
    xoffset = dx
    yoffset = dy
    xoffset *= sensitivity
    yoffset *= sensitivity



def update(dt):
    [update_model(model) for model in models if model != terrainModel] 

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
