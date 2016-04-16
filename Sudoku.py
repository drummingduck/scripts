#This is a sudoku solver. Imports a sudoku text file and prints the solution.

#making edits

class Sudoku(object):

	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.puzzle_array = [[0 for j in range(9)] for i in range(9)]
		self.possibles_list = [[[1,2,3,4,5,6,7,8,9] for j in range(9)] for i in range(9)]
		self.count = 0
		self.runs = 0
		self.breaks = 0


	def chop_puzzle(self):
		# for line in self.puzzle:
		for h in range(9):
			for j in range(9):
				a = self.puzzle[(h*9) + j]
				if a == '.':
					None
				else:
					self.puzzle_array[h][j] = int(a)

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
			#row
			#----------------
			for i in range(9):
				if i != y:
					if self.puzzle_array[x][i] in b:
						b.remove(self.puzzle_array[x][i])
			#----------------
			#column
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
		else:
			b = [a]
		self.possibles_list[x][y] = b
		if len (b) == 1:
			self.puzzle_array[x][y] = b[0]
			self.count = self.count + 1

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
			#row
			#----------------
			for possibility in b:
				possible_counter = 0
				for i in range(9):
					if possibility not in self.possibles_list[x][i]:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					b = [possibility]
			#----------------
			#column
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
		if len (b) == 1:
			self.puzzle_array[x][y] = b[0]
			self.possibles_list[x][y] = b

	def rule_4(self, x, y):
		a = self.puzzle_array[x][y]
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if a == 0:
			for possibility in b:
				#check column
				tick = 0
				for i in range(modx , modx + 3):
					if possibility in self.possibles_list[i][y]:
						tick = tick + 1
				possible_counter = 0
				for i in range(modx , modx + 3):
					for j in range(mody , mody + 3):
						if possibility in self.possibles_list[i][j]:
							possible_counter = possible_counter + 1
				#remove possibilities from column outside box
				if possible_counter == tick:
					for i in range(0, 9):
						if i not in range(modx, modx + 3):
							if possibility in self.possibles_list[i][y]:
								c = self.possibles_list[i][y]
								c.remove(possibility)
								self.possibles_list[i][y] = c
				#check cloumn
				tick = 0
				for i in range(mody , mody + 3):
					if possibility in self.possibles_list[x][i]:
						tick = tick + 1
				possible_counter = 0
				for i in range(modx , modx + 3):
					for j in range(mody , mody + 3):
						if possibility in self.possibles_list[i][j]:
							possible_counter = possible_counter + 1
				#remove possibilities from cloumn outside box
				if possible_counter == tick:
					for i in range(0, 9):
						if i not in range(mody, mody + 3):
							if possibility in self.possibles_list[x][i]:
								c = self.possibles_list[x][i]
								c.remove(possibility)
								self.possibles_list[x][i] = c

	def possible_moves_board(self):
		self.count = 0
		for i in range(9):
			for j in range (9):
				self.possible_moves(i,j)

	def inferred_moves_board(self):
		for i in range(9):
			for j in range (9):
				self.inferred_moves(i,j)
		self.possible_moves_board()

	def rule_4_board(self):
		for i in range(9):
			for j in range (9):
				self.rule_4(i,j)
		self.possible_moves_board()

	def valid(self):
		for i in range(9):
			for j in range (9):
				moves = self.possibles_list[i][j]
				if len(moves) == 0:
					return False
		return True

	def guess(self):
		import copy
		g = copy.deepcopy(self.puzzle_array)
		h = copy.deepcopy(self.possibles_list)
		for i in range(9):
			e = copy.deepcopy(self.puzzle_array)
			f = copy.deepcopy(self.possibles_list)
			for j in range (9):
				a = self.puzzle_array[i][j]
				b = self.possibles_list[i][j]
				if a == 0:
					c = copy.deepcopy(self.puzzle_array)
					d = copy.deepcopy(self.possibles_list)
					for possibility in b:
						self.possibles_list[i][j] = [possibility]
						self.possible_moves_board()
						self.inferred_moves_board()
						self.rule_4_board()
						self.inferred_moves_board()
						if self.valid() == False:
							self.puzzle_array = copy.deepcopy(e)
							self.possibles_list = copy.deepcopy(f)
						if self.valid() == True:
							break

	def solve_sudoku(self):
		self.chop_puzzle()
		print "empty"
		self.print_board()
		self.runs = 0
		self.count = 0
		while self.count != 81:
			self.possible_moves_board()
			self.inferred_moves_board()
			self.rule_4_board()
			self.inferred_moves_board()
			self.guess()
			self.runs = self.runs + 1
			if self.runs > 3:
				self.breaks = self.breaks + 1
				print "------- break %d -------" % self.breaks
				print self.puzzle
				self.print_board()
				quit()
				break
		print "filled"
		self.print_board()

file = open('sudokupuzzles.txt', 'r')
import time
start_time = time.time()
for line in file:
	board = str(line).strip("\n")
	sudokupuzzles = Sudoku(board)
	sudokupuzzles.solve_sudoku()
print("--- %s seconds ---" % (time.time() - start_time))

# board = ["game..", "game2..."]
# board = "300200000000107000706030500070009080900020004010800050009040301000702000000008006"
# board2 = ".....7....9...1.......45..6....2.....36...41.5.....8.9........4....18....815...32"
# sudoku1 = Sudoku(board2)
# sudoku1.solve_sudoku()








