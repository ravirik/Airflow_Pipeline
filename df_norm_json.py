import pandas.io.json as pd_json


f=open('Data.json','r')
data =pd_json.loads(f.read())

df=pd_json.json_normalize(data,record_path='records')

print(df.head(2).to_json(orient='records'))
