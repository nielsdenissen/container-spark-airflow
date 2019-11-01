from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dag_id='run_sample_spark',
    default_args=args,
    schedule_interval='0 0 * * *',
    dagrun_timeout=timedelta(minutes=60),
)

run_this = BashOperator(
    task_id='run_sample_spark',
    bash_command='python /tmp/files/sample-spark.py',
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()
