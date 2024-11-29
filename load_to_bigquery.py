
# Import des packages
import datetime
import logging
import os
import pandas as pd
from sqlalchemy import create_engine
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd

# Chargement des données dans Big Query

def load_csv_to_bigquery(bucket_name,source_blob_name,destination_table,path_to_private_key):
        """
        Charge les données d'un fichier CSV depuis Google Cloud Storage vers une table BigQuery.

        Arguments :
        
        bucket_name : Le nom du bucket Google Cloud Storage contenant le fichier.
        source_blob_name : Le nom du blob (fichier) dans le bucket.
        destination_table : Le nom qualifié complet de la table BigQuery dans laquelle charger les données.
        path_to_private_key: La clé de connexion au compte de service GCP
        
        """
        

        try:
            client = bigquery.Client().from_service_account_json(json_credentials_path=path_to_private_key)
            job_config = bigquery.LoadJobConfig(
                  source_format=bigquery.SourceFormat.CSV,
                  skip_leading_rows=1,  
                  autodetect=True  
            )

            uri = f"gs://{bucket_name}/{source_blob_name}"

            load_job = client.load_table_from_uri(
                  uri, destination_table, job_config=job_config
              )

            load_job.result()  
            
            print("Chargé avec Succès !")
            
        except Exception as e:
            print(f"Erreur lors de l'extraction ou du chargement : {e}")



""""
# Chargement de la base de données dans Big Query
bucket_name = "bucketdjamel"
source_blob_name = "customers.csv"
destination_table="curious-context-412914.customers"
path_to_private_key = 'steel-aileron-442509-q8-8169b6f997b8.json'
load_csv_to_bigquery(bucket_name=bucket_name,source_blob_name=source_blob_name,destination_table=destination_table,path_to_private_key=path_to_private_key)
"""