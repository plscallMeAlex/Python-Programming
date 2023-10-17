import turtle

class Point(object):
    def __init__(self):
        self.pt_list = []
        points_input = input("Input pairs of points (x1 y1 x2 y2 ...): ").split()
        for i in range(0, len(points_input), 2):
            x, y = float(points_input[i]), float(points_input[i + 1])
            self.pt_list.append((x, y))   
    def drawPoints(self):
        for x, y in self.pt_list:
            turtle.penup()
            turtle.goto(x,y)
            turtle.dot(5)

class Rectangle2D(Point):
    def __init__(self):
        super().__init__()
        self.drawPoints()
        self.getRectangle()

    def getRectangle(self):
        x_coords = [point[0] for point in self.pt_list]
        y_coords = [point[1] for point in self.pt_list]
        self.x_min = min(x_coords)
        self.x_max = max(x_coords)
        self.y_min = min(y_coords)
        self.y_max = max(y_coords)
        self.width = self.x_max - self.x_min
        self.height = self.y_max - self.y_min
        
        centre_x = (self.x_max + self.x_min)/2
        centre_y = (self.y_max + self.y_min)/2
        
        turtle.penup()
        turtle.goto(self.x_min, self.y_min)
        turtle.pendown()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)
        print(f"The bonding rectangle is center at ({centre_x}, {centre_y}) with width {self.width} and height {self.height}")

c = Rectangle2D()
turtle.done()
