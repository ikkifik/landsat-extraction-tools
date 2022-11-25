# Extract (download) Indonesia LANDSAT 8 data

import pandas as pd
import json
import os

gcpdf = pd.read_csv('result_gcp.csv')

search_path = gcpdf['wrs_path'].between(100, 140) # Indonesia WRS-path range
idn_bucket = gcpdf[search_path]
search_row = gcpdf['wrs_row'].between(55, 67) # Indonesia WRS-row range
idn_bucket = idn_bucket[search_row]

idn_bucket.reset_index()
idn_bucket.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
idn_bucket.index = pd.RangeIndex(start=1, stop=len(idn_bucket.index)+1)

idn_bucket_dict = idn_bucket.to_dict('records')

# with open("idn_result.json", "w") as f:
#     json.dump(idn_bucket_dict, f, indent=4)

if not os.path.exists("results/"):
    os.mkdir("results")

for bucket in idn_bucket_dict:
    print("Extracting product_id: {} \n".format(bucket['product_id']))
    os.system("gsutil -m cp -r {} results/".format(bucket['base_url']))
    break