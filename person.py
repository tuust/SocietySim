from pyglet import graphics
from pyglet.shapes import Rectangle
from pyglet.gl import *
from phys import physObject
import math
from random import randint

class tooline:
    def __init__(self, size=1):
        self.asukoht = [0,0]
        self.x, self.y = randint(-50,50), randint(-50,50)#self.asukoht[0], self.asukoht[1]
        self.vx = False; self.vy = False
        # x,z = self.asukoht[0], self.asukoht[1]; y = 0
        # X,Y,Z = x+size,y+size,z+size
        # color = ('c3f', (1,1,1)*4)
        # self.object = Rectangle(20, 20, 5, 5, batch=self.batch)
        # self.object.rotation = 33
        
    def draw(self):
        if round(self.x) != self.asukoht[0] or round(self.y) != self.asukoht[1]:
            # print(abs(abs(self.asukoht[0])-abs(self.x)), abs(abs(self.asukoht[1])+abs(self.y)))
            if self.vx:
                if self.x < self.asukoht[0]: self.x += 0.1
                else: self.x -= 0.1
                self.count += 1
                if self.count == 100: self.vx = False
            elif self.vy:
                if self.y < self.asukoht[1]: self.y += 0.1
                else: self.y -= 0.1
                self.count += 1
                if self.count == 100: self.vy = False
            elif abs(abs(self.asukoht[0])-abs(self.x)) >= abs(abs(self.asukoht[1])+abs(self.y)): self.vx = True; self.count = 0
            else: self.vy = True; self.count = 0

        # Kera renderdamine ja joonistamine
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
            
            glPushMatrix()
            glTranslatef(self.x, 1.2*r, self.y)
            glBegin(GL_QUAD_STRIP)
            for j in range(longs+1):
                lng = 2 * math.pi * (j+1) / longs
                x = math.cos(lng)
                y = math.sin(lng)
                
                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(r * x * zr0, r * y * zr0, r * z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(r * x * zr1, r * y * zr1, r * z1)
            glEnd()
            glPopMatrix()
    # @asukoht.setter
    # def asukoht(self, coords)

class opilane:
    def __init__(self):
        print('waow')

class vanur:
    def __init__(self):
        print('waow')

class tootu:
    def __init__(self):
        print('waow')