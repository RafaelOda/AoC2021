import statistics
import math

def parse_data(input_data):
	return list(map(int, input_data[0].split(",")))

def difference(position, reference):
	return abs(position - reference)

def part1(input_data):
	data = parse_data(input_data)
	least_fuel_position = statistics.median(data)
	total_fuel = sum([difference(position, least_fuel_position) for position in data])
	print(total_fuel)


def part2(input_data):
	data = parse_data(input_data)
	average = statistics.mean(data)
	candidate_floor = math.floor(average)
	candidate_ceiling = math.ceil(average)

	def print_total_fuel(reference):
		print(sum([difference(position, reference) * (difference(position, reference) + 1) for position in input_data]) / 2)

	print_total_fuel(candidate_floor)
	print_total_fuel(candidate_ceiling)
