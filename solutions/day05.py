def parse_input(input_data):
	def parse_line(input_line):
		def parse_coordinate(coordinate):
			return list(map(int, coordinate.split(",")))

		coordinate_pairs = input_line.split(" -> ")
		return list(map(parse_coordinate, coordinate_pairs))
	return list(map(parse_line, input_data))

def get_map(size):
	return [
		[0] * size
		for _ in range(size)
	]
	

def get_number_of_intersections(vents_map):
	number_of_intersections = 0

	for line in vents_map:
		for point in line:
			if point >= 2:
				number_of_intersections += 1

	return number_of_intersections


def part1(input_data):
	vents = parse_input(input_data)
	vents_map = get_map(1001)
	for vent in vents:
		start_coordinate = vent[0]
		end_coordinate = vent[1]
		if start_coordinate[1] == end_coordinate[1]:
			y = start_coordinate[1]
			smaller_x, bigger_x = sorted([start_coordinate[0], end_coordinate[0]])
			for x in range(smaller_x, bigger_x + 1):
				vents_map[x][y] += 1
		elif start_coordinate[0] == end_coordinate[0]:
			x = start_coordinate[0]
			smaller_y, bigger_y = sorted([start_coordinate[1], end_coordinate[1]])
			for y in range(smaller_y, bigger_y + 1):
				vents_map[x][y] += 1
		else:
			continue

	number_of_intersections = get_number_of_intersections(vents_map)
	print(number_of_intersections)


def part2(input_data):
	vents = parse_input(input_data)
	vents_map = get_map(1001)
	for vent in vents:
		start_coordinate = vent[0]
		end_coordinate = vent[1]
		if start_coordinate[1] == end_coordinate[1]:
			y = start_coordinate[1]
			smaller_x, bigger_x = sorted([start_coordinate[0], end_coordinate[0]])
			for x in range(smaller_x, bigger_x + 1):
				vents_map[x][y] += 1
		elif start_coordinate[0] == end_coordinate[0]:
			x = start_coordinate[0]
			smaller_y, bigger_y = sorted([start_coordinate[1], end_coordinate[1]])
			for y in range(smaller_y, bigger_y + 1):
				vents_map[x][y] += 1
		else:
			start_x, start_y = start_coordinate
			end_x, end_y = end_coordinate
			step_x = 1 if end_x >= start_x else -1
			step_y = 1 if end_y >= start_y else -1
			for x, y in zip(range(start_x, end_x + step_x, step_x), range(start_y, end_y + step_y, step_y)):
				vents_map[x][y] += 1

	number_of_intersections = get_number_of_intersections(vents_map)
	print(number_of_intersections)
