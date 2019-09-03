import pygame
from random import randint
import numpy as np

from game import Game
from settings import *
from .drawing import draw_background, draw_snake, draw_apple, write_text
from .directions import Directions
from .actions import Actions

class GameGUI(Game):
	def run(self):
		pygame.init()
		screen = pygame.display.set_mode(PLAYGROUND)
		clock = pygame.time.Clock()
		running = True
		self.actor.initialize_game(self)
		while running:

			action = Actions.STAY
			draw_background(screen)			
			if self.gameover:
				write_text(screen, "Press 'Return' to restart the Game")
			else:
				pygame.display.set_caption(GAME_TITLE + " - Points: " + str(self.points) + " - Record: " + str(self.record))
				draw_background(screen)
				draw_snake(screen, self.snake)
				draw_apple(screen, self.apple)
			
			pygame.display.update()

			clock.tick(FPS)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
						break
					elif self.actor.is_human:
						if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d) :
							action = self.key_to_action(event.key)
						elif event.key == pygame.K_RETURN and self.gameover:
							self.reset()
			
			if not self.actor.is_human():
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



				

	def key_to_action(self, key):
		if self.direction == Directions.UP:
			if key == pygame.K_LEFT or key == pygame.K_a:
				return Actions.TURN_LEFT
			elif key == pygame.K_RIGHT or key == pygame.K_d:
				return Actions.TURN_RIGHT
		elif self.direction == Directions.RIGHT:
			if key == pygame.K_UP or key == pygame.K_w:
				return Actions.TURN_LEFT
			elif key == pygame.K_DOWN or key == pygame.K_s:
				return Actions.TURN_RIGHT
		elif self.direction == Directions.DOWN:
			if key == pygame.K_RIGHT or key == pygame.K_d:
				return Actions.TURN_LEFT
			elif key == pygame.K_LEFT or key == pygame.K_a:
				return Actions.TURN_RIGHT
		elif self.direction == Directions.LEFT:
			if key == pygame.K_DOWN or key == pygame.K_s:
				return Actions.TURN_LEFT
			elif key == pygame.K_UP or key == pygame.K_w:
				return Actions.TURN_RIGHT

		return Actions.STAY

