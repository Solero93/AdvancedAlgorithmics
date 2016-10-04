import networkx as nx
import matplotlib.pyplot as plt
import random as rd

# Metodo para dibujar un grafo en linux
def show(G):
	nx.draw(G)
	plt.show()

# Metodo para generar un grafo aleatorio para las pruebas
def random_graph():
	return nx.gnp_random_graph(rd.randint(1,100), rd.random(), None, rd.choice([True,False]))

# Metodo para importar un grafo de un archivo
def import_graph(filename):
	return nx.read_adjlist(filename, nodetype=int)
