def parse_data(input_data):
	def parse_line(input_data):
		def parse_signals(signals):
			return signals.strip().split(" ")
		return map(parse_signals, input_data.split(" | "))
	return list(map(parse_line, input_data))

def part1(input_data):
	data = parse_data(input_data)
	print(
		len(
			[
				output
				for _, outputs in data
				for output in outputs
				if len(output) in [2, 3, 4, 7]
			]
		)
	)

def part2(input_data):
	data = parse_data(input_data)

	def get_characters_to_number_from_signals(signals):
		signal_by_number = {}

		for signal in signals:
			if len(signal) == 2:
				signal_by_number[1] = signal
			elif len(signal) == 3:
				signal_by_number[7] = signal
			elif len(signal) == 4:
				signal_by_number[4] = signal
			elif len(signal) == 7:
				signal_by_number[8] = signal


		c_and_f = [char for char in signal_by_number[1]]
		b_c_d_and_f = [char for char in signal_by_number[4]]
		b_and_d = [char for char in b_c_d_and_f if char not in c_and_f]

		def signal_contains(signal, characters):
			for char in characters:
				if char not in signal:
					return False
			return True

		for signal in signals:
			if len(signal) == 6:
				if not signal_contains(signal, c_and_f):
					signal_by_number[6] = signal
				elif signal_contains(signal, b_c_d_and_f):
					signal_by_number[9] = signal
				else:
					signal_by_number[0] = signal

			elif len(signal) == 5:
				if signal_contains(signal, c_and_f):
					signal_by_number[3] = signal
				elif signal_contains(signal, b_and_d):
					signal_by_number[5] = signal
				else:
					signal_by_number[2] = signal

		return {
			signal: number
			for number, signal in signal_by_number.items()
		}

	def get_input_value_from_outputs(outputs, characters_to_number):
		def get_number_from_map(characters_to_number, output):
			for signal, number in characters_to_number.items():
				if sorted(signal) == sorted(output):
					return number
			print(characters_to_number, output)
			raise
		return sum([get_number_from_map(characters_to_number, output) * 10 ** (3 - index) for index, output in enumerate(outputs)])

	def find_out_input_from_data_entry(data_entry):
		unique_signals, outputs = data_entry
		return get_input_value_from_outputs(outputs, get_characters_to_number_from_signals(unique_signals))

	print(sum(map(find_out_input_from_data_entry, data)))
