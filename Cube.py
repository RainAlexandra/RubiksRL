# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:31:08 2020

@author: RainAlex
"""

import numpy as np
import random

init_state = np.array(['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 
         'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 
         'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 
         'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 
         'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 
         'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8'], str)

sticker_count = len(init_state)

R = [[34, 21, 42, 26, 34],
     [36, 19, 44, 28, 36],
     [39, 16, 47, 31, 39],
     [0, 2, 7, 5, 0],
     [1, 4, 6, 3, 1]]

Ri = [R[i][::-1] for i in range(len(R))]

L = [[32, 24, 40, 23, 32],
     [35, 27, 43, 20, 35],
     [37, 29, 45, 18, 37],
     [8, 10, 15, 13, 8],
     [9, 12, 14, 11, 9]]

Li = [L[i][::-1] for i in range(len(L))]

F = [[37, 0, 42, 15, 37],
     [38, 3, 41, 12, 38],
     [39, 5, 40, 10, 39],
     [24, 26, 31, 29, 24],
     [25, 28, 30, 27, 25]]

Fi = [F[i][::-1] for i in range(len(F))]

B = [[2, 32, 13, 47, 2],
     [4, 33, 11, 46, 4],
     [7, 34, 8, 45, 7],
     [16, 18, 23, 21, 16],
     [17, 20, 22, 19, 17]]

Bi = [B[i][::-1] for i in range(len(B))]

U = [[24, 8, 16, 0, 24],
     [25, 9, 17, 1, 25],
     [26, 10, 18, 2, 26],
     [32, 34, 39, 37, 32],
     [33, 36, 38, 35, 33]]

Ui = [U[i][::-1] for i in range(len(U))]

D = [[13, 29, 5, 21, 13],
     [14, 30, 6, 22, 14],
     [15, 31, 7, 23, 15],
     [40, 42, 47, 45, 40],
     [41, 44, 46, 43, 41]]

Di = [D[i][::-1] for i in range(len(D))]

actions = {"R": R,
            "R'": Ri,
            "L": L,
            "L'": Li,
            "F": F,
            "F'": Fi,
            "B": B,
            "B'": Bi,
            "U": U,
            "U'": Ui,
            "D": D,
            "D'": Di
            }

    
def seq_str_arr_toggle(sequence):
    # convert string sequence to array and vice versa
    if (type(sequence) == str):
        return sequence.split()
    return ' '.join(sequence)

def generate_shuffle_seq(length=25):
    poss_actions = list(actions.keys())
    ret = [random.choice(poss_actions) for i in range(length)]
    return ' '.join(ret)

def move(state, swaps):
    next_state = state.copy()
    for s in swaps:
        from_idx = s[:-1]
        to_idx = s[1:]
        next_state[to_idx] = next_state[from_idx]
    return next_state

def move_seq(state, sequence):
    # sequence = string
    if (type(sequence) != list):
        sequence = sequence.split()
    for seq in sequence:
        state = move(state, actions[seq])
        # print(state)
    return state

def invert(action):
    # in string form
    if (action[-1] == '\''):
        return action[:-1]
    return action + "\'"

def invert_seq(sequence):
    # sequence in string form
    sequence = sequence.split()
    sequence = [invert(action) for action in sequence]
    inverted = ' '.join(reversed(sequence))
    return inverted

def check_if_solved(state):
    return sum(state == sorted(state)) == sticker_count

