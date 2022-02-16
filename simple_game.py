from tkinter import *
import random

class Entity:
    
    positions = []
    
    def __init__(self, c, x, y, size, color):
        self.c, self.x, self.y, self.size, self.color = c, x, y, size, color
        self.draw()
    
    @classmethod
    def correct_position(cls, x, y, x1, y1):
        # print('input pos', x, y, x1, y1)
        
        def find_pos(x, y, x1, y1, posi):
            for i in posi:
                temp = []
                if (i[0] <= x <= i[2] or i[0] <= x1 <= i[2]) and (i[1] <= y <= i[3] or i[1] <= y1 <= i[3]):
                    return i
            return []
           
        p = find_pos(x, y, x1, y1, cls.positions)
        if p != []:
            left_d = x - p[0]
            up_d = y - p[1]
            
            if left_d >= up_d:
                if left_d >= 0:
                    # print('sended coords l+', x + (x1 - x), y, x1 + (x1 - x), y1)
                    try:
                        return cls.correct_position(x + (x1 - x), y, x1 + (x1 - x), y1)
                    except:
                        pass
                elif left_d <= 0:
                    # print('sended coords l-', x + (x1 - x), y, x1 + (x1 - x), y1)
                    try:
                        return cls.correct_position(x - (x1 - x), y, x1 - (x1 - x), y1)
                    except:
                        pass
            else:
                if up_d >= 0:
                    try:
                    # print('sended coords u+', x + (x1 - x), y, x1 + (x1 - x), y1)
                        return cls.correct_position(x, y + (y1 - y), x1, y1 + (y1 - y))
                    except:
                        pass
                elif up_d <= 0:
                    # print('sended coords u-', x + (x1 - x), y, x1 + (x1 - x), y1)
                    try:
                        return cls.correct_position(x, y - (y1 - y), x1, y1 - (y1 - y))
                    except:
                        pass
            
        # print(cls.positions)
        cls.positions.insert(0, [x, y, x1, y1])
        # print('found res', cls.positions)
        return [x, y, x1, y1]
    
class Player(Entity):
    def draw(self):
        x, y, x1, y1 = self.correct_position(self.x - self.size / 2, self.y - self.size / 2, self.x + self.size / 2, self.y + self.size / 2)
        self.c.create_oval(x, y, x1, y1, fill=self.color)

class Bot(Entity):
    def draw(self):
        x, y, x1, y1 = self.correct_position(self.x - self.size / 2, self.y - self.size / 2, self.x + self.size / 2, self.y + self.size / 2)
        self.c.create_rectangle(x, y, x1, y1, fill=self.color)
        
width = 500
height = 500

root = Tk(f'{width}x{height}')
canvas = Canvas(root, width = width, height = height)

p1 = Player(canvas, 30, 30, 50, 'RED')
p1 = Player(canvas, 30, 30, 50, 'BLACK')
p2 = Player(canvas, 470, 30, 50, 'GREEN')
p3 = Player(canvas, 30, 470, 50, 'BLUE')
p4 = Player(canvas, 470, 470, 50, 'WHITE')

for _ in range(5):
    width, length = random.randint(100, 300), random.randint(100, 300)
    bot = Bot(canvas, width, length, 50, 'GREY')

canvas.pack()
root.mainloop()