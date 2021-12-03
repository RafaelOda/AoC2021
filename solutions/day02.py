def part1(input_data):
	horizontal = 0
	depth = 0
	for line in input_data:
		command, number = line.split()
		number = int(number)

		if command == "forward":
			horizontal = horizontal + number
		elif command == "down":
			depth = depth + number
		elif command == "up":
			depth = depth - number
		else:
			raise ValueError("expected forward, down and up only")

	print(horizontal * depth)

def part2(input_data):
	horizontal = 0
	depth = 0
	aim = 0

	for line in input_data:
		command, number = line.split()
		number = int(number)

		if command == "forward":
			horizontal = horizontal + number
			depth = depth + aim * number
		elif command == "down":
			aim = aim + number
		elif command == "up":
			aim = aim - number
		else:
			raise ValueError("expected forward, down and up only")

	print(horizontal * depth)
