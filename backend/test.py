from google.cloud import bigquery
from google.api_core.exceptions import Forbidden

project_id = "generativeai-coe"

try:
    client = bigquery.Client(project=project_id)
    datasets = list(client.list_datasets())
    
    if datasets:
        print(f"✅ You have access! Datasets in {project_id}:")
        for dataset in datasets:
            print(f" - {dataset.dataset_id}")
    else:
        print(f"ℹ️ You have access to project {project_id}, but no datasets found.")

except Forbidden as e:
    print(f"❌ Access denied: {e}")