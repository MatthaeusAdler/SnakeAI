from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from keras.models import Sequential
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import numpy as np
import pandas as pd
import random
from random import sample, randint

import sys
sys.path.append("..") 

import numpy as np
import tensorflow as tf

from actors import Actor
from game import Actions
from game import Directions
from settings import *

INPUT_SIZE=11
# INPUT_SIZE=57
# INPUT_SIZE=GAME_SIZE**2+GAME_SIZE*4+4
RANDOMNESS=0.4

class ActorAi(Actor):
    def __init__(self, max_retries, learn):
        self.retries = 0
        self.max_retries = max_retries
        self.reward = 0
        self.gamma = 0.9
        self.short_memory = np.array([])
        self.learning_rate = 0.0005
        self.model = self.network()        
        self.epsilon = 0
        self.memory = []
        self.old_state=np.asarray([])
        self.last_move=0
        self.old_distance=0
        self.oldpoints=0
        self.learning=(1 if learn else 0)
        self.can_move=True

    def is_ai(self):
        return True

    def network(self):
        model = Sequential()
        model.add(Dense(units=80, activation='relu', input_dim=INPUT_SIZE))
        model.add(Dropout(0.20))
        model.add(Dense(units=60, activation='relu'))
        model.add(Dropout(0.20))
        model.add(Dense(units=3, activation='linear'))
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)
        model.load_weights('weights.hdf5')
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))


    def replay_new(self, memory):
        if not self.learning:
            return
        if len(memory) > 1000:
            minibatch = random.sample(memory, 1000)
        else:
            minibatch = memory
        for state, action, reward, next_state, done in minibatch:
            target = reward
            target = reward + self.gamma * np.amax(self.model.predict(np.array([next_state]))[0])
            target_f = self.model.predict(np.array([state]))
            target_f[0][action] = target
            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)


    def train_short_memory(self, state, action, reward, next_state, done):
        target = reward
        target = reward + self.gamma * np.amax(self.model.predict(next_state.reshape((1, INPUT_SIZE)))[0])
        target_f = self.model.predict(state.reshape((1, INPUT_SIZE)))
        target_f[0][action] = target

        self.model.fit(state.reshape((1, INPUT_SIZE)), target_f, epochs=1, verbose=0)

    def is_human(self):
        return False

    def get_action(self, game ):
        new_state = self.get_state(game.snake, game.apple, game.direction)
        reward = 0
        distance=((game.apple[0]-game.snake[0][0])**2+(game.apple[1]-game.snake[0][1])**2)**(1/2.0)
        if game.gameover:
            reward = -1000
        elif game.points>self.oldpoints:
            reward = 10
        elif distance < self.old_distance:
            reward = 5
        elif distance > self.old_distance:
            if self.can_move:
                reward = -2
            else:
                reward = 1
        if self.learning:
            self.train_short_memory(self.old_state, self.last_move, reward, new_state, game.gameover)
            self.remember(self.old_state, self.last_move, reward, new_state, game.gameover)
        actions = Actions.get_possible_actions()
        if(self.learning and self.max_retries*RANDOMNESS-self.retries>randint(0, self.max_retries)):
            move = randint(0,2)
        else:
            move = np.argmax(self.model.predict(new_state.reshape((1,INPUT_SIZE)))[0])
        self.old_state=new_state
        self.last_move=move
        self.old_distance=distance
        self.oldpoints=game.points
        self.can_move=self.old_state[4] and not (game.snake[0][0]-1, game.snake[0][1]) in game.snake or self.old_state[5] and not (game.snake[0][0]+1, game.snake[0][1]) in game.snake or self.old_state[6] and not (game.snake[0][0]-1, game.snake[0][1]-1) in game.snake or self.old_state[7] and not (game.snake[0][0]-1, game.snake[0][1]+1) in game.snake
        return actions[move]


    def want_restart(self):
        self.model.save_weights('weights.hdf5')
        if self.retries < self.max_retries:
            self.retries += 1
            return True
        else:
            return False


    def get_state(self, snake, apple, direction):
        state=[
            direction==Directions.UP and (snake[0][1]==0 or (snake[0][0], snake[0][1]-1) in snake) or  direction==Directions.LEFT and (snake[0][0]==0 or (snake[0][0]-1, snake[0][1]) in snake)
            or  direction==Directions.DOWN and (snake[0][1]==GAME_SIZE-1 or (snake[0][0], snake[0][1]+1) in snake) or  direction==Directions.RIGHT and (snake[0][0]== GAME_SIZE-1 or (snake[0][0]+1, snake[0][1]) in snake),
            direction==Directions.UP and (snake[0][0]==0 or (snake[0][0]-1, snake[0][1]) in snake) or  direction==Directions.LEFT and (snake[0][1]==GAME_SIZE-1  or (snake[0][0], snake[0][1]+1) in snake)
            or  direction==Directions.DOWN and (snake[0][0]==GAME_SIZE-1 or (snake[0][0]+1, snake[0][1]) in snake) or  direction==Directions.RIGHT and (snake[0][1]== 0 or (snake[0][0], snake[0][1]-1) in snake),
            direction==Directions.UP and (snake[0][0]==GAME_SIZE-1  or (snake[0][0]+1, snake[0][1]) in snake) or direction==Directions.LEFT and (snake[0][1]==0 or (snake[0][0], snake[0][1]-1) in snake)
            or  direction==Directions.DOWN and (snake[0][0]==0  or (snake[0][0]-1, snake[0][1]) in snake) or direction==Directions.RIGHT and (snake[0][1]== GAME_SIZE-1 or (snake[0][0], snake[0][1]+1) in snake),
            direction==Directions.UP,
            direction==Directions.RIGHT,
            direction==Directions.DOWN,
            direction==Directions.LEFT,
            apple[0]<snake[0][0],
            apple[0]>snake[0][0],
            apple[1]<snake[0][1],
            apple[1]>snake[0][1]
        ]      
        for i in range(len(state)):
            if state[i]:
                state[i]=1
            else:
                state[i]=0
        # snake_proximity=[]
        # line=[]
        # for j in range (snake[0][1]-3, snake[0][1]+4):
        #     for i in range (snake[0][0]-3, snake[0][0]+4):
        #         if (i,j) in snake or i < 0 or i > GAME_SIZE-1 or j < 0 or j > GAME_SIZE-1:
        #             line.append(1)
        #         else:
        #             line.append(0)
        #     snake_proximity.append(line)
        #     line=[]
        # if direction==Directions.LEFT:
        #     snake_proximity=np.rot90(snake_proximity, 3)
        # elif direction==Directions.DOWN:
        #     snake_proximity=np.rot90(snake_proximity, 2)
        # elif direction==Directions.RIGHT:
        #     snake_proximity=np.rot90(snake_proximity, 1)
        # for line in snake_proximity:
        #     for element in line:
        #         state.append(element)
                
        # state=[
        #     direction==Directions.UP,
        #     direction==Directions.RIGHT,
        #     direction==Directions.DOWN,
        #     direction==Directions.LEFT,
        # ]
        # for i in range(len(state)):
        #     if state[i]:
        #         state[i]=1
        #     else:
        #         state[i]=0
        # for i in range (0, GAME_SIZE):
        #     for j in range (0, GAME_SIZE):
        #         if (i,j) in snake:
        #             state.append(0)
        #         else:
        #             state.append(1)
        # for i in range (0, GAME_SIZE):
        #     if snake[0][0]==i:
        #         state.append(1)
        #     else:
        #         state.append(0)
        # for j in range (0, GAME_SIZE):
        #     if snake[0][1]==j:
        #         state.append(1)
        #     else:
        #         state.append(0)
        # for i in range (0, GAME_SIZE):
        #     if apple[0]==i:
        #         state.append(1)
        #     else:
        #         state.append(0)
        # for j in range (0, GAME_SIZE):
        #     if apple[1]==j:
        #         state.append(1)
        #     else:
        #         state.append(0)

        return np.asarray(state)


    def initialize_game(self, game):
        self.old_state = self.get_state(game.snake, game.apple, game.direction) 
        self.old_distance=((game.apple[0]-game.snake[0][0])**2+(game.apple[1]-game.snake[0][1])**2)**(1/2.0)
        action=0
        game.moveSnake(Actions.get_possible_actions()[action])
