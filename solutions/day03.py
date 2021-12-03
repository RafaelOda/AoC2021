def get_most_common_algarism(input_data, position):
	total_numbers = len(input_data)
	algarism_sum = sum([int(number[position]) for number in input_data])
	if algarism_sum >= total_numbers / 2:
		return 1
	return 0


def part1(input_data):
	number_size = len(input_data[0])

	gamma_rate = 0
	for i in range(number_size):
		if get_most_common_algarism(input_data, i) == 1:
			gamma_rate = gamma_rate + 2 ** (number_size - i - 1)

	epsilon_rate = 2 ** number_size - gamma_rate - 1
	print(epsilon_rate * gamma_rate)


def part2(input_data):

	def convert_from_binary(number_string):
		number_size = len(number_string)

		converted = 0
		for i in range(number_size):
			if int(number_string[i]) == 1:
				converted = converted + 2 ** (number_size - i - 1)
		return converted

	def calculate_ratings(input_data, position=0, most_common_mode=True):
		if len(input_data) == 1:
			return convert_from_binary(input_data[0])

		most_common = get_most_common_algarism(input_data, position)

		filtered_input_data = [
			number
			for number in input_data
			if bool(int(number[position]) == most_common) == most_common_mode
		]

		return calculate_ratings(filtered_input_data, position + 1, most_common_mode)

	print(calculate_ratings(input_data, most_common_mode=True) * calculate_ratings(input_data, most_common_mode=False))