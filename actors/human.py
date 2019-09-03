from actors import Actor

class ActorHuman(Actor):
	def is_human(self):
		return True

	def is_ai(self):
		return False