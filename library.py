from heapq import heappush, heappop

class PriorityQueue:
    
    def __init__(self, iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap, (0, value))
    
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
    
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)

def reconstruct_path(came_from, start, end):
    """
    >>> came_from = {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'd'}
    >>> reconstruct_path(came_from, 'a', 'e')
    ['a', 'c', 'd', 'e']
    """
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))

#this needs to be changed to access a dictionary that returns the neighboring stations
def get_successor_function(stations):
    """
    return a list of the adjacent stations to cell in the total set of stations
    """
    def get_adjacent_stations(cell):
        #return adjacent stations
        return NotImplementedError
    return get_adjacent_stations

#this needs to be changed to take in a parameter of different kinds of heuristics
def get_heuristic(grid):

    #Case 1 euclidian distance heuristic
    #Case 2 manhattan distance heuristic
    #Case 3 Least future stops heuristic
    return NotImplementedError