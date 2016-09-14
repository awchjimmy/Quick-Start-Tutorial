def main():
	with open('Input.txt') as fin:

		lines = fin.readlines()

		align_style = '{:<15} {:<10} {:<10} {:<10} {:<10}'

		# header
		print(align_style.format('Name,', 'Math,', 'English,', 'Java,', '退學狀態'))

		for line in lines[1:]:
			# split data using tab spaces
			items = line.split('\t')
			# filter empty strings and get rid of \n
			items = [i.strip() for i in items if i != '']

			name = items[0]
			scores = items[1:]

			# convert to Pass/Fail representation
			sscores = []
			failcnt = 0
			for s in scores:
				if int(s) >= 60:
					sscores.append('Pass')
				else:
					sscores.append('Fail')
					failcnt += 1

			# quit schooling
			quit = '退學' if failcnt >= 2 else ''

			print(align_style.format(name, *sscores, quit))

if __name__ == '__main__':
	main()
