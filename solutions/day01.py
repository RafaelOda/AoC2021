def part1(input_data):
	n = 0
	last_depth = input_data[0]
	for depth in input_data[1:]:
		if depth > last_depth:
			n = n + 1
		last_depth = depth
	print(n)


def part2(input_data):
	n = 0
	for i in range(len(input_data) - 3):
		if input_data[i + 3] > input_data[i]:
			n = n + 1
	print(n)
