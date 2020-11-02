from pyglet import graphics
from pyglet.gl import *
from pyglet import resource
from pyglet import image
from os import listdir

class kodu:
    path = 'res/kodu/'
    files = listdir(path)
    textures = []
    for f in files:
        tex = image.load(str(path+f)).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST_MIPMAP_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        glGenerateMipmap(GL_TEXTURE_2D)
        # glFramebufferParameterf(GL_DRAW_FRAMEBUFFER, GL_FRAMEBUFFER_DEFAULT_WIDTH, 512)
        # glFramebufferParameterf(GL_DRAW_FRAMEBUFFER, GL_FRAMEBUFFER_DEFAULT_HEIGHT, 512)
        # glFramebufferParameterf(GL_DRAW_FRAMEBUFFER, GL_FRAMEBUFFER_DEFAULT_SAMPLES, 4)
        textures.append((graphics.TextureGroup(tex), tex.tex_coords))

    batch = graphics.Batch()
    #textures = [ for f in files if not ) if not ] 

    # def load_tex(self, file):
    #     tex = image.load(file).get_texture()
    #     # tex.tex_coords = self.tex_coords[1]
    #     # glEnable(tex.target)
    #     # glBindTexture(tex.target, tex.id)
    #     glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    #     glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    #     self.tex_coords = tex.tex_coords
    #     return graphics.TextureGroup(tex)
    def build(self, x, y, z, size=1):
        X,Y,Z = x+size,y+size,z+size
        #tex_coords = ('t2f', (0,0, 0.796875,0, 0.796875,0.796875, 0,0.796875))
        #tex = self.load_tex('res/kodu/wall1.jpg')
        color = ('c3f', (1,1,1)*4)
        self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3i',(X,y,z, x,y,z, x,Y,z, X,Y,z)), color, ('t3f',self.textures[0][1])) #back
        self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3i',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z)), color, ('t3f',self.textures[0][1])) #front
        self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3i',(x,y,z, x,y,Z, x,Y,Z, x,Y,z)), color, ('t3f',self.textures[0][1])) #left
        self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3i',(X,y,Z, X,y,z, X,Y,z, X,Y,Z)), color, ('t3f',self.textures[0][1])) #right
        self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3i',(x,y,z, X,y,z, X,y,Z, x,y,Z)), color, ('t3f',self.textures[0][1])) # bottom
        # self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3i',(X,Y,Z, X,Y,z, x,Y,z, x,Y,Z)), color, ('t3f',self.textures[0][1])) #top
    def draw(self):
        self.batch.draw()

class tee:
    path = 'res/tee/'
    files = listdir(path)
    textures = []
    for f in files:
        #tex = image.TileableTexture.create_for_image(image.load(str(path+f)))
        tex = image.load(str(path+f)).get_texture()
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        glGenerateMipmap(GL_TEXTURE_2D)
        # glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
        # glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE )
        # glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE )
        textures.append((graphics.TextureGroup(tex), tex.tex_coords))
    batch = graphics.Batch()
    def __init__(self, x, y, z, size=1):
        X,Y,Z = x+size,y+size,z+size
        color = ('c3f', (1,1,1)*4)
        self.batch.add(4, GL_QUADS, self.textures[0][0], ('v3f', (x, y, z,  X, y, z,  X, y, Z,  x, y, Z)), color, ('t3f',self.textures[0][1])) # bottom
    def draw(self):
        self.batch.draw()

class kool:
    def __init__(self):
        print('lol')

class too:
    def __init__(self):
        print('lol')

class park:
    def __init__(self):
        print('lol')

class haigla:
    def __init__(self):
        print('lol')