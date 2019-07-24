# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 5
	board = []

	def __init__(self):
		for i in range(self.size):
			moves = 9999
			name = 'player'
			score = Score(name, moves)
			self.board.append(score)
			self.board.sort(key=lambda x: x.get_score())

	def print_board(self):
		#for escaped in board:	#change
		for i in range(self.size):
			print(str(i+1)+".)", self.board[i].get_name(), str(self.board[i].get_score()), "moves")

	def update(self,score):
		new_score = score.get_score()
		for i in range(self.size):
			if (new_score < self.board[i].get_score()):
				return True

	def insert(self, score):
		for i in range(self.size):
			if score.get_score() < self.board[i].get_score():
				self.board.insert(i, score)
				return

# test = Leaderboard()
# play = Score('test', 1)
# test.print_board()
# if test.update(play):
# 	test.insert(play)
# test.print_board()

## test = Leaderboard()

			# player = escaped.get_name()
			# score = escaped.get_score()
			# print(player, ":", score)
	#
	# def updated(self, score):
	# 	#if score>
	# 	i = 0
	# 	for currentScore in self.print_board: ## change
	# 		if (score.get_score()<=currentScore.get_score()):
	# 			if i == self.size-1:
	# 				return()
	# 			else:
	# 				temporary = self.board[i:self.size-1]
	# 				self.board[i] = scores
	# 				self.board[i+1:self.score] = temporary
	# 				break
	# 		i +=1
	# 	return Leaderboard()
