import sys
import argparse

from actors import Actor, ActorHuman
from game import Game

def main():
	args = setup_arguments()
	
	actor = Actor.get_actor(args.a, args.r, args.l)
	gui = True if type(actor) is ActorHuman else args.g

	game = Game.get_game(gui, actor)
	game.run()

	quit()

def setup_arguments():
	parser = argparse.ArgumentParser(description="Snake AI - this is how to use it")
	parser.add_argument("-g", help="Start with gui", action="store_true")
	parser.add_argument('-r', help='Retries - only usefull if not human', type=int, default=0)
	parser.add_argument('-l', help='Learn - only usefull if ai', action="store_true")

	required = parser.add_argument_group('required arguments')
	required.add_argument('-a', help='Actor - human, random or ai', required=True)
	
	return parser.parse_args()

if __name__ == "__main__":
    main()