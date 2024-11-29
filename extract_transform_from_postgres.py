
# Import des packages
import datetime
import logging
import os
import pandas as pd
from sqlalchemy import create_engine
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd
import psycopg2


# Fonction d'extraction et de transformation de la base de données depuis PostgreSQL

def extract_transform_from_DBMS(connection_info):
        """
    Extraire les données d'une table PostgreSQL dans un DataFrame Pandas.

    Arguments :
        table_name (str) : Nom de la table PostgreSQL à partir de laquelle extraire les données.
        connection_string (str) : Chaîne de connexion PostgreSQL.

    Retourne :
        pandas.DataFrame : Les données extraites, ou None en cas d'erreur.
    """
        
        try:
            # Extraction
            conn = psycopg2.connect(
                user=connection_info['user'],
                password=connection_info['password'],
                host=connection_info['host'],
                port=connection_info['port'],
                database=connection_info['database']  
            )
            
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {connection_info['table_name']}")
            
            
            column_names = [col[0] for col in cursor.description]  
            
            df = pd.DataFrame(cursor.fetchall(), columns=column_names)
            
            #Transformation
            filtered_df = df.dropna(axis = 0)
            filtered_df = filtered_df.rename(columns = str.lower)
            
            conn.close()
            return filtered_df
            
        except Exception as e:
            print(f"Error extracting data from {connection_info["table_name"]}: {e}")
            return None


"""
connection_info = {
    "user": "postgres",
    "password": "Isma",
    "host": "localhost", 
    "port": 5432,
    "database": "E-commerceDatabase",
    "table_name": "customers"  
    }
        
df=extract_transform_from_DBMS(connection_info=connection_info)
print(df)
"""