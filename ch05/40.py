#!/usr/bin/env python
# coding=utf-8
from collections import namedtuple

# 1=========================
#def my_coroutine():
#    while True:
#        received = yield
#        print('Received: ', received)
#
#
#it = my_coroutine()
#next(it)
#it.send('First')
#it.send('Second')


# 2===============================
#def minimize():
#    current = yield # 第一次启动的时候,第一个数就是当前最小值;即current保存着当前最小值
#    while True:
#        value = yield current
#        current = min(value, current)
#
#it = minimize()
#next(it)
#print(it.send(10))
#print(it.send(4))
#print(it.send(22))
#print(it.send(-1))


ALIVE = '*'
EMPTY = '-'
Query = namedtuple('Query',('y','x'))

def count_neighbors(y, x):
    n_ = yield Query(y+1, x+0) # North
    ne = yield Query(y+1, x+1) # Northeast
    e_ = yield Query(y+0, x+1) # East
    se = yield Query(y-1, x+1) # SouthEast
    s_ = yield Query(y-1, x+0) # South
    sw = yield Query(y-1, x-1) # SouthWest
    w_ = yield Query(y+0, x-1) # West
    nw = yield Query(y+1, x-1) # NorthWest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count +=1
    return count

# 3================================
#it = count_neighbors(10, 5)
#q1 = next(it)
#print('First yield: ', q1)
#q2 = it.send(ALIVE)
#print('Second yield: ', q2)
#q3 = it.send(ALIVE)
#print('Third yield: ', q3)
#q4 = it.send(ALIVE)
#print('fourth yield: ', q4)
#q5 = it.send(ALIVE)
#print('fifth yield: ', q5)
#q6 = it.send(ALIVE)
#print('sixth yield: ', q6)
#q7 = it.send(ALIVE)
#print('seventh yield: ',q7)
#q8 = it.send(EMPTY)
#print('eighth yield: ', q8)
#try:
#    count = it.send(EMPTY)
#except StopIteration as e:
#    print('Count: ', e.value)



Transition = namedtuple('Transition', ('y','x','state'))

def step_cell(y, x):
    state = yield Query(y,x)
    neighbors = yield from count_neighbors(y,x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors<2: # Die: Too few
            return EMPTY
        elif neighbors>3: # Die: Too many
            return EMPTY
    else:
        if neighbors == 3: # Regenerate
            return ALIVE
    return state

# 4=========================================
#it = step_cell(10, 5)
#q0 = next(it)
#print('Me:', q0)
#q1 = it.send(ALIVE) # Send my state, get neighbor Query
#print('First yield: ', q1)
#q2 = it.send(ALIVE)
#print('Second yield: ', q2)
#q3 = it.send(ALIVE)
#print('Third yield: ', q3)
#q4 = it.send(ALIVE)
#print('fourth yield: ', q4)
#q5 = it.send(ALIVE)
#print('fifth yield: ', q5)
#q6 = it.send(ALIVE)
#print('sixth yield: ', q6)
#q7 = it.send(ALIVE)
#print('seventh yield: ',q7)
#q8 = it.send(EMPTY)
#print('eighth yield: ', q8)
#t1 = it.send(EMPTY) # get game decision,send EMPTY for no one
#print('Outcome:',t1)


TICK = object()
def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK

class Grid(object):
    '''代表整张网格的类'''
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY]*self.width)

    def __str__(self):
        result = ''
        for i in range(self.height):
            result+=(''.join(self.rows[i])+'\n')
        return result[:-1]

    def query(self, y,x):
        return self.rows[y%self.height][x%self.width] #使用模运算避免坐标越界情况

    def assign(self, y, x, state):
        self.rows[y%self.height][x%self.width] = state

def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else: # Must be a Transition
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)

    return progeny

# 初始化一个网格,并设置所有细胞的初始状态
grid = Grid(5,9)
grid.assign(0,3,ALIVE)
grid.assign(1,4,ALIVE)
grid.assign(2,2,ALIVE)
grid.assign(2,3,ALIVE)
grid.assign(2,4,ALIVE)
print(grid)


class ColumnPrinter(object):
    def __init__(self):
        self.all_grids = []

    def append(self, grid_str):
        grid_str = grid_str.split('\n')
        self.all_grids.append(grid_str)

    def __str__(self):
        result = ''
        if not len(self.all_grids):
            return result
        width = int(len(self.all_grids[0][0])/2)
        for i in range(len(self.all_grids)):
            result += ' '*width
            result += str(i)
            result += ' '*width
            result += '|'
        result = result[:-1]+'\n'
        for row_num in range(len(self.all_grids[0])):
            rows = []
            for i in range(len(self.all_grids)):
                rows.append(self.all_grids[i][row_num])
            rows = '|'.join(rows)
            rows = rows[:-1]+'\n'
            result += rows
        return result[:-1]

columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
print(columns)
for i in range(5):
    columns.append(str(grid))

    grid = live_a_generation(grid, sim)

print(columns)
