# PROJECT 3

# Chess library

import chess
 
# WE Can see the chessboard 
board=chess.Board()

# There are some legal moves which we need to choose and play chess.
board.legal_moves                       
# Nh3, Nf3, Nc3, Na3, h3, g3, f3, e3, d3, c3, b3, a3, h4, g4, f4, e4, d4, c4, b4, a4

# this is the syntax to move any one of them
board.push_san("h3")

print(board)

