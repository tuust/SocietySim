import pyglet as pl
import person as p
import building as b
import math
import numpy as np
# import ratcave as rc  # shaderitega blenderi objektid

class Player():
    def __init__(self, pos=(0,0,0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.y_max = 50

    def edge_smoothing(self, axis, scale, key, params, tilt, tilt_b):
        tilt_v = (-math.exp(-0.07*getattr(self,tilt))+1)*scale
        if getattr(self,tilt) <= 60 and key != None:
            setattr(self, tilt, getattr(self,tilt)+1)
        if (key == 'a' or key == 'w') and self.pos[axis]<params[0]: self.pos[axis] = params[0]-tilt_v
        elif (key == 'd' or key == 's') and self.pos[axis]>params[1]: self.pos[axis] = params[1]+tilt_v
        else:
            tilt_vb = math.exp(-0.07*getattr(self,tilt_b))*scale
            if self.pos[axis]<=params[0]: self.pos[axis] += tilt_vb
            else: self.pos[axis] -= tilt_vb
            setattr(self,tilt,getattr(self,tilt)-1)
            setattr(self,tilt_b,getattr(self,tilt_b)-1)
            return
        if getattr(self,tilt_b) < 60:
            setattr(self,tilt_b,getattr(self,tilt_b)+1)

 
    def camBounds(self, params, scale, dt=0, keys=None, dx=0, dy=0):
        # ---fun fact #001---
        # liites 0.1 ei pruugi alda vastuseks saada oodatud tulemuse, sest arv 0.1 on hoitud arvutis kui
        # 1000000000000000055511151231257827021181583404541015625 ning vahepeal võib "ebatäpsus" jääda arvutusse sisse e.g 0.1 + 0.2 = 0.30000000000000004
        # ja kehtib võrdus 0.1 + 0.2 != 0.3 . See ei ole otseselt bug, vaid laialt kasutuse olevate floating point standard (Double Presicion Number (binary64)),
        # mille täpsus on 52 biti. Niimoodi toimivad ka teised programmeerimiskeeled.
        # --- fun fact acquiered ---
        
        # kaamera üles alla liigutamise piirid ja kallutamine kõrguse muutusega
        params = (params[0]*scale, params[1]*scale)
        if self.pos[1] >= 1.2*scale and self.pos[1] <= self.y_max:
            self.rot[0] -= dy/scale
        elif self.pos[1] <= 1.2*scale:
            self.pos[1] = 1.2*scale
        # Seab mapi äärele piiri, kuid laseb exponentsiaalsel kirusel minna kuni (-e^60)+1 ja samamoodi tuleb tagasi kui nuppu peal ei hoia
        edge = False
        if keys != None:
            if self.pos[0]<=params[0] or self.pos[0]>=params[1]:
                edge = True
                if keys[pl.window.key.A]: self.edge_smoothing(0, scale, 'a', params,'tilt','tilt_b')
                elif keys[pl.window.key.D]: self.edge_smoothing(0, scale, 'd', params,'tilt','tilt_b')
                else: self.edge_smoothing(0, scale, None, params,'tilt','tilt_b')
            if self.pos[2]<=params[0] or self.pos[2]>=params[1]:
                edge = True
                if keys[pl.window.key.W]: self.edge_smoothing(2, scale, 'w', params,'ztilt','ztilt_b')
                elif keys[pl.window.key.S]: self.edge_smoothing(2, scale,'s', params,'ztilt','ztilt_b')
                else: self.edge_smoothing(2, scale, None, params,'ztilt','ztilt_b')

        if not edge:
            self.tilt = 1
            self.ztilt = 1
            self.tilt_b = 60
            self.ztilt_b = 60

    def mouse_motion(self, dx, dy, mouse, params):
        # hiirega liikumise kalkuleerimine, kui mouse mode'is
        dx/=8; dy /=8; self.rot[0]+=dy; self.rot[1]-=dx
        if self.rot[0]>90: self.rot[0] = 90
        elif self.rot[0]<-90: self.rot[0] = -90
        # vasak hiire klahv on võrdne W'ga
        if mouse[pl.window.mouse.LEFT]: 
            rotY = -self.rot[1]/180*math.pi # glRotatef võtab radiaane
            rotX = self.rot[0]/180*math.pi
            dx, dy, dz = math.sin(rotY)*0.1, rotX*0.1, math.cos(rotY)*0.1
            self.pos[0] +=dx; self.pos[1] += dy; self.pos[2] -=dz

    def update(self, dt, keys, params, scale):
        # nuppudega liikumise kalkuleerimine
        rotY = -self.rot[1]/180*math.pi # glRotatef võtab radiaane
        rotX = self.rot[0]/180*math.pi
        dx, dy, dz = math.sin(rotY)*0.1*scale, rotX*0.1*scale, math.cos(rotY)*0.1*scale
        # kaamera liigutamine kaasarvatud kaamera nurk
        if keys[pl.window.key.W]: self.pos[0] +=dx; self.pos[2] -=dz # self.pos[1] += dy
        if keys[pl.window.key.S]: self.pos[0] -=dx; self.pos[2] +=dz # self.pos[1] -= dy
        if keys[pl.window.key.A]: self.pos[0] -=dz; self.pos[2] -=dx
        if keys[pl.window.key.D]: self.pos[0] +=dz; self.pos[2] +=dx

        # kaamera yles alla
        dy = 0
        s = dt*10*scale
        if keys[pl.window.key.LCTRL]: self.pos[1] -= s; dy = -s
        if keys[pl.window.key.LSHIFT]: self.pos[1] += s; dy = s
        # print(scene.camera.position.xyz)
        # scene.camera.position.xyz = self.pos[0]*0.01,self.pos[1]*0.01,self.pos[2]*0.01
        # scene.camera.rotation.xyz = self.rot[0],self.rot[1],0
        self.camBounds(params, scale, dy=dy*10, keys=keys)

class simwin(pl.window.Window):
    ''' akna kontrollimine ning kõik muu graafika konstrueerimine sellesse '''
    def __init__(self, city, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(500, 300)
        self.fps = pl.window.FPSDisplay(self)
        i = round(sum(city.shape)/2); self.gridParams = (-i, i) # linna suurus

        pl.gl.glClearColor(123/255,221/255,240/255,1) #background color
        pl.gl.glEnable(pl.gl.GL_DEPTH_TEST)
        #pl.gl.glEnable(pl.gl.GL_CULL_FACE)
        self.fov = 90
        self.scale = 10
        self.keys = pl.window.key.KeyStateHandler()
        self.mouse = pl.window.mouse.MouseStateHandler()
        self.push_handlers(self.keys, self.mouse)
        pl.clock.schedule_interval(self.update, 1/120)
        self.player = Player((0.5*self.scale,max(city.shape)*self.scale,-0.5*self.scale),(-90,0))
        self.objects = {'buildings': None, 'tee': None, 'tool': []}
        inimesed = [p.tooline() for x in range(50)]
        for y in range(self.gridParams[0], self.gridParams[1]):
            for x in range(self.gridParams[0]+1, self.gridParams[1]):
                if y % 2 == 0 and x % 2 != 0:
                    build = b.kodu(x*self.scale, 0, y*self.scale, self.scale); key = 'buildings'
                else:
                    build = b.tee(x*self.scale, 0, y*self.scale, self.scale); key = 'tee'
                if self.objects[key] == None: self.objects[key] = build
        for inimene in inimesed:
            # if None in self.objects.values():
            if isinstance(inimene, p.tooline):
                self.objects['tool'].append(inimene)
            else: break

    def push(self, pos, rot):
        pl.gl.glPushMatrix()
        # päriselt kaamera liigutamine ning keeramine
        pl.gl.glRotatef(-rot[0],1,0,0)
        pl.gl.glRotatef(-rot[1],0,1,0)
        pl.gl.glTranslatef(-pos[0],-pos[1],-pos[2])

    def Projection(self):
        pl.gl.glMatrixMode(pl.gl.GL_PROJECTION)
        pl.gl.glLoadIdentity()

    def Model(self):
        pl.gl.glMatrixMode(pl.gl.GL_MODELVIEW)
        pl.gl.glLoadIdentity()

    def set3d(self):
        self.Projection()
        pl.gl.gluPerspective(self.fov,self.width/self.height,0.05,1000) # FOV, aspect ratio, min render distance, max render dist
        self.Model()

    def set2d(self):
        self.Projection()
        pl.gl.gluOrtho2D(0,self.width,0,self.height)
        self.Model()

    # hiir kaob ära, et indentifitseerida hiirega kaamera liigutamist
    # mouse mode
    def setLock(self, state): self.lock = state; self.set_exclusive_mouse(state)
    lock = False; mouse_lock = property(lambda self:self.lock,setLock)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_lock: self.player.mouse_motion(dx, dy, self.mouse, self.gridParams)

    def on_key_press(self, KEY, MOD):
        if KEY == pl.window.key.ESCAPE: self.close()
        elif KEY == pl.window.key.SPACE: self.mouse_lock = not self.mouse_lock

    def update(self, dt):
        self.player.update(dt, self.keys, self.gridParams, self.scale)
        if self.mouse_lock: self.player.mouse_motion(0, 0, self.mouse, self.gridParams)

    def on_draw(self):
        # --- fun fact #002 ---
        # Koodiga
        # for b in self.buildings:
        #     b.draw()
        # "joonistab" OpenGL iga kuubiku eraldi ning juba 100x100 ruudustikus on umbes 0.5 fps'i, pannes aga kõik kuubikud ühe batch'i sisse ehk
        # self.buildings.draw() on samas 100x100 ruudustikus fps umbes 800  #VoteForBatchedRendering,
        # ilmselt tuleneb see sellest, et batched rendering oskab kasutada gpu'd paremini 
        # --- fun fact acquiered ---

        self.clear()
        self.set3d()
        self.push(self.player.pos, self.player.rot)
        for key in self.objects:
            if isinstance(self.objects[key], list):
                for obj in self.objects[key]:
                    obj.draw(self.scale)
            else: self.objects[key].draw()
        pl.gl.glPopMatrix()
        
        self.fps.draw()

city = np.ones((5,5))

window = simwin(city, resizable=True, width=1280, height=720)
pl.app.run()