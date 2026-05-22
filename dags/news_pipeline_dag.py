import sys
import os
sys.path.insert(0, '/Users/arjun/Documents/dev/DataPipelineProject')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from etl.extract import fetch_news
from etl.transform import transform
from etl.load import load

def extract_task(**kwargs):
    print("Starting extract task")
    ti = kwargs['ti']
    print("Fetching news...")
    raw_json = fetch_news('technology')
    print(f"Got {len(raw_json['articles'])} articles")
    ti.xcom_push(key='raw_json', value=raw_json['articles'])
    print("XCom push complete")

def transform_load_task(**kwargs):
    ti = kwargs['ti']
    articles = ti.xcom_pull(task_ids='extract', key='raw_json')
    raw_json = {'articles': articles}
    transformed_data = transform(raw_json)
    load(transformed_data)

default_args = {
    'owner': 'arjun',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='news_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 5, 22),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_task
    )
    transform_and_load = PythonOperator(
        task_id='transform',
        python_callable=transform_load_task
    )
    extract >> transform_and_load