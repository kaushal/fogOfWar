import random

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
        currentNode.right = Node(i + 1, 1)
        currentNode.right.left = currentNode
        currentNode = currentNode.right

    bottomLeft.up = Node(1, 1)
    bottomLeft.up.down = bottomLeft

    currentNodeNewRow = bottomLeft.up
    currentNodePrevRow = currentNodeNewRow.down

    newBottomLeft = currentNodeNewRow

    for i in range(100):
        count = 0
        while currentNodePrevRow != None:
            current = Node(count, i + 1)
            randVal = random.randint(0, 10)
            if randVal < 3:
                current.value = 'B'
            currentNodeNewRow.right = current
            currentNodeNewRow.right.left = currentNodeNewRow

            current.down = currentNodePrevRow
            current.down.up = current


            currentNodeNewRow = currentNodeNewRow.right
            currentNodePrevRow = currentNodePrevRow.right
            count += 1

        newBottomLeft.up = Node(0, i + 2)

        currentNodeNewRow = newBottomLeft.up
        currentNodePrevRow = newBottomLeft

        newBottomLeft = newBottomLeft.up
    return bottomLeft

a = generateMap()
bottomLeft = a
count = 1
while bottomLeft != None:
    a = bottomLeft
    count += 1
    while a != None:
        print a.value,
        a = a.right
    print ''
    bottomLeft = bottomLeft.up
import ipdb; ipdb.set_trace()

