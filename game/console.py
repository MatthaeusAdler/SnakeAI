import pygame
from random import randint
import numpy as np

from game import Game
from settings import *
from .drawing import draw_background, draw_snake, draw_apple, write_text
from .directions import Directions
from .actions import Actions

class GameConsole(Game):
	def run(self):
		running = True
		self.actor.initialize_game(self)
		while running:
			action = Actions.STAY
			action = self.actor.get_action(self)
			if self.gameover:
				if self.points>self.record:
					self.record=self.points
				print("Score: "+str(self.points))
				self.sum+=self.points
				if self.actor.want_restart():
					self.reset()						
					if self.actor.is_ai():
						self.actor.replay_new(self.actor.memory)
						self.actor.initialize_game(self)
				else:
					print("Record: "+str(self.record))
					print("Average: "+str(self.sum/self.actor.max_retries))
					running = False

			if running and not self.gameover:
				self.moveSnake(action)

		pygame.quit()



				

