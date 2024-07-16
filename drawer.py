import turtle
class Drawer(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.pu()
    def move(self, x, y,text):
        self.teleport(x, y)
        self.write(text)