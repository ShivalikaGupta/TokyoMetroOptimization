import json
import math
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

loc = open("output.json")
location_data = json.load(loc)
succ = open("connections.json")

location_data2 = json.load(succ)

def get_distance_to_goal(current, goal):
    #print("current: " + current + ",  goal:" + goal)
    x1 = location_data[current]['latitude']
    x2 = location_data[goal]['latitude']
    y1 = location_data[current]['longitude']
    y2 = location_data[goal]['longitude']
    horizontal = (x2-x1)**2
    vertical = (y2-y1)**2
    distance = math.sqrt(horizontal + vertical)* 110.574
    return distance


def get_successor(node):
  successors = location_data2[node]
  names = []
  for i in successors:
    names.append(i[0])
  return names

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


def generate_path(start, goal, successor_f, heuristic):
  visited = set()
  history = dict()
  distance = {start: 0}
  frontier = PriorityQueue()
  frontier.add(start)
  while frontier:
      node = frontier.pop()
      if node in visited:
          continue
      if goal == node:#change this to be if the node == goal station
          return reconstruct_path(history, start, node)
      visited.add(node)
      for successor in successor_f(node):
          frontier.add(
              successor,
              priority = distance[node] + 1 + heuristic(node, successor) # we may have to change this as this determines which stop we take next at each step
          )
          if (successor not in distance
              or distance[node] + 1 < distance[successor]):
              distance[successor] = distance[node] + 1
              history[successor] = node
  return None

path = generate_path("A01", "C01", get_successor, get_distance_to_goal)
print(len(path))
print(path)