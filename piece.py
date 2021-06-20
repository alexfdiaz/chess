import pygame

class Piece:
	def __init__(self, color, piece, inCheck = False, moved = False):
		self.color = color
		self.piece = piece
		self.inCheck = inCheck
		self.moved = moved
		self.selected = False


		if self.color == 'w':
			if self.piece == 'k':
				self.img = pygame.image.load('images/white_king.png')
			elif self.piece == 'q':
				self.img = pygame.image.load('images/white_queen.png')
			elif self.piece == 'b':
				self.img = pygame.image.load('images/white_bishop.png')
			elif self.piece == 'n':
				self.img = pygame.image.load('images/white_knight.png')
			elif self.piece == 'r':
				self.img = pygame.image.load('images/white_rook.png')
			elif self.piece == 'p':
				self.img = pygame.image.load('images/white_pawn.png')
		elif self.color == 'b':
			if self.piece == 'k':
				self.img = pygame.image.load('images/black_king.png')
			elif self.piece == 'q':
				self.img = pygame.image.load('images/black_queen.png')
			elif self.piece == 'b':
				self.img = pygame.image.load('images/black_bishop.png')
			elif self.piece == 'n':
				self.img = pygame.image.load('images/black_knight.png')
			elif self.piece == 'r':
				self.img = pygame.image.load('images/black_rook.png')
			elif self.piece == 'p':
				self.img = pygame.image.load('images/black_pawn.png')

	def moves(self, location):
		if self.piece == 'k':
			for y in range(location[1] - 1, location[1] + 2):
				for x in range(location[0] - 1, location[0] + 2):
					if True:
						pass

	def draw(self, surface, location):
		surface.blit(self.img, (location[0] * self.img.get_width(), location[1] * self.img.get_height()))
