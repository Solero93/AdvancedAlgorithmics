import networkx as nx

# Christian Jose Soler, ejercicio 2

## La eficiencia de esta algoritmo es O(n2) ya que seguimos una iteracion lineal sobre cada archivo y en cada una de ellas hacemos n operaciones para cubrirlo
## Para optimizarlo, se podria hacer el algoritmo desdel medio con dividir y vencer que tiene complejidad O(n log (n))

## La demostracion formal seria suponiendo que podria haber mejor complejidad que O(n log (n)), pero vemos que es imposible ya que solo recorrer la lista es O(n), y no hemos operado con ningun elemento aun.

#Clase que representa un archivo
class Archivo():
	def __init__(self, size, index):
		self.size = size # Su tamano que va a disminuir
		self.capacity = size # Su capacidad que es la inicial
		self.index = index # La posicion que ocupa en la lista
	def decrement(self, n):
		self.size -= n
	def getSize(self):
		return self.size
	def getCapacity(self):
		return self.capacity
	def getIndex(self):
		return self.index

#Clase que representa una cinta
class Cintes():
	def __init__(self, size):
		self.size = size # Su tamano que va a disminuir
		self.visited = [] # La lista de archivos cubiertos
	def visit(self, archivo):
		self.visited.append(archivo)
	def decrement(self, n):
		self.size -= n
	def getSize(self):
		return self.size
	def getVisited(self):
		return self.visited

# K es un numero natural y M es una lista de numeros naturales (representan capacidad de cinta y tamano de archivos)
def cintes(K,M):
	M = sorted(M)
	archivos = []  # Hacemos un vector de objetos Archivo
	index = 0 # Indice inicial
	
	for num in M: # Para cada valor en la lista de archivos
		tmp = Archivo(num,index) # Nos creamos el objeto Archivo
		archivos.append(tmp) # Lo anadimos a los archivos
		index += 1 # Aumentamos indice
	
	used_cintes = [] # Creamos vector de tipo Cintes
	count_visited = 0 # Iniciamos contador de archivos visitados

	while count_visited < len(archivos): # Mientras todos los archivos no hayan sido visitados
		current_cinta = Cintes(K) # Creamos una cinta inicial
		while current_cinta.getSize() > 0 and count_visited < len(archivos): # Mientras la cinta no se haya acabado y no hayamos visitado todos los archivos
			tmp_file = archivos[count_visited] # Cogemos un archivo
			tmp_file.decrement(current_cinta.getSize() - tmp_file.getSize()) # Decrementamos el tamano del archivo, asi cubriendolo
			current_cinta.visit(archivos[count_visited]) # Ponemos el archivo en la lista de cubiertos por la cinta
			current_cinta.decrement(tmp_file.getSize()) # Decrementamos la capacidad de la cinta
			count_visited += 1 # Aumentamos contador de visitados
		
		used_cintes.append(current_cinta) # Anadimos al objeto cinta, los archivos visitados
	
	
	print "En total hay " , len(used_cintes) , " placas" # Imprimimos resultados
	print "Mas detalladamente: "
	for elem in used_cintes:
		print "   Esta placa cubre: (indice y tamano)"
		for archivo in elem.getVisited():
			print archivo.getIndex(), archivo.getCapacity()

cintes(3,[1,2,5,4,6]) # Ejemplo de prueba 	
