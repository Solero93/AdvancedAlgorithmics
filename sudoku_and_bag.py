def main(doc1, doc2):
  print "THE RUCKSACK PROBLEM: "
  mochila(doc1)
  print "\nTHE SUDOKU SOLVER"
  sudoku_solver(doc2)

##Christian Jose Soler: El problema de la mochila
## Analisis de eficiencia: Este algoritmo es de complejidad O(n^2) ya que para cada posibilidad que se puede meter en la mochila (que son n) se comprueba n veces lo que pasaria si esa opcion se metiese en la mochila = O(n*n) = O(n^2). La cantidad de memoria usada incrementa por el hecho de tener que reseguir el camino de meter elementos en la matriz, si no, con un vector de tamano n, bastaria.

# Class that represents an item to be put in the rucksack
class Item():
	def __init__(self, index=0, weight=0, value=0):
		self.index = index # Its ID in the given list
		self.weight = weight # Its weight
		self.value = value # Its value
		self.used = 0 # How many times it was used (initially 0)
		self.printed = False # Auxiliar attribute for the final return of the results

	def use(self):
		self.used += 1

	def getWeight(self):
		return self.weight

	def getValue(self):
		return self.value

	def getIndex(self):
		return self.index

	def printItem(self):
		if self.used != 0 and not self.printed:
			print "\tThe item with index ",self.index," was used ",self.used," times"
			self.printed = True

def mochila(doc):
	w = input("tamano de mochila?: ")
	items = parser_mochila(doc)
	K = [0] * (w+1)
 	best_config = [[]] * (w+1)

	# Algorithm for the rucksack problem 
	for i in xrange(1,w+1):
		maxim_val = -float("inf")
		for elem in items:
			tmp_w = elem.getWeight()
			tmp_max = K[i-tmp_w] + elem.getValue()
			if tmp_w <= i and tmp_max > maxim_val:
				maxim_val = tmp_max
				maxim_w = tmp_w	
				maxim_elem = elem
				
		best_config[i] = best_config[(i-maxim_w)] + [maxim_elem] 
		K[i] = maxim_val
	
	print "The maximized value of the rucksack with these items is: ", K[w]

	best_config = best_config[w] # Our solution is the last row of the matrix	
	
	# In order to get the number of times an element is used, these operations are made:
	map(lambda x: x.use(), best_config) 
	print "The items used are: "
	for elem in best_config:
		elem.printItem()

# Parser of the file	
def parser_mochila(doc):
	with open(doc,'r') as archivo:
		parsed = []
		index=1
		for line in archivo:
			value = [int(s) for s in line[:-1].split() if s.isdigit()] 
			parsed.append( Item(index, value[0], value[1]) )
			index+=1
	return parsed

	
	
	
## Christian Jose Soler : Algoritmo enumerativo del sudoku
## Analisis de eficiencia : Este algoritmo al ser enumerativo, tiene complejidad asimptoticamente igual al de una busqueda exhaustiva, pero como hay heuristicas inteligentes que hacen que algunas posibilidades no se comprueben, es algo mas optimo. Al usarse generadores en lugar de listas para la recursion, la cantidad de memoria usada es algo mas optima.

## Class that represents the Sudoku object
class Sudoku9x9():
	def __init__(self):
		# Initialization of the sudoku as a matrix full of False's
		self.sudoku = map (lambda x: [Sudoku9x9Item(x,y) for y in xrange(9)], xrange(9))
	# Method that assigns a value to a field of sudoku
	def fill(self,row,col,value):
		self.sudoku[row][col].setValue(value)
	
	# Getter of a field
	def get(self,row,col):
		return self.sudoku[row][col]
	# Getter of the value of a field
	def getValue(self,row,col):
		return self.sudoku[row][col].getValue()
	
	# Method to print the sudoku on screen
	def printSudoku(self):
		for elem1 in self.sudoku:
			for elem2 in elem1:
				print elem2.getValue(), "\t",
			print ""
		print ""

## Class that represents an element of the sudoku
class Sudoku9x9Item():
	def __init__(self,row,col,value=False):
		self.row = row
		self.col = col
		self.value = value

	#Getters and setters
	def getRow(self):
		return self.row
	def getCol(self):
		return self.col
	def getValue(self):
		return int(self.value)
	def setValue(self, value):
		self.value = value
	
	# Method that checks from 1-9 which numbers can go in the current field and yields them one by one
	def possibilities_iter(self):
		for i in xrange(1,10):
			if not self.checkElem(i):
				yield i

	# Method that returns all the possible values from 1-9 that can go in this field of sudoku
	def getPossibilities(self):
		poss = []	
		for i in xrange(1,10):
			if not self.checkElem(i):
				poss.append(i)
		return poss						
	
	# Method that checks whether the value placed in this field of sudoku is possible to be here (for the initial check)
	def isPossible(self):		
		if self.checkElem(self.value):
			return False
		return True

	# Method that checks if the value to be placed is already in the same row, column or block	
	def checkElem(self,value):
		for j in xrange(0,9):
			if (value == sudoku.getValue(self.row,j) and j != self.col) or (value == sudoku.getValue(j,self.col) and j != self.row):
				return True

		tmp_row = (self.row) - (self.row % 3) 
		tmp_col = (self.col) - (self.col % 3)

		for j in xrange(0,3):
			if tmp_row + j != self.row:
				for k in xrange(0,3):
					if tmp_col + k != self.col and value == sudoku.getValue(tmp_row + j,tmp_col + k):
						return True
		return False

def sudoku_solver(doc):
	global sudoku
	sudoku = Sudoku9x9()
	parser_sudoku(doc)
	print "The initial sudoku is: "
	sudoku.printSudoku();
	if not initialcheck():
		print "There's no solution for this sudoku"
		return	
	resolt = solve(0,0)
	if resolt and satisfy():
		print "\nThe solved sudoku is: "
		resolt.printSudoku()
	else:
		print "There's no solution for this sudoku"

# Module that checks if the initial sudoku has any visible initial condition that makes it not to have a solution (numbers wrongly placed, eg. two 2's in the same row)
	# It also checks where are fields that have only 1 possible number to place in, in such case, it is already placed (it avoids unnecessary recursion branches)
def initialcheck():
	for row in xrange(9):
		for col in xrange(9):
			if sudoku.getValue(row,col):
				if not sudoku.get(row,col).isPossible():
					return False
			else:
				tmp = sudoku.get(row,col).getPossibilities()
				if len(tmp) == 1:
					sudoku.fill(row,col,tmp[0])
	return True

# Module that really solves the sudoku recursively
def solve(row,col):
	if not sudoku.getValue(row,col):
		for elem in sudoku.get(row,col).possibilities_iter():
			sudoku.fill(row,col,elem)
			if col == 8:
				if row == 8:
					return sudoku
				tmp = solve(row+1, 0)
			else:
				tmp = solve(row, col+1)
			if tmp:
				return tmp
		sudoku.fill(row,col,False)
		return

	else:
		if col == 8:
			if row == 8:
				return sudoku
			return solve(row+1, 0)
		else:
			return solve(row, col+1)
	
# Function satisfy that checks if all elements in the matrix are well placed
def satisfy():
	for i in xrange(9):
		for j in xrange(9):
			if not sudoku.get(i,j).isPossible(): 
				return False
	return True

# Parser of the file that makes the initial sudoku matrix
def parser_sudoku(doc):
	with open(doc,'r') as archivo:
		row = 0
		col = 0
		for line in archivo:
			for elem in line:
				if elem != "." and col < 9:
					sudoku.fill(row,col,elem)
				col += 1
			row += 1
			col = 0
