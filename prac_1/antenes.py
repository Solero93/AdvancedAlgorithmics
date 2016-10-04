import graphs as gr

def main():
	g = gr.import_graph("graph.txt")
	g1 = gr.random_graph()
	s = antenes(g1)
	print(s)
	gr.show(g1)

def antenes(g):	
	max_node = find_max(g)  			# Begin the search from the node with most neighbors (of there are more, the first of them)
	solution = [max_node]    			# The node with most neighbors, by definition, belongs to our solution
	not_visited_nodes = g.nodes()
	
	g.node[max_node]["visited"] = True
	not_visited_nodes = erase_node(max_node, not_visited_nodes)	
	for node in g.neighbors_iter(max_node):				# Set all its neighbours visited and erase from the not_visited list
		g.node[node]["visited"] = True
		not_visited_nodes = erase_node(node, not_visited_nodes) 
			
	while not_visited_nodes != [] :
		tmp_max = -1	
	
		for node in iter(not_visited_nodes):
			tmp_max2 = len(filter(lambda x: g.node[x]["visited"] == False, g.neighbors_iter(node)))
			if tmp_max2 > tmp_max:
				max_node = node
				tmp_max = tmp_max2
		
		solution.append(max_node)
		g.node[max_node]["visited"] = True
		not_visited_nodes = erase_node(max_node, not_visited_nodes)
	
		for node in g.neighbors_iter(max_node):
			g.node[node]["visited"] = True
			not_visited_nodes = erase_node(node, not_visited_nodes)
	return solution

# Search node with most neighbors
def find_max(g):
	tmp_max = -1 # Initial value to find the maximum

	for node in g.nodes_iter():
		g.node[node]["visited"] = False
		tmp_neigh_len = len(g.neighbors(node))
		if tmp_neigh_len > tmp_max:
			tmp_max = tmp_neigh_len
			max_node = node
	return max_node

def erase_node(node, lista):
	try:
		tmp = lista.index(node)
	except:
		return lista	

	lista[tmp], lista[-1] = lista[-1], lista[tmp]
	lista.pop()
	return lista	


# Search neighbor of node with most neighbors
def find_max_neigh(g,node):
	tmp_max = -1	
	for node in g.neighbor_iter(node):
		tmp_neigh = g.neighbors(node)
		if len(tmp_neigh) > tmp_max:
			tmp_max = len(tmp_neigh)
			max_node = node
	return max_node

# Check if all neighbours of a node had been visited already
def visited_node_neigh(g,node):
	for node in g.neighbors_iter(node):
		if g.node[node]["visited"] == False:
			return False
	return True

# Check if the whole graph had been visited
def visited_graph(g):
	for node in g.nodes_iter():
		if g.node[node]["visited"] == False:
			return False
	return True

main()	
