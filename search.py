from helpers import World, Node
import cPickle as pickle
import heapq
import os

class Search:
    def test():
        print 'passed'

def getHeuristic(start, finish):
    return abs(start.x - finish.x) + abs(start.y - finish.y)

def printGraph(bottomLeft):
    while bottomLeft.up != None:
        bottomLeft = bottomLeft.up

    topLeft = bottomLeft
    leftIter = topLeft
    while topLeft != None:
        while leftIter != None:
            print leftIter.value,
            leftIter = leftIter.right
        print ''
        leftIter = topLeft.down
        topLeft = topLeft.down

def inQueue(node, queue):
    for item in queue:
        if item[1] == node:
            return True
    return False

def getNeighbors(node):
    array = []
    if node.left and node.left.value != 'B':
        array.append(node.left)
    if node.right and node.right.value != 'B':
        array.append(node.right)
    if node.up and node.up.value != 'B':
        array.append(node.up)
    if node.down and node.down.value != 'B':
        array.append(node.down)
    return array


def dumbGetNeighbors(node):
    array = []
    if node.left and not node.left.knownBlocked:
        array.append(node.left)
    if node.right and not node.right.knownBlocked:
        array.append(node.right)
    if node.up and not node.up.knownBlocked:
        array.append(node.up)
    if node.down and not node.down.knownBlocked:
        array.append(node.down)
    return array


def computePath(origin, destination, bottomLeft):
    closedSet = []
    queue = []
    heapq.heapify(queue)
    cameFrom = {}
    gscore = {}
    fscore = {}
    gscore[origin] = 0
    fscore[origin] = gscore[origin] + getHeuristic(origin, destination)
    heapq.heappush(queue, (fscore[origin], origin))

    while(len(queue) > 0):
        current = heapq.heappop(queue)[1]
        if current == destination:
            return cameFrom

        closedSet.append(current)
        for neighbor in dumbGetNeighbors(current):
            if neighbor in closedSet:
                continue
            tempGScore = gscore[current] + 1

            if not inQueue(neighbor, queue) or tempGScore < gscore[neighbor]:
                #print current.x, current.y
                #import ipdb; ipdb.set_trace()

                #printGraph(bottomLeft)
                #os.system('clear')
                cameFrom[neighbor] = current
                gscore[neighbor] = tempGScore
                fscore[neighbor] = getHeuristic(neighbor, destination)
                if neighbor not in queue:
                    heapq.heappush(queue, (fscore[neighbor], neighbor))


def getPath(tree, end):
    path = []
    temp = end
    while temp in tree.keys():
        path.append(temp)
        temp = tree[temp]
    return [item for item in reversed(path)]

def discoverNeighboarBlocks(node):
    if node.up and node.up.value == 'B':
        node.up.knownBlocked = True
    if node.down and node.down.value == 'B':
        node.down.knownBlocked = True
    if node.left and node.left.value == 'B':
        node.left.knownBlocked = True
    if node.right and node.right.value == 'B':
        node.right.knownBlocked = True

def walkPath(path):
    count = 0
    for step in path:
        #discoverNeighboarBlocks(step)
        if step.value == 'B':
            step.knownBlocked = True
            return count
        else:
            step.value = 'V'
        count += 1
    return count

def repeatedReverseAStar(origin, destination, bottomLeft):
    tempNode = destination
    finalPath = []
    path = computePath(tempNode, destination, bottomLeft)
    pathArr = getPath(path, destination)
    pathArr = [node for node in reversed(pathArr)]

    while tempNode != origin:
        #os.system('clear')
        #printGraph(bottomLeft)
        path = computePath(tempNode, origin, bottomLeft)
        pathArr = getPath(path, destination)

        index = walkPath(pathArr)
        finalPath += pathArr[:index]
        if index == len(pathArr) - 1:
            return finalPath
        # Temp node becomes the place where we stopped along the walkPath method
        tempNode = finalPath[len(finalPath) - 1]
    return finalPath



def repeatedForwardAStar(origin, destination, bottomLeft):
    tempNode = origin
    finalPath = []
    while tempNode != destination:
        #os.system('clear')
        #printGraph(bottomLeft)
        path = computePath(tempNode, destination, bottomLeft)
        pathArr = getPath(path, destination)

        index = walkPath(pathArr)
        finalPath += pathArr[:index]
        if index == len(pathArr) - 1:
            return finalPath
        # Temp node becomes the place where we stopped along the walkPath method
        if len(finalPath) >= 1:
            tempNode = finalPath[len(finalPath) - 1]
        os.system('clear')
        printGraph(bottomLeft)

    return finalPath



def aStarSearch(origin, destination, bottomLeft):
    closedSet = []
    queue = []
    heapq.heapify(queue)
    cameFrom = {}
    gscore = {}
    fscore = {}
    gscore[origin] = 0
    fscore[origin] = gscore[origin] + getHeuristic(origin, destination)
    heapq.heappush(queue, (fscore[origin], origin))

    while(len(queue) > 0):
        current = heapq.heappop(queue)[1]
        if current == destination:
            return cameFrom

        closedSet.append(current)
        for neighbor in getNeighbors(current):
            if neighbor in closedSet:
                continue
            tempGScore = gscore[current] + 1

            if not inQueue(neighbor, queue) or tempGScore < gscore[neighbor]:
                #print current.x, current.y
                #import ipdb; ipdb.set_trace()
                current.value = 'V'
                cameFrom[neighbor] = current
                gscore[neighbor] = tempGScore
                fscore[neighbor] = gscore[neighbor] + getHeuristic(neighbor, destination)
                if neighbor not in queue:
                    heapq.heappush(queue, (fscore[neighbor], neighbor))

def main(worldNumber):
    world = pickle.load(open('./worlds/world%d.pkl' % worldNumber, 'rb'))

    path = repeatedForwardAStar(world.start, world.end, world.bottomLeft)
    os.system('clear')
    printGraph(world.bottomLeft)
    print 'hello world'

if __name__ == '__main__':
    for i in range(50):
        if i == 37:
            continue
        main(i)

