import pyglet
from pyglet.gl import *

from ..render import renderer_init

from ..core.events import equinoxEvents


def on_mouse_scroll(x, y, scroll_x, scroll_y):
        #print("SCROLL1: ",scroll_y) 
        equinoxEvents.cameraEvents.zoom(scroll_y >0)


def on_mouse_motion(x, y, dx, dy):  
    equinoxEvents.cameraEvents.move(x,y,dx,dy)

def on_mouse_press(x, y, button, modifiers):
    equinoxEvents.cameraEvents.mouse_press(button)

def on_mouse_release(x, y, button, modifiers):
    equinoxEvents.cameraEvents.mouse_reset()

def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    equinoxEvents.cameraEvents.move(x,y,dx,dy)

def equinox_create_window(W,H,title="",debug_fps=False):
    window = pyglet.window.Window(W,H)
    window.set_caption(title)

    window.on_mouse_scroll = on_mouse_scroll
    window.on_mouse_motion = on_mouse_motion
    window.on_mouse_press  = on_mouse_press
    window.on_mouse_release = on_mouse_release
    window.on_mouse_drag = on_mouse_drag

    
    
    if debug_fps: 
        fps_display =  pyglet.window.FPSDisplay(window=window)
        return window, fps_display
    return window



def equinox_run(update_func):

    pyglet.clock.schedule_interval(update_func, 0.1)

    pyglet.app.run()
