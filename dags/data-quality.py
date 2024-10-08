from airflow import DAG
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from datetime import datetime
from pathlib import Path
from airflow.models.baseoperator import chain
import logging

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),  # Update the start date as needed
    'retries': 1,  # Number of retries in case of task failure
}

base_path = Path(__file__).parents[1]
data_dir = base_path / "data" / "data-quality"

ge_root_dir = str(data_dir)

logging.info(ge_root_dir)
with DAG(
        dag_id="example_great_expectations_dag",
        start_date=datetime(2021, 12, 15),
        catchup=False,
        schedule_interval='@hourly',
) as dag:
    ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
        task_id="ge_data_context_root_dir_with_checkpoint_name_pass",
        data_context_root_dir=ge_root_dir,
        checkpoint_name="trino_pegel_checkpoint",
        return_json_dict = True,
    )


chain(
    ge_data_context_root_dir_with_checkpoint_name_pass,
)