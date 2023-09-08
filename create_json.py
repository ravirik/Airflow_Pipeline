import json
from faker import Faker

fake=Faker('en_IN')

output_file=open('Data.json',mode='w')

all_data={}
all_data['records']=[]

for row in range(1000):
	data={'Name':fake.name(),'Street':fake.street_address(),'City':fake.city(),'State':fake.state(),'Phone':fake.random_int(min=6789787908,max=9867674278,step=1)}
	all_data['records'].append(data)

json.dump(all_data,output_file)
