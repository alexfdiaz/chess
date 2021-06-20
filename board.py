import pygame
from piece import Piece

class Board:
	def __init__(self):
		self.WIDTH = 8
		self.HEIGHT = 8
		self.board = [[None for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
		self.lightColor = (239, 217, 180)
		self.darkColor = (180, 136, 97)

	def init(self):
		self.pieces = {
			(0,0): Piece('b', 'r'), (1,0): Piece('b', 'n'), (2,0): Piece('b', 'b'), (3,0): Piece('b', 'q'), (4,0): Piece('b', 'k'), (5,0): Piece('b', 'b'), (6,0): Piece('b', 'n'), (7,0): Piece('b', 'r'), 
			(0,1): Piece('b', 'p'), (1,1): Piece('b', 'p'), (2,1): Piece('b', 'p'), (3,1): Piece('b', 'p'), (4,1): Piece('b', 'p'), (5,1): Piece('b', 'p'), (6,1): Piece('b', 'p'), (7,1): Piece('b', 'p'), 
			(0,2): None, (1,2): None, (2,2): None, (3,2): None, (4,2): None, (5,2): None, (6,2): None, (7,2): None,
			(0,3): None, (1,3): None, (2,3): None, (3,3): None, (4,3): None, (5,3): None, (6,3): None, (7,3): None,
			(0,4): None, (1,4): None, (2,4): None, (3,4): None, (4,4): None, (5,4): None, (6,4): None, (7,4): None,
			(0,5): None, (1,5): None, (2,5): None, (3,5): None, (4,5): None, (5,5): None, (6,5): None, (7,5): None,
			(0,6): Piece('w', 'p'), (1,6): Piece('w', 'p'), (2,6): Piece('w', 'p'), (3,6): Piece('w', 'p'), (4,6): Piece('w', 'p'), (5,6): Piece('w', 'p'), (6,6): Piece('w', 'p'), (7,6): Piece('w', 'p'),
			(0,7): Piece('w', 'r'), (1,7): Piece('w', 'n'), (2,7): Piece('w', 'b'), (3,7): Piece('w', 'q'), (4,7): Piece('w', 'k'), (5,7): Piece('w', 'b'), (6,7): Piece('w', 'n'), (7,7): Piece('w', 'r'), 

		}

	def moves(self, selected):
		self.legalMoves = []

		if self.pieces[selected].piece == 'k':
			for y in range(selected[1] - 1, selected[1] + 2):
				for x in range(selected[0] - 1, selected[0] + 2):
					if (x, y) in self.pieces and (self.pieces[(x, y)] == None or self.pieces[selected].color != self.pieces[(x, y)].color):
						self.legalMoves.append((x, y))
			if not self.pieces[selected].moved:
				if self.pieces[(selected[0] + 1, selected[1])] is None and self.pieces[(selected[0] + 2, selected[1])] is None:
					self.legalMoves.append((selected[0] + 2, selected[1]))
			

		if self.pieces[selected].piece == 'n':
			for y in range(-2, 3):
				for x in range(-2, 3):
					if x ** 2 + y ** 2 == 5:
						if (x + selected[0], y + selected[1]) in self.pieces and (self.pieces[(x + selected[0], y + selected[1])] == None or self.pieces[selected].color != self.pieces[(x + selected[0], y + selected[1])].color):
							self.legalMoves.append((x + selected[0], y + selected[1]))
			

		if self.pieces[selected].piece == 'p' and self.pieces[selected].color == 'w':
			if (selected[0], selected[1] - 1) in self.pieces and self.pieces[(selected[0], selected[1] - 1)] == None:
				self.legalMoves.append((selected[0], selected[1] - 1))
				if selected[1] == 6 and self.pieces[(selected[0], 4)] == None:
					self.legalMoves.append((selected[0], 4))
			if (selected[0] - 1, selected[1] - 1) in self.pieces and self.pieces[(selected[0] - 1, selected[1] - 1)] != None and self.pieces[selected].color != self.pieces[(selected[0] - 1, selected[1] - 1)].color:
				self.legalMoves.append((selected[0] - 1, selected[1] - 1))
			if (selected[0] + 1, selected[1] - 1) in self.pieces and self.pieces[(selected[0] + 1, selected[1] - 1)] != None and self.pieces[selected].color != self.pieces[(selected[0] + 1, selected[1] - 1)].color:
				self.legalMoves.append((selected[0] + 1, selected[1] - 1))
			

		if self.pieces[selected].piece == 'p' and self.pieces[selected].color == 'b':
			if (selected[0], selected[1] + 1) in self.pieces and self.pieces[(selected[0], selected[1] + 1)] == None:
				self.legalMoves.append((selected[0], selected[1] + 1))
				if selected[1] == 1 and self.pieces[(selected[0], 3)] == None:
					self.legalMoves.append((selected[0], 3))
			if (selected[0] - 1, selected[1] + 1) in self.pieces and self.pieces[(selected[0] - 1, selected[1] + 1)] != None and self.pieces[selected].color != self.pieces[(selected[0] - 1, selected[1] + 1)].color:
				self.legalMoves.append((selected[0] - 1, selected[1] + 1))
			if (selected[0] + 1, selected[1] + 1) in self.pieces and self.pieces[(selected[0] + 1, selected[1] + 1)] != None and self.pieces[selected].color != self.pieces[(selected[0] + 1, selected[1] + 1)].color:
				self.legalMoves.append((selected[0] + 1, selected[1] + 1))
			

		if self.pieces[selected].piece == 'r' or self.pieces[selected].piece == 'q':
			cross = [
				[(selected[0], selected[1] + i) for i in range(1, 8 - selected[1])],
				[(selected[0], selected[1] - i) for i in range(1, selected[1] + 1)],
				[(selected[0] + i, selected[1]) for i in range(1, 8 - selected[0])],
				[(selected[0] - i, selected[1]) for i in range(1, selected[0] + 1)]
			]
			for direction in cross:
				for square in direction:
					if self.pieces[square] is None:
						self.legalMoves.append(square)
					else:
						if self.pieces[selected].color != self.pieces[square].color:
							self.legalMoves.append(square)
						break
			

		if self.pieces[selected].piece == 'b' or self.pieces[selected].piece == 'q':
			cross = [
				[(selected[0] + i, selected[1] + i) for i in range(1, 8)],
				[(selected[0] - i, selected[1] - i) for i in range(1, 8)],
				[(selected[0] - i, selected[1] + i) for i in range(1, 8)],
				[(selected[0] + i, selected[1] - i) for i in range(1, 8)]
			]
			for direction in cross:
				for square in direction:
					if square in self.pieces:
						if self.pieces[square] is None:
							self.legalMoves.append(square)
						else:
							if self.pieces[selected].color != self.pieces[square].color:
								self.legalMoves.append(square)
							break
			
		return self.legalMoves


	def draw(self, surface, width, height):
		for y in range(self.HEIGHT):
			for x in range(self.WIDTH):
				if (x + y) % 2 == 0:
					pygame.draw.rect(surface, self.lightColor, (x * (width / self.WIDTH), y * (height / self.HEIGHT), width / self.WIDTH, height / self.HEIGHT))
				else:
					pygame.draw.rect(surface, self.darkColor, (x * (width / self.WIDTH), y * (height / self.HEIGHT), width / self.WIDTH, height / self.HEIGHT))
