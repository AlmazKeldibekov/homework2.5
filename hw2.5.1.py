example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def func(dict,list):
	for i in list:
		try:
			sum_ = 0
			for j in dict[i]:
				try:
					sum_ += j
				except TypeError:
					continue
			print(f'{i}-----------------{sum_}')
		except KeyError:
			print(f'ключа--{i}---не существует')

func(example,elements)