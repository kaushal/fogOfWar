import random
import cPickle
import sys

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

def generateMap():
    bottomLeft = Node(0, 0)
    currentNode = bottomLeft

    # generate a base layer
    for i in range(100):
        currentNode.right = Node(i + 1, 0)
        randVal = random.randint(0, 10)
        if randVal < 3:
            currentNode.right.value = 'B'
        currentNode.right.left = currentNode
        currentNode = currentNode.right

    bottomLeft.up = Node(0, 1)
    bottomLeft.up.down = bottomLeft

    currentNodeNewRow = bottomLeft.up
    currentNodePrevRow = currentNodeNewRow.down

    newBottomLeft = currentNodeNewRow

    for i in range(100):
        count = 1
        while currentNodePrevRow.right != None:
            current = Node(count, i + 2)
            randVal = random.randint(0, 10)
            if randVal < 3:
                current.value = 'B'
            currentNodeNewRow.right = current
            currentNodeNewRow.right.left = currentNodeNewRow

            current.down = currentNodePrevRow.right
            current.down.up = current


            currentNodeNewRow = currentNodeNewRow.right
            currentNodePrevRow = currentNodePrevRow.right
            count += 1
        new = Node(0, i + 2)
        newBottomLeft.up = new

        newBottomLeft.up.down = currentNodeNewRow

        currentNodeNewRow = newBottomLeft.up
        currentNodePrevRow = newBottomLeft
        currentNodeNewRow.down = currentNodePrevRow
        newBottomLeft = newBottomLeft.up

    randX = random.randint(0, 100)
    randY = random.randint(0, 100)

    nodestart = bottomLeft

    for i in range(randX):
        nodestart = nodestart.right

    for i in range(randY):
        nodestart = nodestart.up

    nodestart.value = 'S'

    randX = random.randint(0, 100)
    randY = random.randint(0, 100)

    nodeend = bottomLeft

    for i in range(randX):
        nodeend = nodeend.right

    for i in range(randY):
        nodeend = nodeend.up


    nodeend.value = 'E'

    return World(bottomLeft, nodestart, nodeend)
'''
sys.setrecursionlimit(100000)

for i in range(50):
    a = generateMap()

    output = open('../worlds/world%d.pkl' % i, 'wb')

    cPickle.dump(a, output)

    output.close()


import ipdb; ipdb.set_trace()
bottomLeft = a.bottomLeft
while bottomLeft != None:
    a = bottomLeft
    while a != None:
        print a.value,
        a = a.right
    print ''

    bottomLeft = bottomLeft.up
    '''
