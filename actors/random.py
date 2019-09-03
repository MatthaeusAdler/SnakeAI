from actors import Actor
from game import Actions
from random import randint

class ActorRandom(Actor):
	def is_human(self):
		return False

	def is_ai(self):
		return False

	def get_action(self, game):
		actions = Actions.get_possible_actions()

		return actions[randint(0, len(actions) -1)]

	def want_restart(self):
		if self.retries < self.max_retries:
			self.retries += 1
			return True
		else:
			return False