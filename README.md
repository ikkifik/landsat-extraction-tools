# LANDSAT 8 Extraction Tools

This tools using public data from BigQuery Google Cloud Platform (GCP). Make sure your internet connection is stable enough. Don't forget to create a project and generate your own [API Credential Key](https://console.cloud.google.com/apis/credentials) on GCP.

Step:  
1. After creating credential keys from GCP console, save it to `.json` file. 
2. Define the credential keys file name in `getting_landsat.py` at `KEY_PATH` variable. 
3. Run the `getting_landsat.py` to create the landsat dataset.
4. Run the `extract_landsat.py` to download needed landsat collection (default is set to Indonesia area)
