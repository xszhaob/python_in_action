import csv

with open('files/test.csv', 'w+') as file_obj:

	writer = csv.writer(file_obj)
	writer.writerow(('number', 'number plus 2', 'number times 2'))
	for i in range(10):
		writer.writerow((i, i + 2, i ** 2))