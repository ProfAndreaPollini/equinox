import pyglet
from pyglet.gl import *

from ..render import renderer_init


class Window(pyglet.window.Window):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
       
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        self.set_caption("TEST")
        #glViewport(0,0,W, H)
        
        

        context = pyglet.gl.get_current_context()
        #self.window = pyglet.window.Window()#context=context)
    #     #config = pyglet.gl.Config(double_buffer = True, 
    #                             depth_size = 24, 
    #                             major_version=4, 
    #                             minor_version=6, 
    #                             forward_compatible = True)

    #     self.window = pyglet.window.Window(config=config)#config=Config(major_version=4, minor_version=6))
        self.push_handlers(self)
        #renderer_init(self.window)
        print('OpenGL version:', self.context.get_info().get_version())
        print('OpenGL 3.2 support:', self.context.get_info().have_version(4,6))
        
    def on_resize(self,w,h):
        glViewport(0,0,w, h)
   
    # def on_draw(self):
    #     #self.window.clear()
        
        

    #     self.onDraw()
        

    # def onDraw(self):
    #     raise NotImplementedError()
        

    def run(self):
       pyglet.app.run()


def equinox_create_window(W,H,title=""):
    window = pyglet.window.Window(W,H)
    window.set_caption(title)

    return window



def equinox_run(update_func):

    pyglet.clock.schedule_interval(update_func, 0.1)

    pyglet.app.run()
