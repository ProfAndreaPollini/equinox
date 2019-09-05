
from pyglet import image 

class Texture:
    _textures = []

    def __init__(self, filename):
        self.image = image.load(filename)
        self.texture = self.image.get_texture()
        Texture._textures.append(self.texture.id)
