from heapq import heappush, heappop
import json
import math

loc = open("locations.json")
location_data = json.load(loc)
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
    def get_adjacent_stations(node):

        successors = location_data[node]
        names = []
        for i in successors:
            names.append(i[0])
        return names
    return get_adjacent_stations

#Calculates the distance from our current station to our goal station
#Current = string code for current station
#Goal = string code for goal station
#Note, since the units of latitude are in degrees we convert to miles by multiplying
# by 69
def get_distance_to_goal(current, goal):
    x1 = location_data[current]['latitude']
    x2 = location_data[goal]['latitude']
    y1 = location_data[current]['longitude']
    y2 = location_data[goal]['longitude']
    horizontal = (x2-x1)**2
    vertical = (y2-y1)**2
    distance = math.sqrt(horizontal + vertical)* 69
    return distance


#this needs to be changed to take in a parameter of different kinds of heuristics
def get_heuristic(current, goal):

    #Case 1 euclidian distance heuristic
    return get_distance_to_goal(current, goal)
    #Case 2 manhattan distance heuristic
    #Case 3 Least future stops heuristic
    #return NotImplementedError