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

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hi, I am a second task"
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo Hi, I am a third task"
    )

# method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
# method 2
    # task1 >> task2
    # task1 >> task3
# method3
    task1 >> [task2, task3]