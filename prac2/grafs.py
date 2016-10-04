import graphs_mod as gr # Es un archivo que implementa metodos de grafos

## Christian Jose Soler, Algoritmica avanzada
## Practica 1 : Ejercicio 1, Ciclio euleriano

## Analisis de complejidad:
    ## Tenemos el algoritmo de complejidad O(n2), ya que hacemos un bucle para cada vecino del nodo actual que se llama, como maximo, tantas veces como nodos haya en el grafo. 

# La funcion main que hace la tarea principal del programa
def main():				
	g = gr.import_graph("graf1.dat") # Creamos el grafo a partir del archivo	
	lista = [1] # Inicializamos la lista del ciclo
	
	lista = explora_cicle_complet(g, lista[0], lista) # Ejecutamos el modulo que encuentra el ciclo

        # Imprimimos los resultados a pantalla
	if lista:
		print "El cicle euleria es: ", lista
	else:
		print "Cal repassar arestes"

# Modulo que se encarga de buscar el ciclo euleriano, de forma recursiva
def explora_cicle_complet(g, node, lista):
        # Para cada vecino del nodo actual
	for neighbour in g.neighbors(node):
                # Si no es de la lista, lo exploramos
		if neighbour not in lista:
			tmp = explora_cicle_complet (g, neighbour, (lista + [neighbour]))
			if tmp:
				return tmp
                # Si es de la lista, miramos si recubrimos todo el grafo
		else:
			if len(lista) == len(g) and neighbour == 1:
				return lista + [1]
	return
main()
