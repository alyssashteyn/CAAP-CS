# This is the engine of the game, basically runs everything

class Engine(object):

	# global variables to keep track of game status and live count

	escaped = False
	#lives = 3
	print("Wlcome! Select a difficulty level\nEnter 1 for 'easy', 2 for 'medium', and 3 for 'hard'.")
	difficulty = int(input("difficulty level: "))
	lives = 4 - difficulty
	print("You will have", lives, "lives.")

	#difficulty = input("Select a difficulty. Ener 1 for easy, 2 for medium, or 3 for hard! > ")
	# if difficulty == 1:
	# 	lives = 5
	# 	print("You have 5 lives.")
	# elif difficulty == 2:
	# 	lives = 3
	# 	print("You have 3 lives.")
	# elif difficulty == 3:
	# 	lives = 1
	# 	print("You have 1 life")

	# initializes the map in the game
	def __init__(self, scene_map):
		self.scene_map = scene_map
	# takes current scene, plays it, gets the next scene, and updates the game
	# should also return the number of moves the game takes in total
	def play(self): #gameflow
		current_scene = self.scene_map.opening_scene()
		next_scene_name = ''
		checkpoint = current_scene
		n_moves = 0
		while (next_scene_name != 'escaped' and self.lives > 0): #print ("You failed. You now have", n_moves, "more tries.")
			next_scene_name = current_scene.enter() #function in scenes file
			if (next_scene_name == 'quit'):
				exit(1)
			elif (next_scene_name == 'death'):
				checkpoint = current_scene
				n_moves += 1
				print("score = ", n_moves)
				current_scene = self.scene_map.next_scene(next_scene_name)
			elif (next_scene_name == 'died'):
				self.lives -=1
				current_scene = checkpoint
				#n_moves +=1
				#print("You now have", self.lives, "lives") #replace n_moves with moves
				#print("moves = ", n_moves)
			else:
				current_scene = self.scene_map.next_scene(next_scene_name)
				n_moves += 1
				print("score = ", n_moves)

		# if (current_scene == escaped): #if (current_scene == 'escaped'):
		# 	self.escaped = True
		# 	return n_moves##??

		if (next_scene_name == 'escaped'):
			self.escaped = True
			print("Enter 1 to see if you made it to the leaderboard!")
		return n_moves


	# updates the variable to determine whether player won or failed.
	def won(self):
		return self.escaped
