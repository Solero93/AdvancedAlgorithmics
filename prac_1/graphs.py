import networkx as nx
import matplotlib.pyplot as plt
import random as rd

def show(G):
	nx.draw(G)
	plt.show()

def random_graph():
	return nx.gnp_random_graph(rd.randint(1,100), rd.random(), None, rd.choice([True,False]))

def import_graph(filename):
	return nx.read_adjlist(filename, nodetype=int)

def explora(node, lista):
	pass
