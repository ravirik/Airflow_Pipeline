import faker

import csv

output_file=open('myCSV.CSV',mode='w')

csvwriter=csv.writer(output_file)

header=['name','brand','model','year','price']

csvwriter.writerow(header)

data = [
['scorpio', 'Mahindra', 'Z6', 2022, 1605000],
['XUV500', 'Mahindra', 'W11', 2020, 1747000],
['Safari', 'Tata', 'XT', 2023, 1868400]
]

csvwriter.writerows(data)

output_file.close()
