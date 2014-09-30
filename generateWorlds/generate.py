class Node:
    left = None
    right = None
    up = None
    down = None
    value = '-'

def generateMap():
    bottomLeft = Node()
    currentNode = bottomLeft

    # generate a base layer
    for i in range(100):
        currentNode.right = Node()
        currentNode.right.left = currentNode
        currentNode = currentNode.right

    bottomLeft.up = Node()
    bottomLeft.up.down = bottomLeft

    currentNodeNewRow = bottomLeft.up
    currentNodePrevRow = currentNodeNewRow.down

    newBottomLeft = currentNodeNewRow

    for i in range(100):
        while currentNodePrevRow != None:
            current = Node()
            currentNodeNewRow.right = current
            currentNodeNewRow.right.left = currentNodeNewRow

            current.down = currentNodePrevRow
            current.down.up = current


            currentNodeNewRow = currentNodeNewRow.right
            currentNodePrevRow = currentNodePrevRow.right

        newBottomLeft.up = Node()

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

