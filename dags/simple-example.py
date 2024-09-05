from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a simple function to print "Hello, Airflow!"
def print_hello():
    print("Hello, Airflow!")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),  # set a start date for the DAG
    'retries': 1,  # number of retries in case of failure
}

# Instantiate the DAG
with DAG(
        'hello_airflow',  # Name of the DAG
        default_args=default_args,
        schedule_interval='@daily',  # Run this DAG once a day
        catchup=False,  # Don't run for previous dates if start_date is in the past
) as dag:

    # Define a task using PythonOperator
    hello_task = PythonOperator(
        task_id='print_hello',  # Unique ID for the task
        python_callable=print_hello,  # The function to be called by this task
    )

# The DAG will automatically include all tasks defined within the "with" block.