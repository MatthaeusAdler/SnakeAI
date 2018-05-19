class Actor:
	def __init__(self, max_retries):
		self.retries = 0
		self.max_retries = max_retries

	def is_human(self):
		pass

	def get_action(self):
		pass
	
	def want_restart(self):
		pass


	@staticmethod
	def get_actor(name, retries):
		if name == "human":
			return ActorHuman(retries)
		elif name == "random":
			return ActorRandom(retries)
		else:
			print("NO VALID ACTOR")

from .human import ActorHuman
from .random import ActorRandom