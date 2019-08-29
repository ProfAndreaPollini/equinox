import pyglet
from .utils import Borg

class CameraEvents(pyglet.event.EventDispatcher):

    NONE = 0
    TRANSLATION = 1
    ROTATION = 2

    #constants
    SENSITIVITY = 0.5

    def __init__(self):
        super().__init__()
        self.status = CameraEvents.NONE

    def move(self,x,y,dx,dy):
        if self.status == CameraEvents.NONE: return

        if self.status == CameraEvents.TRANSLATION:
            self.dispatch_event('on_camera_move',x,y,dx,dy,self.status)
        elif self.status == CameraEvents.ROTATION:
            self.dispatch_event('on_camera_move',x,y,dx,dy,self.status)

    def zoom(self,is_zoom_in=True):
        self.dispatch_event('on_zoom',is_zoom_in)

    def mouse_reset(self):
        self.status = CameraEvents.NONE
        print("RESET")

    def mouse_press(self,button):
        if button == pyglet.window.mouse.LEFT:
            print("TRANSLATION")
            self.status = CameraEvents.TRANSLATION
        elif button == pyglet.window.mouse.RIGHT:
            print("ROTATION")
            self.status = CameraEvents.ROTATION

     

CameraEvents.register_event_type('on_camera_move')
CameraEvents.register_event_type('on_zoom')


class EquinoxEvents(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.cameraEvents = CameraEvents()
    def __str__(self): return self.cameraEvents


equinoxEvents = EquinoxEvents()