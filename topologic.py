import networkx as nx

# Christian Jose Soler, ejercicio 1

# D es un String que representa la direccion y nombre del archivo donde se ubica el grafo

## Analisis: Encontrar el root del arbol, ya de por si es O(n2) al tener bucles dentro de bucles i busqueda de elementos en una lista
## La parte del algoritmo topologico en si, tiene complejidad O(n2) tambien, ya que aunque el peor caso es el de los 3 bucles uno dentro del otro, se compensan entre si.

def topologic(D):
	g = nx.read_adjlist(D,create_using=nx.DiGraph(),nodetype=int)
	root = find_root(g)			
	ordre = topo(g,root)
	print ordre

# La raiz es uno de aquellos nodos que no son vecinos de nadie, la buscamos
def find_root(g):
	tmp = g.nodes()
	for i in g.nodes():
		for j in g.neighbors(i):
			try:
				index = tmp.index(j)
				tmp[index] = -1
			except:
				pass
	for elem in tmp:
		if elem != -1:
			return elem	
# El algoritmo propio mente dicho que encuentra la ordenacion topologica
def topo(g,root):
	nodes = g.nodes() # Definimos la lista de nodos a analizar
	solution = [root] # Sabemos que la raiz serásolucion nuestra
	nodes.remove(root) # Lo quitamos de la lista a analizar
	len_g = len(g)	# Nos guardamos la longitud del grafo

	while len(solution) < len_g:
		tmp = []
		for node in nodes: # El siguiente en la lista sera un nodo que no sea vecino de los que quedan
			for elem in g.neighbors(node):
				if elem not in tmp:
					tmp.append(elem)
		for node in nodes: # Si no estáen la lista de todos los vecinos, lo anadimos a la solucion y lo quitamos de la lista para analizar
			if node not in tmp:
				solution.append(node)
				nodes.remove(node)
	return solution
			
				

topologic("dades.dat")
