"""
Author: Ashley Harris
This algorithm finds the shortest distance between two airports, using
intermediate airports, given that the plane can fly a maximum of 200km
before needing to refuel.
"""
import sys, math, heapq
from heapq import heappop, heappush

def dijkstra(adj_dict, source, destination):
    heap = [(0, source)]
    dist_dict = {}
    for key in adj_dict:
        dist_dict[key] = None
    while heap:
        path_len, coord = heappop(heap)
        if dist_dict[coord] is None: # coord is unvisited
            dist_dict[coord] = path_len
            for adj_coord, edge_len in adj_dict[coord].items():
                if dist_dict[adj_coord] is None:
                    heappush(heap, (path_len + edge_len, adj_coord))
    return dist_dict[destination]

def calc_dist(coord1, coord2):
    xdist = float(coord1[0:coord1.index(",")]) - float(coord2[0:coord2.index(",")])
    ydist = float(coord1[coord1.index(",")+1:len(coord1)]) \
            - float(coord2[coord2.index(",")+1:len(coord2)])
    dist = math.sqrt(xdist * xdist + ydist * ydist)
    return dist

for line in sys.stdin:
    data = (line.strip()).split(",")
    n = data[0]
    coord_list = []
    coord_num = len(data[1:]) // 2
    k = 1
    for i in range(coord_num):
        coord_tup = (data[k], data[k+1])
        coord_list.append(",".join(coord_tup))
        k += 2
    source = coord_list[0]
    destination = coord_list[-1]
    adj_dict = {}
    for coord in coord_list:
        adj_dict[coord] = {}
    for i in range(coord_num):
        out = coord_list.pop()
        for coord in coord_list:
            dist = calc_dist(out, coord)
            if dist <= 200:
                adj_dict[out][coord] = dist
                adj_dict[coord][out] = dist
    min_path = dijkstra(adj_dict, source, destination)
    if min_path is None:
        print(-1)
    else:
        print("{:.2f}".format(min_path))