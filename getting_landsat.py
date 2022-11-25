# Download Landsat 8 dataset from GCP Bigquery

from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import tqdm
import time

key_path = "fik-labs-2a7dd813e40a.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

# Perform a query.
QUERY = ("""SELECT scene_id, product_id, spacecraft_id, sensor_id, date_acquired, 
         sensing_time, collection_number, collection_category, data_type, wrs_path, wrs_row, 
         cloud_cover, north_lat, south_lat, west_lon, east_lon, total_size, base_url, source_url, etl_timestamp 
         FROM bigquery-public-data.cloud_storage_geo_index.landsat_index 
         WHERE spacecraft_id='LANDSAT_8' ORDER BY etl_timestamp DESC""")
query_job = client.query(QUERY)  # API request

collect_row = []

try:
    count=0
    for row in query_job:
        print(count)
        collect_row.append(dict(row.items()))
        count+=1
except:
    pass

df = pd.json_normalize(collect_row)
df.to_csv("result_gcp.csv")
