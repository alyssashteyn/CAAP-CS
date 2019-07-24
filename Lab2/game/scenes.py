# imports random madule form library
from random import randint
from death import Death

# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class Doorway(Scene):

	name ='doorway_scene'

	def enter(self):
		print ("This is the day. You're in the Doorway with your Russian princess, her mom opens the door.\n You're nervous but at least you brought something with you. ")
		print ("What do you bring to dinner?")#raise ValueError ('todo')
		return self.action()

	def action(self):
		print ("Select an option by typing 1,2, or 3.")
		print("1. wine")
		print("2. chips and quac")
		print("3. board game")

		choice = input(">")
		if choice == 'quit':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except (1,2,3):
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Congrats! You've pleased her mother with the nectar of the pagan gods!")
			#moves+=1
			return self.exit_scene('foyer') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Soviets don't eat 'guacamole'... they've probably never seen an avocado before in their lives.")
			#moves +=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Sorry, the Soviets aren't into your nerdy board games?\n Save them house study breaks, not for meeting her parents.")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type 'quit' to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Foyer(Scene):
	name = 'foyer_scene'

	def enter(self):
		print ("You've passed the gift test, you walk past the physical barrier of the Doorway and the psychological barrier of your first interaction with her intimidating mother (who's making no effort to make you feel worthy).\n At least you've made it this far. You enter the house into the foyer.\n Her grandfathers are standing there chatting with their coats and ushankas still in hand.")
		print ("How do you greet them?")
		return self.action() ## TODO:

	def action(self):
		print ("1. Hug them both and adress them as 'Dedushka'")
		print ("2. Tickle them")
		print ("3. Shake their hands firmly")
		#raise ValueError ('todo')
		choice = input(">")
		if choice == 'quit':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except (1, 2, 3):
		 print("That's not an int!")
		 return self.exit_scene(self.name)
		if int(choice) == 3:
			 print ("Good choice.")
			 #moves+=1
			 return self.exit_scene('dinner') # raise ValueError ('todo')
		elif int(choice) == 1:
			 print ("Soviets don't like physical affection. Nor do they appreciate their titles mispronounced.")
			 #moves+=1
			 return self.exit_scene('death')# raise ValueError ('todo')
		elif int(choice) == 2:
			 pass
			 print ("It's probably a good time to reinstall Tinder on your phone.")
			 #moves +=1
			 return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type 'quit' to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome

class Dinner(Scene):

	name ='dinner_scene'

	def enter(self):
		#raise ValueError ('todo')
		print ("Cool, now you've introducted yourself to her family. You've survived so far, but how will you fare in smalltalk? ")
		print ("You sit down for dinner. There's beet salad on the table and a variety of other concoctions you've never known or desired to eat.\n Her mom asks what you do for a living. Wyd?")
		return self.action() #outcome: ## TODO:

	def action(self):
		#raise ValueError ('todo')
		print("So, what do you do for a living")
		print("1. Emergency Cardiothorasic Surgeon")
		print("2. Software Developer")
		print("3. Stand up comedian")

		choice = input(">")
		if choice == 'quit':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
			try:
			 choice = int(choice)
			except (1, 2, 3):
				print("That's not an int!")
			return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Is the 500k a year worth it if you're always on call? Not to my mother.")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Good choice.")
			#moves +=1
			return self.exit_scene('jewish') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Maybe you can find someone else to 'woo' with your 'jokes'")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type 'quit' to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Jewish(Scene):

	name ='jewish_scene'

	def enter(self):
		print ("Her mom asks about your religious beliefs at dinner. There is truly no holding back with this woman.")
		print ("Are you willing to convert to Judaism?")#raise ValueError ('todo')
		return self.action()

	def action(self):
		print ("Select an option by typing 1,2, or 3.")
		print("1. Yes")
		print("2. No")
		print("3. I am Jewish.")

		choice = input(">")
		if choice == 'quit':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except (1,2,3):
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("It's nice that you're willing but you wouldn't be ethnically Jewish. Soz.")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Yikes! Time to dust off your Torah.")
			#moves +=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("L'chaim!")
			#moves+=1
			return self.exit_scene('kids') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type 'quit' to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome

class Kids(Scene):

	name ='kids_scene'

	def enter(self):
		print ("Literally no one: n\ Her mother: So, do you want kids?")
		return self.action()

	def action(self):
		print ("Select an option by typing 1,2, or 3.")
		print("1. Yes, 18 of them")
		print("2. Do dogs count?")
		print("3. Yes, probably like 2 or three.")

		choice = input(">")
		if choice == 'quit':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except (1,2,3):
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Me too. But my mom is more interested in financial stability.")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Did you know that genetics play a factor into whether or not you'll own a dog as an adult?")
			#moves +=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Nice.")
			#moves+=1
			return self.exit_scene('leaving') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type 'quit' to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome

class Leaving():
	name = 'leaving_scene'
	def enter(self):
		#raise ValueError ('todo')
		print ("Dinner's over. You've been guilted into eating too much.\n Now the women of the table are clearing plates and preparing for dessert and chai. ")
		print ("What do you do in the meanwhile?")
		return self.action() #outcome: ## TODO:

	def action(self):
		#raise ValueError ('todo')
		print("1. Help clear the table")
		print("2. Chat with grandfathers")
		print("3. Wash dishes in the kitchen as the women bring in table contents.")

		choice = input(">")
		if choice == 'quit':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
			choice = int(choice)
		except (1, 2, 3):
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Nice try, but that's not the manly choice. And Russains care about that a lot. Just look at their fearless leader, Putin.")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Nice, I hope you're well versed in Russian politics.")
			print ("Congrats! You won this trivial game!")
			#moves +=1
			return self.exit_scene('escaped') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("You can roll up your sleeves, but no one will be impressed, you might as well hang out with my grandpas.")
			#moves+=1
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type 'quit' to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
			return outcome

class Escaped(Scene):
	name = 'escaped_scene'
	def enter(self):
		print ("Congratulations")
		exit(1)
		return self.action()
	def action(self):
		print("congrats")
		# choice = input(">")
		# if choice == 'quit':
		return self.exit_scene(choice)
	def exit_scene(self, outcome):
		return outcome
