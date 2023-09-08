import json

with open('Data.json',mode='r') as f:
	data=json.load(f)
	print(data['records'][0])
	print(data['records'][500]['City'])
	print(data['records'][990]['Name'])

