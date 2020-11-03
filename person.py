from pyglet import graphics, image, clock
from pyglet.shapes import Rectangle
from pyglet.gl import *
import math
from random import randint
from os import listdir

class tooline:
    path = 'res/inimene/'
    files = listdir(path)
    textures = []
    for f in files:
        tex = image.load(str(path+f)).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        glGenerateMipmap(GL_TEXTURE_2D)
        textures.append((graphics.TextureGroup(tex), tex.tex_coords))
    batch = graphics.Batch()
    def __init__(self, asukoht, size=1):
        self.size = size
        self.asukoht = asukoht
        self.coords = (-size*10+asukoht[0]*size*2+size*1.5,-size*10+asukoht[1]*size*2+size/2)
        self.aeg = 10
        self.x, self.y = self.coords[0], self.coords[1]
        self.vx = False; self.vy = False

        # Kera objekti tegemine
        lats = 10
        longs = 10
        r = 2
        for i in range(lats):
            lat0 = math.pi * (-0.5 + i / lats)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)

            lat1 = math.pi * (-0.5 + (i+1) / lats)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)
            

            # glBegin(GL_QUAD_STRIP)
            for j in range(longs+1):
                lng = 2 * math.pi * (j+1) / longs
                x = math.cos(lng)
                y = math.sin(lng)
                self.batch.add(2, GL_QUAD_STRIP, None, ('v3f', (r * x * zr0, r * y * zr0, r * z0, r * x * zr1, r * y * zr1, r * z1)))
                # unbanched viis kera loomiseks, ülimalt CPU kulukas
                # glNormal3f(x * zr0, y * zr0, z0)
                # glVertex3f(r * x * zr0, r * y * zr0, r * z0)
                # glNormal3f(x * zr1, y * zr1, z1)
                # glVertex3f(r * x * zr1, r * y * zr1, r * z1)
            # glEnd()
    
    def draw(self, scale):
        # Liikumise arvutamine
        if round(self.x) != self.coords[0] or round(self.y) != self.coords[1]:
            if self.vx:
                if self.x < self.coords[0]: self.x += 0.1
                else: self.x -= 0.1
                self.count += 1
                if self.count == 10*scale: self.vx = False
            elif self.vy:
                if self.y < self.coords[1]: self.y += 0.1
                else: self.y -= 0.1
                self.count += 1
                if self.count == 10*scale: self.vy = False
            elif max(self.coords[0]-self.x, self.x-self.coords[0]) >= max(self.coords[1]-self.y, self.y-self.coords[1]): self.vx = True; self.count = 0
            else: self.vy = True; self.count = 0
        else: self.vx = False; self.vy = False

        # Liikumine määratud asukohta
        glPushMatrix()
        if self.staatus == 0: glColor3ub(102, 255, 102)
        elif self.staatus == 1: glColor3ub(255, 102, 102)
        else: glColor3ub(102, 255, 255)
        glTranslatef(self.x, 0.2*scale, self.y)
        self.batch.draw()
        glPopMatrix()

    @property
    def asukoht(self):
        return self._asukoht
    
    @asukoht.setter
    def asukoht(self, coords):
        print(coords)
        self.coords = (-self.size*10+coords[0]*self.size*2+self.size*1.5,-self.size*10+coords[1]*self.size*2+self.size/2)
        self._asukoht = coords

class opilane:
    def __init__(self):
        print('waow')

class vanur:
    def __init__(self):
        print('waow')

class tootu:
    def __init__(self):
        print('waow')