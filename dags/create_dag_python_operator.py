from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'laurent',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(task_instance):
    first_name = task_instance.xcom_pull(task_ids='get-name', key='first_name')
    last_name = task_instance.xcom_pull(task_ids='get-name', key='last_name')
    age = task_instance.xcom_pull(task_ids="get-age", key='age')
    print(f"hello world , my name is {first_name} {last_name}, I am {age}")

def get_name(task_instance):
    task_instance.xcom_push(key='first_name', value='Laurent')
    task_instance.xcom_push(key='last_name', value='Friboulet')

def get_age(task_instance):
    age_value = 44
    task_instance.xcom_push(key='age', value=age_value)

with DAG(
        dag_id="our_python_operator_dag_v6",
        description="our python operator dag",
        default_args=default_args,
        start_date=datetime(2022, 7, 13, 2),
        schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet
    )

    task2 = PythonOperator(
        task_id="get-name",
        python_callable=get_name
    )

    task3 = PythonOperator(
        task_id='get-age',
        python_callable=get_age
    )
    # task1
    [task2, task3] >> task1
