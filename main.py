import extract_transform_from_postgres
import load_to_bigquery
import load_to_GCS

def main():
    
    # Extraction de la table dans PosgreSQL
    
    connection_info = {
    "user": "postgres",
    "password": "Isma",
    "host": "localhost", 
    "port": 5432,
    "database": "E-commerceDatabase",
    "table_name": "customers"  
    }
        
    df=extract_transform_from_postgres.extract_transform_from_DBMS(connection_info=connection_info)

    # Chargement de la base de données dans Cloud Storage
    bucket_name = "bucketdjamel"
    destination_blob_name = "customers4.csv"
    path_to_private_key = 'steel-aileron-442509-q8-8169b6f997b8.json' 
    load_to_GCS.upload_to_GCS(df=df,bucket_name=bucket_name,destination_blob_name=destination_blob_name,path_to_private_key=path_to_private_key)
    
    # Chargement de la base de données dans Big Query
    bucket_name = "bucketdjamel"
    source_blob_name = "customers.csv"
    destination_table="curious-context-412914.customers"
    path_to_private_key = 'steel-aileron-442509-q8-8169b6f997b8.json'
    load_to_bigquery.load_csv_to_bigquery(bucket_name=bucket_name,source_blob_name=source_blob_name,destination_table=destination_table,path_to_private_key=path_to_private_key)
    
if __name__ == '__main__':
    main()