def assoc(node, net):
    val = [x for x in net if x[0] == node]
    return [] if val == [] else val[0]

def shortest_path(start, end, net):
    return bfs(end, [[start]], net)

def bfs(end, queue, net):
    print "Queue: %s" % queue
    if not len(queue):
        return None
    else:
        path = queue[0]
        node = path[0]
        if node == end:
            return path[::-1]
        else:
            return bfs(end, queue[1:] + new_paths(path, node, net) ,net)

def new_paths(path, node, net):
    return [[child] +  path for child in assoc(node, net)[1:]]

def longest_path(start, end, net):
    return dfs(end, [start], [], net)[::-1]

def dfs(end, current_path, best_path, net):
    if current_path[0] in current_path[1:]:
        #print "Cycle: %s, Best: %s" % (str(current_path), str(best_path))
        if current_path[0] == end and end == current_path[-1]:
            # update best path
            best_path = current_path if len(current_path) > len(best_path) else best_path
        return best_path

    for child in assoc(current_path[0], net)[1:]:
        result = dfs(end, [child] + current_path, best_path, net)
        # update best path
        best_path = result if len(result) > len(best_path) else best_path

    if current_path[0] == end:
        # update best path
        best_path = current_path if len(current_path) > len(best_path) else best_path
        return best_path

    return best_path

# net = [['A', 'B', 'C'], ['B', 'C'], ['C', 'D']]
# print shortest_path('A', 'D', net)

networks = []
networks.append([['A', 'B'], ['B', 'C']])
networks.append([['A', 'B'], ['B', 'A', 'C']])
networks.append([['A', 'D', 'E', 'F', 'G', 'B'], ['B', 'A', 'C']])
networks.append([['A', 'B'], ['B', 'A', 'C']])
networks.append([['A', 'B'], ['B', 'A'], ['C']])
networks.append([['A', 'B', 'C'], ['B', 'F'], ['C', 'D'], ['D', 'E'], ['E', 'F']])
networks.append([['A', 'B', 'C', 'A'], ['B', 'C', 'D'], ['C', 'E', 'A'], ['D', 'E', 'F'], ['E', 'D', 'F']])
networks.append([['A', 'B', 'C', 'A'], ['B', 'C', 'D'], ['C', 'E', 'A'], ['D', 'E', 'F'], ['E', 'D', 'F']])
networks.append([['A', 'B'], ['B', 'C']])
networks.append([['A', 'A', 'B'], ['B', 'C']])
networks.append([['A', 'B', 'A'], ['B', 'C']])
networks.append([['A','B'], ['B', 'C'], ['C', 'B']])
networks.append([['A', 'B', 'C'], ['B', 'C'], ['C', 'B']])

print longest_path('A', 'C', networks[0])
print longest_path('A', 'C', networks[1])
print longest_path('A', 'C', networks[2])
print longest_path('A', 'A', networks[3])
print longest_path('A', 'C', networks[4])
print longest_path('A', 'F', networks[5])
print longest_path('A', 'F', networks[6])
print longest_path('A', 'A', networks[7])
print longest_path('A', 'A', networks[8])
print longest_path('A', 'A', networks[9])
print longest_path('A', 'A', networks[10])
print longest_path('A', 'B', networks[11])
print longest_path('A', 'B', networks[12])