import datetime as dt
from datetime import timedelta

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

def CSVtoJSON():
    df = pd.read_csv('/home/ricky/project/Airflow_Pipeline/Data.CSV')
    for i, r in df.iterrows():
        print(r['model'])
    df.to_json('/home/ricky/project/Airflow_Pipeline/CtoJ_Airflow.json', orient='records')

default_args = {
	'owner': 'RaviChoudhary',
	'start_date': dt.datetime(2023, 9, 10),
	'end_date': datetime(2023, 9, 12)
	'retries': 1,
	'retry_delay': dt.timedelta(minutes=5),
}

with DAG('CTOJDAG', default_args=default_args, schedule_interval=timedelta(minutes=5), ) as dag: # we can also use cron schedule_interval = '0 * * * *',
	
	print_starting = BashOperator(task_id = 'starting', bash_command ='echo " Reading the CSV now.."')
	
	CSV_JSON = PythonOperator(task_id = 'convertCSVtoJSON', python_callable=CSVtoJSON)
	
	print_starting.set_downstream(CSV_JSON) # can also use print_starting >> CSVJson
	
	CSV_JSON.set_upstream(print_starting) # can also use CSVJson << print_starting
	
	
	