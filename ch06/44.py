#!/usr/bin/env python
# coding=utf-8

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4


state = GameState()
state.level += 1 #Player beat a level
state.lives -= 1 #Player had to try again

state_path = '/tmp/game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)
