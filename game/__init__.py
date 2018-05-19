from random import randint
from math import sin, cos, radians
from settings import *
from .directions import Directions
from .actions import Actions

class Game:
	def __init__(self, actor):
		self.actor = actor
		self.reset()

	def reset(self):
		self.createSnake()
		self.createApple()
		self.gameover = False
		self.points = 0
		self.direction = Directions.UP
		
	def createSnake(self):
		starting_pos = int(GAME_SIZE / 2)
		self.snake = [(starting_pos, starting_pos), (starting_pos, starting_pos + 1), (starting_pos, starting_pos + 2)]

	def createApple(self):
		possible_apples = []
		
		for x in range(0, GAME_SIZE):
			for y in range(0, GAME_SIZE):
				possible_apples.append((x, y))

		for part in self.snake:
			possible_apples.remove(part)
		
		self.apple = possible_apples[randint(0, len(possible_apples) - 1)]

	def moveSnake(self, action):
		if action != Actions.STAY:
			a = 90 if action == Actions.TURN_RIGHT else -90

			x = int(self.direction[0] * cos(radians(a)) - self.direction[1] * sin(radians(a)))
			y = int(self.direction[0] * sin(radians(a)) + self.direction[1] * cos(radians(a)))

			self.direction = (x, y)

		new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

		self.snake.insert(0, new_head)

		if new_head == self.apple:
			self.createApple()
			self.points = self.points + 1
		else:
			self.snake.pop()

		self.checkCollision()

	def checkCollision(self):
		head = self.snake[0]

		if head[0] < 0 or head[0] > GAME_SIZE - 1 or head[1] < 0 or head[1] > GAME_SIZE - 1:
			self.gameover = True

		for i in range(1, len(self.snake) - 1):
			if head == self.snake[i]:
				self.gameover = True

	def run(self):
		pass

	@staticmethod
	def get_game(gui, actor):
		if gui:
			return GameGUI(actor)
		else:
			return GameConsole(actor)

from .console import GameConsole
from .gui import GameGUI



