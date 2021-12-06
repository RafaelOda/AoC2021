def is_bingo(marking_board):
	size = len(marking_board[0])
	for line in marking_board:
		if all(line): 
			return True
	for i in range(size):
		if all([line[i] for line in marking_board]):
			return True
	return False

def get_board_sum(board, markings):
	result = 0
	for board_line, markings_line in zip(board, markings):
		for board_number, marking in zip(board_line, markings_line):
			if not marking:
				result = result + board_number

	return result

class BingoSimulator:
	def __init__(self, input_data):
		numbers, boards = self._parse_data(input_data)
		self.numbers = numbers
		self.boards = boards
		self.board_size = len(boards[0])

		def build_empty_marking_boards(size):
			def build_empty_markings_line(size):
				return [0] * size
			return [
				build_empty_markings_line(size)
				for i in range(size)
			]

		self.marking_boards = [
			build_empty_marking_boards(self.board_size)
			for i in range(len(self.boards))
		]

	def _parse_data(self, input_data):
		numbers = list(map(int, input_data[0].split(",")))

		boards = []
		current_board = []

		for line in input_data[2:]:
			line = line.strip()
			if not line:
				if current_board:
					boards.append(current_board)
				current_board = []
				continue

			current_board.append(list(map(int, line.split())))

		return numbers, boards

	def mark_number(self, number):
		for index, board in enumerate(self.boards):
			for line_index, line in enumerate(board):
				for column_index, line_number in enumerate(line):
					if line_number == number:
						self.marking_boards[index][line_index][column_index] = 1

	def solve(self):
		winner_boards_sum_by_index = {}
		winning_number = None

		for number in self.numbers:
			self.mark_number(number)
			for board_number, board in enumerate(self.boards):
				marking_board = self.marking_boards[board_number]
				if is_bingo(marking_board):
					winner_boards_sum_by_index[board_number] = get_board_sum(board, marking_board)		
			if winner_boards_sum_by_index:
				winning_number = number
				break

		return winning_number, winner_boards_sum_by_index

	def find_loser(self):
		for number in self.numbers:
			self.mark_number(number)

			winning_boards_this_round = []
			is_only_one_remaining = len(self.boards) == 1

			for board_number, board in enumerate(self.boards):
				marking_board = self.marking_boards[board_number]
				if is_bingo(marking_board):
					if is_only_one_remaining:
						return number * get_board_sum(board, marking_board)
					winning_boards_this_round.append(board_number)
			for board_number in sorted(winning_boards_this_round, reverse=True):
				del self.boards[board_number]
				del self.marking_boards[board_number]


def part1(input_data):
	bingo_simulator = BingoSimulator(input_data)
	winning_number, winner_boards_sum_by_index = bingo_simulator.solve()
	for winner_board_index, winner_board_sum in winner_boards_sum_by_index.items():
		print(winner_board_index, winning_number * winner_board_sum)


def part2(input_data):
	bingo_simulator = BingoSimulator(input_data)
	print(bingo_simulator.find_loser())
