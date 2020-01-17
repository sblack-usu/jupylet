"""
    jupylet/sprite.py
    
    Copyright (c) 2020, Nir Aides - nir@winpdb.org

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
       list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import pyglet

import PIL.Image

import numpy as np


def image_from(o, width=None, height=None, crop=True):
    
    if type(o) is str:
        return image_from_resource(o)
    
    if isinstance(o, np.ndarray):
        #return image_from_array(o)
        o = PIL.Image.fromarray(o.astype('uint8'))
    
    if isinstance(o, PIL.Image.Image):
        return image_from_pil(o)
    
    return o

    
def image_from_resource(name):
    
    try:
        return pyglet.resource.image(name)
    
    except pyglet.resource.ResourceNotFoundException:
        pyglet.resource.reindex()
        return pyglet.resource.image(name)

    
def image_from_array(array):
    
    array = array.astype('uint8')

    height, width = array.shape[:2]
    
    if len(array.shape) == 2:
        channels = 1
    else:
        channels = array.shape[-1]
        
    mode = ['L', None, 'RGB', 'RGBA'][channels-1]
        
    return pyglet.image.ImageData(width, height, mode, array.reshape(-1).tobytes(), -width*channels)


def image_from_pil(image):
    
    width, height = image.size 
    channels = {'L': 1, 'RGB': 3, 'RGBA': 4}[image.mode]
        
    return pyglet.image.ImageData(width, height, image.mode, image.tobytes(), -width*channels)


class Sprite(pyglet.sprite.Sprite):
    
    def __init__(self,
                 img, x=0, y=0,
                 blend_src=pyglet.gl.GL_SRC_ALPHA,
                 blend_dest=pyglet.gl.GL_ONE_MINUS_SRC_ALPHA,
                 batch=None,
                 group=None,
                 usage='dynamic',
                 subpixel=True,
                 scale=1.0):

        img = image_from(img)
            
        super(Sprite, self).__init__(img, x, y,
                 blend_src,
                 blend_dest,
                 batch,
                 group,
                 usage,
                 subpixel)

        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        
        self.scale = scale
        self.rotation = 0

    @property
    def image(self):
        return pyglet.sprite.Sprite.image.fget(self)
    
    @image.setter
    def image(self, img):
        
        img = image_from(img)
            
        pyglet.sprite.Sprite.image.fset(self, img)
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.rotation = self.rotation
        
    def distance_to(self, o, pos=None):

        x, y = pos or (o.x, o.y)
        
        dx = x - self.x
        dy = y - self.y

        return (dx ** 2 + dy ** 2) ** 0.5
    
    def angle_to(self, o, pos=None):
        
        qd = {
            (True, True): 0,
            (True, False): 180,
            (False, False): 180,
            (False, True): 360,
        }
        
        x, y = pos or (o.x, o.y)
        
        dx = x - self.x
        dy = y - self.y

        return math.atan(dy / (dx or 1e-7)) / math.pi * 180 + qd[(dy >= 0, dx >= 0)]

    @property
    def top(self):
        return self.y + self.height - self.image.anchor_y
        
    @property
    def right(self):
        return self.x + self.width - self.image.anchor_x
        
    @property
    def bottom(self):
        return self.y - self.height + self.image.anchor_y
        
    @property
    def left(self):
        return self.x - self.width + self.image.anchor_x
        
    def wrap_position(self, width, height, margin=50):
        self.x = (self.x + margin) % (width + 2 * margin) - margin
        self.y = (self.y + margin) % (height + 2 * margin) - margin

    def clip_position(self, width, height, margin=0):
        self.x = max(-margin, min(margin + width, self.x))
        self.y = max(-margin, min(margin + height, self.y))


def canvas2sprite(c):
    
    a = c.get_image_data()
    b = a.tostring()
    x = ctypes.string_at(id(b)+20, len(b))
    d = pyglet.image.ImageData(a.shape[1], a.shape[0], 'RGBA', x)
    s = Sprite(d)
    
    return s

