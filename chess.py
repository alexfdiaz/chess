'''
TODO:
- Castling (King side and Queen side)
- Check and check mate
- En passant
- Promotion
- Legal moves (avoid checks)
- Piece notation 
- FEN notation
- PGN notation
- Flip board
- Show coordinates
- SFX
- Highlight last move
- GUI
- Timer
- AI (position score, minimax, alpha beta prune)
'''

import pygame, sys
from pygame.locals import *
from board import Board

pygame.init()
WINSIZE = (512, 512)
win = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

board = Board()
board.init()

def getMousePos():
	x, y = pygame.mouse.get_pos()
	return x // (WINSIZE[0] // 8), y // (WINSIZE[1] // 8)

def drawWindow():
	board.draw(win, WINSIZE[0], WINSIZE[1])

	if selected is not None:

		for move in board.moves(selected):
			if board.pieces[move] is None:
				if (move[0] + move[1]) % 2 == 0:
					pygame.draw.circle(win, (179, 163, 136), (move[0] * 64 + 32, move[1] * 64 + 32), 12)
				else:
					pygame.draw.circle(win, (135, 101, 72), (move[0] * 64 + 32, move[1] * 64 + 32), 12)
			else:
				if (move[0] + move[1]) % 2 == 0:
					pygame.draw.circle(win, (179, 163, 136), (move[0] * 64 + 32, move[1] * 64 + 32), 32, 6)
				else:
					pygame.draw.circle(win, (135, 101, 72), (move[0] * 64 + 32, move[1] * 64 + 32), 32, 6)

	for pos in board.pieces:
		if board.pieces[pos] is not None:
			board.pieces[pos].draw(win, pos)

	pygame.display.update()


turnCounter = 0
selected = None

board.moves((3, 1))

run = True
while run:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mousePos = getMousePos()

			if selected is not None:
				if mousePos in board.moves(selected):
					board.pieces[selected].moved = True
					board.pieces[mousePos] = board.pieces[selected]
					board.pieces[selected] = None
					selected = None
					turnCounter += 1

			
			if board.pieces[mousePos] is not None:

				if turnCounter % 2 == 0:
					if board.pieces[mousePos].color == 'w':
						if not board.pieces[mousePos].selected:

							for pos in board.pieces:
								if board.pieces[pos] is not None:
									board.pieces[pos].selected = False

							board.pieces[mousePos].selected = True
							selected = mousePos
							#print(f'piece selected {board.pieces[mousePos].moved}')

						else:
							board.pieces[mousePos].selected = False
							selected = None
							#print('piece deselected')

				else:
					if board.pieces[mousePos].color == 'b':
						if not board.pieces[mousePos].selected:

							for pos in board.pieces:
								if board.pieces[pos] is not None:
									board.pieces[pos].selected = False

							board.pieces[mousePos].selected = True
							selected = mousePos
							#print(f'piece selected {board.pieces[mousePos].moved}')

						else:
							board.pieces[mousePos].selected = False
							selected = None
							#print('piece deselected')

	drawWindow()

pygame.quit()