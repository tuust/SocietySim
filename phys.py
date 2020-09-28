from pyglet import graphics
class physObject():
    def __init__(self):
        self.v_x, self.v_y = 0., 0.

    def update(self, dt):
        self.x += self.v_x * dt
        self.y += self.v_y * dt