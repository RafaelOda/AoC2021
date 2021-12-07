def parse_data(data):
	return sorted(list(map(int, data[0].split(","))), reverse=True)

def count_lanternfish_by_value(lanternfishes):
	lanternfish_count_by_value = {}

	for lanternfish in lanternfishes:
		if lanternfish not in lanternfish_count_by_value:
			lanternfish_count_by_value[lanternfish] = 0
		lanternfish_count_by_value[lanternfish] += 1

	return lanternfish_count_by_value

def process_lanterfishes_after_one_day(lanternfishes):
	lanternfish_count_by_value = count_lanternfish_by_value(lanternfishes)

	def build_new_lanternfish_state(lanternfish_count_by_value):
		new_lanternfish_state = []
		for value, count in lanternfish_count_by_value.items():
			if value > 0:
				new_lanternfish_state += [value - 1] * count
			else:
				new_lanternfish_state += [6] * count + [8] * count

		return new_lanternfish_state

	return build_new_lanternfish_state(lanternfish_count_by_value)


def simulate_period_for_lanternfishes(initial_lanternfishes, days, current_day=0):
	print(current_day)
	if days == current_day:
		return initial_lanternfishes
	current_day += 1
	return simulate_period_for_lanternfishes(
		process_lanterfishes_after_one_day(initial_lanternfishes), 
		days, 
		current_day=current_day
	)

def optimized_count_of_lanternfishes(initial_lanternfishes, total_days):
	
	initial_number = len(initial_lanternfishes)

	lanternfish_count_by_value = count_lanternfish_by_value(initial_lanternfishes)	

	count_per_day = {
		0: initial_number,
		1: initial_number,
	}

	for day in range(2, 9):
		count_per_day[day] = count_per_day[day - 1] + lanternfish_count_by_value.get(day - 1, 0)

	count_per_day[9] = count_per_day[8] + lanternfish_count_by_value[1]
	count_per_day[10] = count_per_day[9] + lanternfish_count_by_value[2]

	def get_count_for_day(count_per_day, day):
		return (
			count_per_day[day - 1] + 
			count_per_day[day - 7] -
			count_per_day[day - 8] +
			count_per_day[day - 9] -
			count_per_day[day - 10]
		)

	if total_days in count_per_day:
		return count_per_day[total_days]

	for day in range(total_days):
		if day in count_per_day:
			continue
		count_per_day[day] = get_count_for_day(count_per_day, day)
	
	return get_count_for_day(count_per_day, total_days)

def part1(input_data):
	days_until_end = 80
	initial_lanternfishes = parse_data(input_data)
	print(len(simulate_period_for_lanternfishes(initial_lanternfishes, days_until_end)))

def part2(input_data):
	days_until_end = 256
	initial_lanternfishes = parse_data(input_data)
	print(optimized_count_of_lanternfishes(initial_lanternfishes, days_until_end))
