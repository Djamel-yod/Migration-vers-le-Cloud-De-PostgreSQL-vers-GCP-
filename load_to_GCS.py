
# Import des packages
import datetime
import logging
import os
import pandas as pd
from sqlalchemy import create_engine
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd

# Fonction de chargement des données dans Cloud Storage

def upload_to_GCS(df,bucket_name,destination_blob_name,path_to_private_key):
    
    """
    Télécharge un dataframe pandas les charge dans un bucket Google Cloud Storage.

    Arguments :
        df: Nom du dataframe pandas
        bucket_name (str) : Nom du bucket Google Cloud Storage.
        destination_blob_name (str) : Nom du fichier dans le bucket.

    Retourne :
        bool : True si l'opération a réussi, False sinon.
    """


    try:
        
        # Créer un client pour interagir avec Cloud Storage
       
        storage_client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name) 
        
        # Télécharger le fichier dans le bucket
        blob.upload_from_string(df.to_csv(), 'text/csv')

        return True
    
    except Exception as e:
        print(f"Erreur lors de l'extraction ou du chargement : {e}")
        return False