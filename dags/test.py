from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'laurent',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
        dag_id="our_first_dag_v3",
        description="our first dag",
        default_args=default_args,
        start_date=datetime(2022, 7, 12, 2),
        schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo Hello world, this is a first task"
    )

    task1