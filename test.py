import networkx as nx
from matplotlib import pyplot as plt
import math

G = nx.Graph()

row = '643715.202,2499149.0506 643752.61523545,2499089.86084203 ' +\
    '643773.6038,2499056.6558 643773.73878609,2499056.44011079 ' +\
    '643793.20162482,2499025.34111554 643813.55943268,2498992.81212045 ' +\
    '643826.6563,2498971.8852'

a=row.split(" ")
# Saving the previous node to be able to calculate the distance
prev_point = None
# Save the positions in a dictionary to be able to draw 
# the nodes at the correct positions
pos = {}
for i in a:
    cur_point = tuple([float(x) for x in i.split(',')])
    assert len(cur_point) == 2
    if prev_point is not None:
        # Calculate the distance between the nodes with the Pythagorean
        # theorem
        b = cur_point[1] - prev_point[1]
        c = cur_point[0] - prev_point[0]
        a = math.sqrt(b ** 2 + c ** 2)
        G.add_edge(cur_point, prev_point, weight=a)
    G.add_node(cur_point)
    pos[cur_point] = cur_point
    prev_point = cur_point
nx.draw(G, pos=pos)
