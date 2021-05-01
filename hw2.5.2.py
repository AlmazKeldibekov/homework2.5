import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
	'fhjhafhdfa.txt']
file = open (f'{names[random.randint(0,10)]}', 'w')

def func1(name1):
	for i in name1:
		try:
			with open(f'{i}', 'r+') as f:
				f.write('Almaz')
		except FileNotFoundError:
			print(f'Такого файла {i} не существует')
func1(names)
