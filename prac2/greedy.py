import graphs_mod as gr # Es un archivo que implemento metodos de grafos

## Christian Jose Soler, Algoritmica Avanzada
## Practica 1 : Ejercicio 2, Problema de las antenas

## Analisis de complejidad:
    ## La busqueda del nodo con mas vecinos: O(n) (Se hace una vez)
    ## La busqueda del nodo aun no visitado con vecinos aun no visitados O(n2)
        ## O(n), porque como maximo hay un numero de nodos del orden de n
        ## O(n), porque para cada nodo, recorremos sus vecinos y los contamos, que es del orden maximo de n
            ## Multiplicados dan el O(n2)
    ## Se que se pide O(n), pero solo recorrer el grafo, ya es O(n) y aun no he mirado ni vecinos, pues no vi manera de conseguirlo

def main():
	g = gr.import_graph("graf1.dat") # Creamos el grafo a partir del archivo 
	solution = antenes(g) # Buscamos la lista minima y devolvemos el resultado
        print "The best solution is: ", solution

# Modulo que busca la posible mejor solucion para el problema, usando un algoritmo greedy
def antenes(g):	
	max_node = find_max(g) # Empezamos por el nodo con mas vecinos 
	solution = [max_node] # Le anadimos a nuestra solucion
	not_visited_nodes = g.nodes() # Creamos la lista con los nodos aun no visitados
	
	g.node[max_node]["visited"] = True # Hacemos que el nodo inicial se visite y lo borramos de la lista
	not_visited_nodes.remove(max_node)
        for node in g.neighbors_iter(max_node):	# Hacemos lo mismo con sus vecinos
		g.node[node]["visited"] = True
                try:
		    not_visited_nodes.remove(node)
                except:
                    pass
	
        # Mientras no se visiten todos los nodos
	while not_visited_nodes :
		tmp_max = -1

                # De los nodos aun no visitados 
                # Buscamos al nodo con el mayor numero de vecinos aun no visitados
	
		for node in iter(not_visited_nodes):
			tmp_max2 = len(filter(lambda x: g.node[x]["visited"] == False, g.neighbors_iter(node)))
			if tmp_max2 > tmp_max:
				max_node = node
				tmp_max = tmp_max2
	
                # Si lo encontramos, formara parte de nuestra solucion
                # Sus vecinos se ponen como visitados

		solution.append(max_node)
		g.node[max_node]["visited"] = True
		not_visited_nodes.remove(max_node)
	
		for node in g.neighbors_iter(max_node):
			g.node[node]["visited"] = True
                        try:
                            not_visited_nodes.remove(node)
                        except:
                            pass
	return solution

# Modulo que busca el nodo con mas vecinos e inicializa el atributo "visited" a falso
def find_max(g):
	tmp_max = -1
	for node in g.nodes_iter():
		g.node[node]["visited"] = False
		tmp_neigh_len = len(g.neighbors(node))
		if tmp_neigh_len > tmp_max:
			tmp_max = tmp_neigh_len
			max_node = node
	return max_node
main()
