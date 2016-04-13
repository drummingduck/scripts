#This is a sudoku solver. Imports a sudoku text file and prints the solution.

#making edits

class Sudoku(object):

	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.puzzle_array = [[0 for j in range(9)] for i in range(9)]
		self.possibles_list = [[[1,2,3,4,5,6,7,8,9] for j in range(9)] for i in range(9)]
		self.count = 0
		self.runs = 0

	def print_puzzle(self):
		# for line in self.puzzle:
		i = 0
		while i <= 8:
			print self.puzzle[i*9:9+i*9]
			i = i + 1

	def chop_puzzle(self):
		# for line in self.puzzle:
		for h in range(9):
			for j in range(9):
				a = self.puzzle[(h*9) + j]
				if a == '.':
					None
				else:
					self.puzzle_array[h][j] = int(a)
		print self.puzzle_array

	def print_board(self):
		# for h in range(9):
		print "board"
		for row in self.puzzle_array:
			print row

	def possible_moves(self, x, y):
		a = self.puzzle_array[x][y]
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if a == 0:
			#----------------
			#Check column, row, box for numbers already known
			#and remove from possiilities list for each cell.
			#----------------
			#column
			#----------------
			for i in range(9):
				if self.puzzle_array[x][i] in b:
					b.remove(self.puzzle_array[x][i])
			#----------------
			#row
			#----------------
			for i in range(9):
				if self.puzzle_array[i][y] in b:
					b.remove(self.puzzle_array[i][y])
			#----------------
			#box
			#----------------
			for i in range(modx , modx + 3 ):
				for j in range (mody , mody + 3 ):
					if self.puzzle_array[i][j] in b:
						b.remove(self.puzzle_array[i][j])
			self.possibles_list[x][y] = b
		else:
			self.possibles_list[x][y] = [a]

	def inferred_moves(self, x, y):
		a = self.puzzle_array[x][y]
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if a == 0:
			#----------------
			#for each cell checks possibilities of each cell in column, row, box
			#if possibility is not in any other cell it sets the cell to that possibility
			#----------------
			#column
			#----------------
			possible_counter = 0
			for possiblity in b:
				for i in range(9):
					if possiblity in self.possibles_list[x][i]:
						pass
					else:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					a = possiblity
			#----------------
			#row
			#----------------
			possible_counter = 0
			for possiblity in b:
				for i in range(9):
					if possiblity in self.possibles_list[i][y]:
						pass
					else:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					a = possiblity
			#----------------
			#box
			#----------------
			possible_counter = 0
			for possiblity in b:
				for i in range(modx , modx + 3 ):
					for j in range (mody , mody + 3 ):
						if possiblity in self.possibles_list[i][j]:
							pass
						else:
							possible_counter = possible_counter + 1
				if possible_counter == 8:
					a = possiblity
		else:
			None

			#----------------
			#----------------
	#def rule_4(self)
			#this needs to be rule 4
			#----------------
	#def naked_pairs(self)
	#def lines(self)
			#http://byteauthor.com/2010/08/sudoku-solver-update/
			#----------------
			#----------------
	def possible_moves_board(self):
		self.count = 0
		for i in range(9):
			for j in range (9):
				self.possible_moves(i,j)
				moves = self.possibles_list[i][j]
				if len(moves) == 1:
					self.puzzle_array[i][j] = self.possibles_list[i][j][0]
					self.count = self.count + 1
				self.inferred_moves(i,j)


	def solve_sudoku(self):
		import time
		start_time = time.time()
		while self.count != 81:
			self.possible_moves_board()
			self.runs = self.runs + 1
		self.print_board()
		print "number of runs through board:"
		print self.runs
		print("--- %s seconds ---" % (time.time() - start_time))











board = ["game..", "game2..."]
board = ".9..8..2.71.2....8.685........4.2.15.5.798.349..1..7.6.7.3.4.62.26..135...39..14."
board2 = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"
sudoku1 = Sudoku(board)

sudoku1.print_puzzle()
sudoku1.chop_puzzle()
sudoku1.print_board()
sudoku1.possible_moves(0,1)
sudoku1.possible_moves_board()
sudoku1.solve_sudoku()








