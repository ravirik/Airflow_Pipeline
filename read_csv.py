import csv

with open('Data.CSV') as f:
	my_reader=csv.DictReader(f)
	headers=next(my_reader)
	for row in my_reader:
		print(row['model'])
