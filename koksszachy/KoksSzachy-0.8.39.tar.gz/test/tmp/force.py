#!/usr/bin/env python3

import sys
sys.path.insert(0, "../../koksszachy")

from engine import KoksSzachy

MAXVAL = 10000
depth = 5
#fen = "r1b2k1r/pp1pQppp/3P4/5P2/8/5N2/4KP1P/qN3B1R b - - 3 19"
#fen = "r1b2k1r/pp1p1ppp/3P4/5P2/8/4QN2/4KP1P/qN3B1R w - - 2 19"
#fen = "r1br3k/pp1p1pp1/1n2pN1B/2p1P3/4B2Q/2P4P/P1P2P2/R3K3 b Q - 0 19"
#fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
fen = "r1b1k3/ppp1nQ2/4P1pN/2q5/8/6P1/5PBP/R3R1K1 b - - 2 28"
v = KoksSzachy(fen)
moves = list(v.game.legal_moves)
x = v.iter_deep(5)
print(x)
