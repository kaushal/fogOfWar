import random
import cPickle
import sys

class Node:
    left = None
    right = None
    up = None
    down = None
    value = '-'

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
    return bottomLeft

sys.setrecursionlimit(100000)

for i in range(50):
    a = generateMap()

    output = open('../worlds/data%d.pkl' % i, 'wb')

    cPickle.dump(a, output)

    output.close()



import ipdb; ipdb.set_trace()
bottomLeft = a
while bottomLeft != None:
    a = bottomLeft
    while a != None:
        print a.value,
        a = a.right
    print ''

    bottomLeft = bottomLeft.up
