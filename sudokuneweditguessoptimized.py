import numpy as np
from copy import copy
import time

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

	def set_cell(self, x, y):
		None
		# set
		# update

	#possible moves should return a list for cell x,y


	def possible_moves(self, x, y):
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if self.puzzle_array[x][y] == 0:
			#----------------
			#Check column, row, box for numbers already known
			#and remove from possiilities list for each cell.
			#----------------
			#row
			#----------------
			for i in range(9):
				if self.puzzle_array[x][i] in b:
					b.remove(self.puzzle_array[x][i])
			#----------------
			#column
			#----------------
			for i in range(9):
				if self.puzzle_array[i][y] in b:
					b.remove(self.puzzle_array[i][y])
			#----------------
			#box
			#----------------
			for i in range(modx , modx + 3):
				for j in range(mody , mody + 3):
					if self.puzzle_array[i][j] in b:
						b.remove(self.puzzle_array[i][j])
			if len (b) == 1:
				self.puzzle_array[x][y] = b[0]
		else:
			b = [self.puzzle_array[x][y]]
			self.count = self.count + 1
		self.possibles_list[x][y] = b

	def inferred_moves(self, x, y):
		modx = (x//3)*3
		mody = (y//3)*3
		if self.puzzle_array[x][y] == 0:
			#----------------
			#for each cell checks possibilities of each cell in column, row, box
			#if possibility is not in any other cell it sets the cell to that possibility
			#----------------
			#row
			#----------------
			for possibility in self.possibles_list[x][y]:
				possible_counter = 0
				for i in range(9):
					if possibility not in self.possibles_list[x][i]:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					self.puzzle_array[x][y] = possibility
					return
			#----------------
			#column
			#----------------
			for possibility in self.possibles_list[x][y]:
				possible_counter = 0
				for i in range(9):
					if possibility not in self.possibles_list[i][y]:
						possible_counter = possible_counter + 1
				if possible_counter == 8:
					self.puzzle_array[x][y] = possibility
					return
			#----------------
			#box
			#----------------
			for possibility in self.possibles_list[x][y]:
				possible_counter = 0
				for i in range(modx , modx + 3):
					for j in range(mody , mody + 3):
						if possibility not in self.possibles_list[i][j]:
							possible_counter = possible_counter + 1
				if possible_counter == 8:
					self.puzzle_array[x][y] = possibility
					return


	def rule_4(self, x, y):
		b = self.possibles_list[x][y]
		modx = (x//3)*3
		mody = (y//3)*3
		if self.puzzle_array[x][y] == 0:
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
					for i in range(9):
						if i not in range(modx, modx + 3):
							if possibility in self.possibles_list[i][y]:
								self.possibles_list[i][y].remove(possibility)
				#check row
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
								self.possibles_list[x][i].remove(possibility)

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
				self.inferred_moves(i,j)

	def is_distinct(self, list ):
		'''Auxiliary function to is_solved
		checks if all elements in a list are distinct
		(ignores 0s though)
		'''
		used = []
		for i in list:
			if i == 0:
				continue
			if i in used:
				return False
			used.append(i)
		return True

	def is_valid(self, brd ):
		'''Checks if Sudoku board is valid'''
		for i in range(9):
			row = [brd[i][0],brd[i][1],brd[i][2],
					brd[i][3],brd[i][4],brd[i][5],
					brd[i][6],brd[i][7],brd[i][8]]
			if not self.is_distinct(row):
				return False
			col = [brd[0][i],brd[1][i],brd[2][i],
					brd[3][i],brd[4][i],brd[5][i],
					brd[6][i],brd[7][i],brd[8][i]]
			if not self.is_distinct(col):
				return False
			box =  [brd[(i/3)*3+0][0+(i*3)%9],brd[(i/3)*3+0][1+(i*3)%9],brd[(i/3)*3][2+(i*3)%9],
					brd[(i/3)*3+1][0+(i*3)%9],brd[(i/3)*3+1][1+(i*3)%9],brd[(i/3)*3+1][2+(i*3)%9],
					brd[(i/3)*3+2][0+(i*3)%9],brd[(i/3)*3+2][1+(i*3)%9],brd[(i/3)*3+2][2+(i*3)%9]]
			if not self.is_distinct(box):
				return False
		return True

	def callsolves(self):
		self.possible_moves_board()
		self.inferred_moves_board()
		self.rule_4_board()
		self.inferred_moves_board()

	def guess(self):
		b = list(np.array(self.puzzle_array).flatten())
		empties = b.count(0)
		if empties == 0:
			return self.is_valid(self.puzzle_array)
		startlength = 9
		x = 0
		y = 0
		for i in range(9):
			for j in range (9):
				if self.puzzle_array[i][j] == 0:
					length = len(self.possibles_list[i][j])
					if length <= startlength:
						startlength = length
						x = i
						y = j
		b = self.possibles_list[x][y]
		brd2 = copy(self.puzzle_array)
		list2 = copy(self.possibles_list)
		for possibility in b:
			brd2[x][y] = possibility
			board = np.array(brd2).flatten()
			sudokuguess = Sudoku(list(board))
			if sudokuguess.solve_sudoku() and self.is_valid(brd2):
				return True
		return False





	def solve_sudoku(self):
		self.chop_puzzle()
		#is the board full?
		self.callsolves()
		self.callsolves()
		b = list(np.array(self.puzzle_array).flatten())
		empties = b.count(0)
		if empties == 0 and self.is_valid(self.puzzle_array):
			print "filled"
			self.print_board()
		if self.guess() and self.is_valid(self.puzzle_array):
			return True
		return False


board = ["game..", "game2..."]
board = "300200000000107000706030500070009080900020004010800050009040301000702000000008006"
board2 = ".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"
board3 = "000096080026107904108000007004009000600503012000760000900804020031025090850071436"
board4 = ".....7....9...1.......45..6....2.....36...41.5.....8.9........4....18....815...32"
board5 = ".8.4.....13...............84....1...5.7..2..3...9..1......2.78.2....6.3..76..3..9"
sudoku1 = Sudoku(board5)

# tests
# print "empty"
# sudoku1.chop_puzzle()
# sudoku1.print_board()

# start_time = time.time()
# sudoku1.solve_sudoku()
# print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
file = open('msk_009.txt', 'r')
import time
start_time = time.time()
for line in file:
	board = str(line).strip("\n")
	print board
	sudokupuzzles = Sudoku(board)
	sudokupuzzles.solve_sudoku()
print("--- %s seconds ---" % (time.time() - start_time))



