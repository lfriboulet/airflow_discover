from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

#
#  https://crontab.guru/
#
default_args = {
    'owner': 'laurent',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        dag_id='dag_with_cron_expression_v3',
        default_args=default_args,
        start_date=datetime(2022, 7, 21),
        schedule_interval='0 3 * * Tue',
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo dag with cron expression!'
    )

    task1