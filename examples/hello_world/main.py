from equinox.core import equinox_create_window,equinox_run
from equinox.models import BasicModel,cleanup
from equinox.render import Renderer,renderer_init,Camera

from random import random

vertices = (
    -0.5,0.5,0.0,
    -0.5,-0.5,0.0,
    0.5,0.5,0.0
)



W = 1600
H = 800

# Direct OpenGL commands to this window.
window = equinox_create_window(W,H)
#glEnable(GL_DEPTH_TEST)
#glDepthFunc(GL_LESS)
#window.set_caption("TEST")


#model = BasicModel.create(vertices)

models = []

for i in range(10):
    models.append(BasicModel.create(vertices))

renderer = Renderer()
camera = Camera(W,H)


@window.event
def on_draw():
   
    renderer.prepare()
   
    renderer.render(camera,models)
   
   
def update(dt):
    for model in models:
        update_model(model)

def update_model(model):
    model.rotate(0.5)
    dx = 2.0*random()-1
    dy =  2.0*random()-1
    dz = 2.0*random()-1

    if (dx >= 0.0): 
        dx = 0.01 
    else: dx = -0.01

    if (dy >= 0.0): 
        dy = 0.01 
    else: dy = -0.01

    if (dz >= 0.0): 
        dz = 0.01 
    else: dz = -0.01

    model.move(dx,dy,dz)
    model.update()

equinox_run(update)

cleanup()
