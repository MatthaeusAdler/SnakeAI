class Actor:
	def __init__(self, max_retries):
		self.retries = 0
		self.max_retries = max_retries

	def is_human(self):
		pass

	def is_ai(self):
		pass
		
	def get_action(self, game):
		pass
	
	def want_restart(self):
		pass


	@staticmethod
	def get_actor(name, retries, learn):
		if name == "human":
			return ActorHuman(retries)
		elif name == "random":
			return ActorRandom(retries)
		elif name == "ai":
			return ActorAi(retries, learn)
		else:
			print("NO VALID ACTOR")

from .human import ActorHuman
from .random import ActorRandom
from .ai import ActorAi