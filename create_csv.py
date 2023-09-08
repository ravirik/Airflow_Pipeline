import csv
from faker import Faker

from faker_vehicle import VehicleProvider

fake=Faker('en_IN')
fake.add_provider(VehicleProvider)

output=open('Data.CSV',mode='w')
header=['model','brand','Category','year','price']

my_writer=csv.writer(output)
my_writer.writerow(header)

for i in range(1000):
	my_writer.writerow([fake.vehicle_model(), fake.vehicle_make(), fake.vehicle_category(), fake.vehicle_year(), fake.random_int(min=600000,max=15000000, step=1)])
	
output.close()

