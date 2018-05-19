import pygame

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
		
		while running:
			action = Actions.STAY

			draw_background(screen)
			
			if self.gameover:
				write_text(screen, "Press 'Return' to restart the Game")
			else:
				pygame.display.set_caption(GAME_TITLE + " - Points: " + str(self.points))
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
						if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) :
							action = self.key_to_action(event.key)
						elif event.key == pygame.K_RETURN and self.gameover:
							self.reset()
			
			if not self.actor.is_human():
				if self.gameover:
					if self.actor.want_restart():
						self.reset()
					else:
						running = False
				else:
					action = self.actor.get_action()

			if running and not self.gameover:
				self.moveSnake(action)

		pygame.quit()

	def key_to_action(self, key):
		if self.direction == Directions.UP:
			if key == pygame.K_LEFT:
				return Actions.TURN_LEFT
			elif key == pygame.K_RIGHT:
				return Actions.TURN_RIGHT
		elif self.direction == Directions.RIGHT:
			if key == pygame.K_UP:
				return Actions.TURN_LEFT
			elif key == pygame.K_DOWN:
				return Actions.TURN_RIGHT
		elif self.direction == Directions.DOWN:
			if key == pygame.K_RIGHT:
				return Actions.TURN_LEFT
			elif key == pygame.K_LEFT:
				return Actions.TURN_RIGHT
		elif self.direction == Directions.LEFT:
			if key == pygame.K_DOWN:
				return Actions.TURN_LEFT
			elif key == pygame.K_UP:
				return Actions.TURN_RIGHT

		return Actions.STAY