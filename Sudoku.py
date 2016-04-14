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
		print "- - - - - - - - - - - - -"
		for i in range(3):
			line = self.puzzle_array[i]
			print "| %d %d %d | %d %d %d | %d %d %d |" % (
				line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
		print "| - - - - - - - - - - - |"
		for i in range(3,6):
			line = self.puzzle_array[i]
			print "| %d %d %d | %d %d %d | %d %d %d |" % (
				line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
		print "| - - - - - - - - - - - |"
		for i in range(6,9):
			line = self.puzzle_array[i]
			print "| %d %d %d | %d %d %d | %d %d %d |" % (
				line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
		print "- - - - - - - - - - - - -"

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
				if i != y:
					if self.puzzle_array[x][i] in b:
						b.remove(self.puzzle_array[x][i])
			#----------------
			#row
			#----------------
			for i in range(9):
				if i != x:
					if self.puzzle_array[i][y] in b:
						b.remove(self.puzzle_array[i][y])
			#----------------
			#box
			#----------------
			for i in range(modx , modx + 3):
				for j in range(mody , mody + 3):
					if i != x and j != y:
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
			for possibility in b:
				possible_counter = 0
				for i in range(9):
					if possibility not in self.possibles_list[x][i]:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					b = [possibility]
			#----------------
			#row
			#----------------
			for possibility in b:
				possible_counter = 0
				for i in range(9):
					if possibility not in self.possibles_list[i][y]:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					b = [possibility]
			#----------------
			#box
			#----------------
			for possibility in b:
				possible_counter = 0
				for i in range(modx , modx + 3):
					for j in range(mody , mody + 3):
						if possibility not in self.possibles_list[i][j]:
							possible_counter = possible_counter + 1
				if possible_counter == 8:
					b = [possibility]
			self.possibles_list[x][y] = b

	def rule_4(self, x, y):
		a = self.puzzle_array[x][y]
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if a == 0:
			for possibility in b:
				#check row
				tick = 0
				for i in range(modx , modx + 3):
					if possibility in self.possibles_list[i][y]:
						tick = tick + 1
				possible_counter = 0
				for i in range(modx , modx + 3):
					for j in range(mody , mody + 3):
						if possibility in self.possibles_list[i][j]:
							possible_counter = possible_counter + 1
				#remove possibilities from row outside box
				if possible_counter == tick:
					for i in range(0, 9):
						if i not in range(modx, modx + 3):
							if possibility in self.possibles_list[i][y]:
								c = self.possibles_list[i][y]
								c.remove(possibility)
				#check column
				tick = 0
				for i in range(mody , mody + 3):
					if possibility in self.possibles_list[x][i]:
						tick = tick + 1
				possible_counter = 0
				for i in range(modx , modx + 3):
					for j in range(mody , mody + 3):
						if possibility in self.possibles_list[i][j]:
							possible_counter = possible_counter + 1
				#remove possibilities from row outside box
				if possible_counter == tick:
					for i in range(0, 9):
						if i not in range(mody, mody + 3):
							if possibility in self.possibles_list[x][i]:
								c = self.possibles_list[x][i]
								c.remove(possibility)
		else:
			None

			#----------------
	#def naked_pairs(self)
	#def lines(self)
			#http://byteauthor.com/2010/08/sudoku-solver-update/
			#----------------
			#----------------
	# def guess(self):
	# 	test_board = self.puzzle_array
	# 	for i in range(9):
	# 		for j in range (9):
	# 			a = test_board[i][j]
	# 			b = self.possibles_list[i][j]
	# 			if a = 0:
	# 				for possibility in b:




	def possible_moves_board(self):
		self.count = 0
		for i in range(9):
			for j in range (9):
				self.possible_moves(i,j)
				self.inferred_moves(i,j)
				self.rule_4(i,j)
				moves = self.possibles_list[i][j]
				if len(moves) == 1:
					self.puzzle_array[i][j] = self.possibles_list[i][j][0]
					self.count = self.count + 1
		#if self.count >= 50:
		#	self.guess()


	def solve_sudoku(self):
		import time
		start_time = time.time()
		while self.runs != 10:
			self.possible_moves_board()
			self.runs = self.runs + 1
			self.print_board()
			print self.possibles_list[6][0]
			print self.possibles_list[6][1]
			print self.possibles_list[6][2]
			print self.possibles_list[7][0]
			print self.possibles_list[7][1]
			print self.possibles_list[7][2]
			print self.possibles_list[8][0]
			print self.possibles_list[8][1]
			print self.possibles_list[8][2]
			print "bottom corner"
			print self.possibles_list[6][6]
			print self.possibles_list[6][7]
			print self.possibles_list[6][8]
			print self.possibles_list[7][6]
			print self.possibles_list[7][7]
			print self.possibles_list[7][8]
			print self.possibles_list[8][6]
			print self.possibles_list[8][7]
			print self.possibles_list[8][8]
			print self.count
		self.print_board()
		print "number of runs through board:"
		print self.runs
		print("--- %s seconds ---" % (time.time() - start_time))











board = ["game..", "game2..."]
board = ".9..8..2.71.2....8.685........4.2.15.5.798.349..1..7.6.7.3.4.62.26..135...39..14."
board2 = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"
sudoku1 = Sudoku(board2)

sudoku1.print_puzzle()
sudoku1.chop_puzzle()
sudoku1.print_board()
sudoku1.possible_moves(0,1)
sudoku1.possible_moves_board()
sudoku1.solve_sudoku()









