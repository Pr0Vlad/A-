import pygame
from shapely.geometry import LineString
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.h = 0
        self.f = 0
        self.g = 0
    def __eq__(self, other):
        return self.position == other.position
def search(environment, cost, start, end, lines):
    starting = Node(None, tuple(start))
    starting.g = starting.h = starting.f = 0
    ending = Node(None, tuple(end))
    ending.g = ending.h = ending.f = 0
    open = []
    closed = []
    open.append(starting)
    while len(open) > 0:
        current = open[0]
        i = 0
        for j, item in enumerate(open):
            if item.f < current.f:
                current = item
                i = j
        #print(current.position)
        open.pop(i)
        closed.append(current)
        if current == ending:
            path = []
            current = current
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path
        children = []
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for position in moves:
            location = (current.position[0] + position[0], current.position[1] + position[1])
            currentline = LineString([(current.position[1], current.position[0]), (location[1], location[0])])
            if location[0] > (len(environment) - 1) or location[0] < 0 or location[1] > (len(environment[len(environment) - 1]) - 1) or location[1] < 0:
                continue
            #print("this is start ", current.position)
            if not LineString.intersects(currentline, line3) and not LineString.intersects(currentline, line4) and not LineString.intersects(currentline, line5) and not LineString.intersects(currentline, line6) and not LineString.intersects(currentline, line7) and not LineString.intersects(currentline, line8) and not LineString.intersects(currentline, line9):
                new = Node(current, location)
                children.append(new)
        for child in children:
            if len([closedchild for closedchild in closed if closedchild == child]) > 0:
                continue
            child.g = current.g + cost
            child.h = (((child.position[0] - ending.position[0]) ** 2) + ((child.position[1] - ending.position[1]) ** 2))
            child.f = child.g + child.h
            for opened in open:
                if child == opened and child.g > opened.g:
                    continue
            open.append(child)
if __name__ == '__main__':
    row, col = (41, 41)
    environment = [[0 for i in range(row)] for j in range(col)]
    lines = list()
    start = (0, 0)
    end = (40, 40)
    cost = 1

    environment[1][2] = -1
    environment[1][17] = -1
    environment[6][2] = -1
    environment[6][17] = -1
    shape1 = ((1, 2), (1, 17), (6, 17), (6, 2))
    line3 = LineString([(1, 2), (1, 17)])
    line4 = LineString([(1, 2), (6, 3)])

    environment[12][2] = -1
    environment[12][20] = -1
    environment[17][2] = -1
    environment[17][20] = -1
    shape2 = ((12, 2), (12, 20), (17, 20), (17, 2))
    line5 = LineString([(18, 2), (18, 20)])
    line6 = LineString([(13, 2), (13, 20)])

    environment[20][25] = -1
    environment[20][38] = -1
    environment[32][37] = -1
    environment[32][29] = -1
    environment[35][26] = -1
    environment[27][18] = -1
    shape3 = ((20, 25), (20, 38), (32, 37), (32, 29), (35, 26), (27, 18))
    line8 = LineString([(20, 25), (27, 19)])
    line9 = LineString([(27, 19), (34, 26)])

    environment[14][35] = -1
    environment[6][23] = -1
    environment[19][23] = -1
    shape4 = ((14, 35), (6, 23), (19, 23))
    #line7 = LineString([(7, 26), (24, 22)])
    line7 = LineString([(7, 24), (19, 24)])

    environment[24][5] = -1
    environment[20][10] = -1
    environment[23][13] = -1
    environment[25][16] = -1
    environment[30][12] = -1
    shape5 = ((24, 5), (20, 10), (23, 13), (25, 16), (30, 12))


    #print(environment)
    path = search(environment, cost, start, end, lines)
    #print(path)

    #print('\n'.join([''.join(["{:" ">3d}".format(item) for item in col])
    #                 for col in environment]))

def draw(shape):
    z = 0
    while z < len(shape):
        if z == len(shape) - 1:
            pygame.draw.line(gameDisplay, blue, (shape[0][1] * 40, shape[0][0] * 40), (shape[z][1] * 40, shape[z][0] * 40), 5)
            z += 1
        else:
            pygame.draw.line(gameDisplay, blue, (shape[z][1] * 40, shape[z][0] * 40), (shape[z + 1][1] * 40, shape[z + 1][0] * 40), 5)
            z += 1

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((1600, 1600))
gameDisplay.fill(black)

#Drawing the shapes
draw(shape1)
draw(shape2)
draw(shape3)
draw(shape4)
draw(shape5)

size = len(path)
for i in range(size):
    if i < size -1:
        pygame.draw.line(gameDisplay, red, (path[i + 1][0] * 40, path[i + 1][1] * 40), (path[i][0] * 40, path[i][1] * 40), 5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
