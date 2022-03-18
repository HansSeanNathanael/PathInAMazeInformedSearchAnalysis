import heapq
import copy
import time
import tracemalloc

def currentTimeNanos():
    return time.time_ns()

class Coord:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        return 1
    
    def distance(self, coord):
        dx = self.x - coord.x
        dy = self.y - coord.y
        
        if (dx < 0):
            dx = -dx
        if (dy < 0):
            dy = -dy
            
        return dx + dy
    
    def setCoord(self, x, y):
        self.x = x
        self.y = y

def solusiGreedyBestFirstSearch(width, height, board, startCoord, endCoord):

    pqueue = []
    heapq.heappush(pqueue, (endCoord.distance(startCoord), startCoord, 0))
    
    while(len(pqueue) > 0):
        currentState = heapq.heappop(pqueue)
        currentCoord = currentState[1]
        
        if (board[currentCoord.y][currentCoord.x] == 'T'):
            return currentState[2]
            
        elif (board[currentCoord.y][currentCoord.x] != 'X'):
            board[currentCoord.y][currentCoord.x] = 'X'
            
            if (currentCoord.y > 0 and board[currentCoord.y - 1][currentCoord.x] != 'X' and board[currentCoord.y - 1][currentCoord.x] != '#'):
                nextCoord = Coord(currentCoord.x, currentCoord.y - 1)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord), nextCoord, currentState[2] + 1))
            if (currentCoord.y < height - 1 and board[currentCoord.y + 1][currentCoord.x] != 'X' and board[currentCoord.y + 1][currentCoord.x] != '#'):
                nextCoord = Coord(currentCoord.x, currentCoord.y + 1)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord), nextCoord, currentState[2] + 1))
            if (currentCoord.x > 0 and board[currentCoord.y][currentCoord.x - 1] != 'X' and board[currentCoord.y][currentCoord.x - 1] != '#'):
                nextCoord = Coord(currentCoord.x - 1, currentCoord.y)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord), nextCoord, currentState[2] + 1))
            if (currentCoord.x < width - 1 and board[currentCoord.y][currentCoord.x + 1] != 'X' and board[currentCoord.y][currentCoord.x + 1] != '#'):
                nextCoord = Coord(currentCoord.x + 1, currentCoord.y)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord), nextCoord, currentState[2] + 1))
                
    return "DOOMED"
    
def solusiAStar(width, height, board, startCoord, endCoord):

    pqueue = []
    heapq.heappush(pqueue, (endCoord.distance(startCoord), startCoord, 0))
    
    while(len(pqueue) > 0):
        currentState = heapq.heappop(pqueue)
        currentCoord = currentState[1]
        
        if (board[currentCoord.y][currentCoord.x] == 'T'):
            return currentState[2]
            
        elif (board[currentCoord.y][currentCoord.x] != 'X'):
            board[currentCoord.y][currentCoord.x] = 'X'
            
            if (currentCoord.y > 0 and board[currentCoord.y - 1][currentCoord.x] != 'X' and board[currentCoord.y - 1][currentCoord.x] != '#'):
                nextCoord = Coord(currentCoord.x, currentCoord.y - 1)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord) + currentState[2], nextCoord, currentState[2] + 1))
            if (currentCoord.y < height - 1 and board[currentCoord.y + 1][currentCoord.x] != 'X' and board[currentCoord.y + 1][currentCoord.x] != '#'):
                nextCoord = Coord(currentCoord.x, currentCoord.y + 1)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord) + currentState[2], nextCoord, currentState[2] + 1))
            if (currentCoord.x > 0 and board[currentCoord.y][currentCoord.x - 1] != 'X' and board[currentCoord.y][currentCoord.x - 1] != '#'):
                nextCoord = Coord(currentCoord.x - 1, currentCoord.y)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord) + currentState[2], nextCoord, currentState[2] + 1))
            if (currentCoord.x < width - 1 and board[currentCoord.y][currentCoord.x + 1] != 'X' and board[currentCoord.y][currentCoord.x + 1] != '#'):
                nextCoord = Coord(currentCoord.x + 1, currentCoord.y)
                heapq.heappush(pqueue, (endCoord.distance(nextCoord) + currentState[2], nextCoord, currentState[2] + 1))
                
    return "DOOMED"

if __name__ == "__main__":

    height = 7
    width = 11
    
    board = [
		['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
		['.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
		['.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.'],
		['S', '#', '.', '#', '.', '#', '.', '#', '.', '#', 'T'],
		['.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
		['.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
		['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
	]
    
    startCoord = Coord(0, 3)
    goalCoord = Coord(10, 3)

    tracemalloc.start()
    startTime = currentTimeNanos()
    print(solusiGreedyBestFirstSearch(width, height, copy.deepcopy(board), startCoord, goalCoord))
    endTime = currentTimeNanos()
    print("GBFS time elaps:", endTime - startTime, "ms")
    print("Memory usage:", tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    startTime = currentTimeNanos()
    print(solusiAStar(width, height, copy.deepcopy(board), startCoord, goalCoord))
    endTime = currentTimeNanos()
    print("AStar time elaps:", endTime - startTime, "ms")
    print("Memory usage:", tracemalloc.get_traced_memory())
    tracemalloc.stop()