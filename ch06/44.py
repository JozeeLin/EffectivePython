#!/usr/bin/env python
# coding=utf-8

import pickle
import copyreg


#class GameState(object):
#    def __init__(self):
#        self.level = 0
#        self.lives = 4
#
#
#state = GameState()
#state.level += 1 #Player beat a level
#state.lives -= 1 #Player had to try again
#
#state_path = '/tmp/game_state.bin'
#with open(state_path, 'wb') as f:
#    pickle.dump(state, f)


class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    '''对构造器的小小封装'''
    return GameState(**kwargs)

copyreg.pickle(GameState, pickle_game_state)
# 开始原来的序列化和反序列化操作
state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)


class GameState(object):
    def __init__(self, level=0,lives=4,points=0,magic=5):
        self.level = level
        self.lives = lives
        self.points = points
        self.magic = magic

new_state_after = pickle.loads(serialized) #使用新的类对象来反序列化就的pickle数据
print(new_state_after.__dict__)


class BetterGameState(object):
    def __init__(self, level=0, points=0, magic=5):
        pass

copyreg.pickle(BetterGameState, pickle_game_state)
state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized[:35])

