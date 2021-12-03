import argparse
import importlib


def main(day, part):
	solution = importlib.import_module("day%02d" % day)

	with open("inputs/day%02d.txt" % day, "r") as f:
		input_data = [int(l) for l in f]
	
	if part == 1:
		return solution.part1(input_data)
	elif part == 2:
		return solution.part2(input_data)
	else:
		raise ValueError("Expected part to be either 1 or 2")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--day", type=int)
	parser.add_argument("--part", type=int)
	args = parser.parse_args()
	main(args.day, args.part)
