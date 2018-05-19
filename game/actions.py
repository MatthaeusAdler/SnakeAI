class Actions:
	STAY = 0
	TURN_LEFT = 1
	TURN_RIGHT = 2

	@staticmethod
	def get_possible_actions():
		return [Actions.STAY, Actions.TURN_LEFT, Actions.TURN_RIGHT]