import generate
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
            printGraph(bottomLeft)
            return cameFrom

        closedSet.append(current)
        for neighbor in getNeighbors(current):
            if neighbor in closedSet:
                continue
            tempGScore = gscore[current] + 1

            if not inQueue(neighbor, queue) or tempGScore < gscore[neighbor]:
                #print current.x, current.y
                #import ipdb; ipdb.set_trace()
                #os.system('clear')
                #printGraph(bottomLeft)
                current.value = 'V'
                cameFrom[neighbor] = current
                gscore[neighbor] = tempGScore
                fscore[neighbor] = gscore[neighbor] + getHeuristic(neighbor, destination)
                if neighbor not in queue:
                    heapq.heappush(queue, (fscore[neighbor], neighbor))

def main(worldNumber):
    world = pickle.load(open('./worlds/world%d.pkl' % worldNumber, 'rb'))

    aStarSearch(world.start, world.end, world.bottomLeft)
    print 'hello world'

if __name__ == '__main__':
    for i in range(50):
        if i == 10:
            continue
        main(i)
