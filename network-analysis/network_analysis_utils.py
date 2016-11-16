from collections import deque
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import math

def facebook_nx_graph():
    return nx.read_pajek('facebook_graph.net')

def random_nx_grap():
    return nx.read_pajek('random_graph.net')

def write_btwns_graph(nx_graph, weight_dict, output_filename):
    
    """ Plot a networkx undirected graph in a file.
        - nx_graph(Graph)         - the graph from networkx library
        - weight_dict(dictionary) - the weight dictionary in the form of { node: betweenness centrality value }
        - output_filename         - the filename of target file"""
    
    # normalizing nodes_weight
    max_weight = float( max( weight_dict.values() ) )
    norm_weights = { n: weight_dict[n] / max_weight for n in nx_graph.nodes() }
    
    # preparing to draw
    weights = [ math.pow(1.0 + norm_weights[n], 6) * 300 for n in nx_graph.nodes() ]
    norm_weights = { n: "%.3f" % norm_weights[n] for n in nx_graph.nodes() }
    
    # drawing
    plt.figure(figsize=(50, 50))
    nx.draw_networkx(nx_graph, node_size=weights, labels= norm_weights, node_color='b', width=0.5)
    plt.savefig(output_filename)
    plt.clf()
    plt.close()

def shortest_paths(nodes, edges):
    """ Returns the shortest paths from all nodes to all nodes. 
        The input are a graph composed by nodes (verticies) and edges. 
        The output are a dictionary as follow:
            {
                node_i: {
                    node_j: [ [path_to_j], [path_to_j], ... ],
                    node_k: [ [path_to_k], [path_to_k], ... ],
                    ...
                },
                ...
            }
        Each node have the correspondent entry on output dictionary.
        *path_to_x* are the sequence of nodes from node_i to node_x.
        """
    
    shortest_paths_dict = {}
    graph_connections = {}

    for node in nodes:
        graph_connections[node] = []

    for node_a, node_b in edges:
        graph_connections[node_a].append(node_b)
        graph_connections[node_b].append(node_a)

    for node in nodes:
        
        shortest_paths_to = { node : [[]] }

        frontier = deque( (node, node_rel) for node_rel in graph_connections[node] )

        while frontier:
            
            prev_node, next_node = frontier.popleft()

            paths_to_prev_node = shortest_paths_to[ prev_node ]
            new_paths_to_next_node = [ path + [ next_node ] for path in paths_to_prev_node ]

            old_paths_to_node = shortest_paths_to.get( next_node, [] )

            if old_paths_to_node:
                min_path_length = len(old_paths_to_node[0])
            else:
                min_path_length = float('inf')

            new_paths_to_next_node = [  path
                                        for path in new_paths_to_next_node
                                        if len(path) <= min_path_length
                                        and path not in old_paths_to_node   ]

            shortest_paths_to[next_node] = old_paths_to_node + new_paths_to_next_node

            frontier.extend((next_node, node_rel)
                            for node_rel in graph_connections[next_node]
                            if node_rel not in shortest_paths_to)

        shortest_paths_dict[node] = shortest_paths_to

    return shortest_paths_dict