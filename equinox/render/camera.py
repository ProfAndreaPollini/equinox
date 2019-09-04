from math import sin, cos

from pyglet.gl import *  # pylint: disable=unused-wildcard-import,wildcard-import,redefined-builtin
import glm

from equinox.core.utils import Observer
from equinox.core.events import equinoxEvents


class Camera(Observer):

    def __init__(self, W, H):
        super().__init__(equinoxEvents.cameraEvents)
        self.screen_width = W
        self.screen_height = H  

        self.yaw = 0.0
        self.pitch = 0.0
        self.pos = glm.vec3(0.0, 1.0, 10.0)
        self.update_front()
        self.up = glm.vec3(0.0, 1.0, 0.0)

    def update_front(self):
        """"update front vector from pitch and yaw values"""
        new_front = glm.vec3(cos(glm.radians(self.pitch)) * cos(glm.radians(self.yaw)),\
                sin(glm.radians(self.pitch)),\
                cos(glm.radians(self.pitch)) * sin(glm.radians(self.yaw)))
        self.front = glm.normalize(new_front)

    def on_camera_move(self, x, y, dx, dy, status): # pylint: disable=unused-argument
        """camera movement event callback"""
        if status == equinoxEvents.cameraEvents.TRANSLATION:
            #print("move!! ",dx,dy)
            right = glm.normalize(glm.cross(self.front, self.up))
            self.pos += 0.1 * dx * right 
            self.pos += 0.1 * dy * self.up 
        elif status == equinoxEvents.cameraEvents.ROTATION:
            self.yaw += dx * equinoxEvents.cameraEvents.SENSITIVITY
            self.pitch += dy * equinoxEvents.cameraEvents.SENSITIVITY

            if self.pitch > 89.0:
                self.pitch = 89.0
            if self.pitch < -89.0:
                self.pitch = -89.0
            self.update_front()

        elif status == equinoxEvents.cameraEvents.ZOOM:
            d_front = glm.normalize(self.front) * dy * equinoxEvents.cameraEvents.SENSITIVITY
            self.pos += d_front

    def on_zoom(self, is_zoom_in):
        zoom_vel = 0.1
        direction = -1
        if is_zoom_in:
            direction *= -1
        self.pos += zoom_vel*self.front *direction

    def viewMatrix(self):
        return  glm.lookAt(self.pos, self.pos + self.front, self.up)

    def projectMatrix(self):
        projection = glm.perspective(glm.radians(45.0),\
            self.screen_width / self.screen_height, 0.1, 100.0)
        return projection 
