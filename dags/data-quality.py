from airflow import DAG
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),  # Update the start date as needed
    'retries': 1,  # Number of retries in case of task failure
}

base_path = Path(__file__).parents[2]
data_dir = base_path / "include" / "data"
data_file = data_dir / "yellow_tripdata_sample_2019-01.csv"

ge_root_dir = str(base_path / "include" / "great_expectations")


# Instantiate the DAG
with DAG(
        dag_id='great_expectations_example',  # Name of the DAG
        default_args=default_args,
        schedule_interval='@daily',  # Schedule to run daily
        catchup=False,  # Prevent running for past dates if start_date is in the past
) as dag:

    # Define a task using GreatExpectationsOperator to run a validation checkpoint
    ge_checkpoint_task = GreatExpectationsOperator(
        task_id='ge_checkpoint_validation',  # Unique ID for the task
        checkpoint_name='my_checkpoint',  # Name of your Great Expectations checkpoint
        data_context_root_dir='/path/to/great_expectations',  # Path to your Great Expectations project
        fail_task_on_validation_failure=True,  # Fail the task if validation fails
        validation_operator_name='action_list_operator'  # Name of the validation operator in your GE config
    )

    # Add additional tasks or dependencies here if needed

# The DAG is automatically picked up by Airflow as it is defined within the "with" block.