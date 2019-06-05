'''
Created on Mar 9, 2019

@author: 15136
'''
import math
import queue
def distanceFromDelivery(x, y):
    return math.sqrt(x**2 + y**2)

class DataPoint(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    # If you change this to self.key > other.key, PQ returns maximum number first 
    def __lt__(self, other):
        return (self.key < other.key)

def nearestPoints(points, k):
    pq = queue.PriorityQueue()
    for point in points:
        distance = distanceFromDelivery(point[0], point[1])
        pq.put(DataPoint(distance, [point[0], point[1]]))
        
    result = []
    count = 0
    while(count < k):
        val = pq.get()
        print(val.key)
        result.append(val.value)
        count += 1
    return result

points_array = [[6, 3], [2, 1], [5, 2], [3, 2], [9, 0], [0, 9]]
neighbors = nearestPoints(points_array, 3)
print(neighbors)

points_array = [[1, 2], [3, 4], [1, -1]]
neighbors = nearestPoints(points_array, 2)
print(neighbors)