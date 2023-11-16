from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    clone = set()

    while len(frontier) != 0:
        for i in frontier:
            result.update(graph[i])
            frontier.update(graph[i])
            clone.update(i)

            current = i
            break
        for x in clone:
            frontier.discard(x)
        
    return result





def connected(graph):
    x = len(graph)
    return x == len(reachable(graph, next(iter(graph))))
    




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    setcycles = set()
    for i in graph:
        reach = reachable(graph, next(iter(i)))
        
        setcycles.add(len(reach))
    print(setcycles)

    if len(graph) in setcycles:
        return 1
    else:
        return len(setcycles)
    ### TODO
    pass

