class World:
    def __init__(self, bottomLeft, start, end):
        self.bottomLeft = bottomLeft
        self.start = start
        self.end = end

class Node:
    left = None
    right = None
    up = None
    down = None
    value = '-'
    knownBlocked = False

    def __init__(self, x, y):
        self.x = x
        self.y = y


