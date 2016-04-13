#This is a sudoku solver. Imports a sudoku text file and prints the solution.

#making edits

class Sudoku(object):

	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.puzzle_array = [[0 for j in range(9)] for i in range(9)]
		self.possibles_list = [[[1,2,3,4,5,6,7,8,9] for j in range(9)] for i in range(9)]
		self.count = 0
		# TODO: self.init_board()

	def print_puzzle(self):
		# for line in self.puzzle:
		i = 0
		while i <= 8:
			print self.puzzle[i*9:9+i*9]
			i = i + 1

	# TODO: maybe rename this to init_board or something
	# and call it in the __init__
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

	# TODO: instead of setting a possibles_list, this function should just return the list
	def possible_moves(self, x, y):
		a = self.puzzle_array[x][y]
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if a == 0:
			for i in range(9):
				if self.puzzle_array[x][i] in b:
					b.remove(self.puzzle_array[x][i])
			for i in range(9):
				if self.puzzle_array[i][y] in b:
					b.remove(self.puzzle_array[i][y])
			for i in range(modx , modx + 3 ):
				for j in range (mody , mody + 3 ):
					if self.puzzle_array[i][j] in b:
						b.remove(self.puzzle_array[i][j])
			self.possibles_list[x][y] = b
		else:
			self.possibles_list[x][y] = [a]
		#print self.possibles_list[x][y]

	#
	# TODO: implement this, using the logic in your email. You should be able to use possible_moves
	#
	def inferred_moves(self, i, j):
		print "implement inferred_moves"
		
	def possible_moves_board(self):
		self.count = 0
		for i in range(9):
			for j in range (9):
				# you should call this like: self.possible_moves(i, j)
				Sudoku.possible_moves(self,i,j)
				# moves = self.possible_moves(i, j)
				# if len(moves) == 1:
				if len(self.possibles_list[i][j]) == 1:
					self.puzzle_array[i][j] = self.possibles_list[i][j][0]
					# self.print_board()
					Sudoku.print_board(self)
					self.count = self.count + 1
	
	def solve_sudoku(self):
		# TODO: instead of self.count != 81
		# maybe have a method called completed() which returns true/false
		# while not self.completed():
		while self.count != 81:
			# self.find_and_fill_next_possible_move()
			Sudoku.possible_moves_board(self)
		Sudoku.print_board(self)











board = ["game..", "game2..."]
board = ".9..8..2.71.2....8.685........4.2.15.5.798.349..1..7.6.7.3.4.62.26..135...39..14."
sudoku1 = Sudoku(board)

sudoku1.print_puzzle()
sudoku1.chop_puzzle()
sudoku1.print_board()
sudoku1.possible_moves(0,1)
sudoku1.possible_moves_board()
sudoku1.solve_sudoku()



