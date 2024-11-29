
# Migration de données d'une base PostgreSQL vers le cloud (Google Cloud Platform)

Ce projet met en œuvre des pipelines ETL Python pour extraire, transformer et charger les données depuis PostgreSQL vers Google Cloud Platform, démontrant ainsi ma capacité à migrer et à valoriser des données dans un environnement cloud. Les principaux avantages de la migration cloud sont la réduction des frais informatiques et l'amélioration des performances, ainsi que des avantages en termes de sécurité et de commodité, entre autres. Le cloud fournit également un package de technologie qui permet de développer des dashboards (Looker Studio), de développer et de mettre en production plus facilement des modèles de machine learning (AutoML, BigQueryML, VertexAI). 

## Méthodologie

- Extraction de ma table cible(customers) dans ma base de données avec le code **extract_transfrom_from_postgres.py**
- Chargement de ma table dans Google Cloud Storage (Google Cloud Storage est le Datalake de GCP)  avec le code **load_to_GCS.py**
- Migration de ma table de Google Cloud Storage vers le Datawarehouse Big Query avec le code **load_to_bigquery.py**

## Résultats

### Base de données PostgreSQL
<img width="958" alt="Capture1" src="https://github.com/user-attachments/assets/10750c8d-003c-4be4-b704-b7c3e16219e8">


### Chargement de la table customers dans Cloud Storage
<img width="946" alt="Capture3" src="https://github.com/user-attachments/assets/d59588f2-e00e-4390-ae07-08b212c91312">


### Migration de la table dans BigQuery
<img width="954" alt="Capture4" src="https://github.com/user-attachments/assets/0ce10086-d7a9-4a94-a65a-8724910e381d">


# Outils

<img width="165" alt="PostgreSQL" src="https://github.com/user-attachments/assets/1f17986f-1b2d-4b46-a8fa-e1abd16bb9e0">

<img width="165" alt="Capture_Python2" src="https://github.com/user-attachments/assets/9677d4d9-1e8b-40e7-95c6-62baee160746">

<img width="165" alt="Capture6" src="https://github.com/user-attachments/assets/9dbf2657-dbd1-4cf7-8850-91ef6d7f1e48">


<a href="#">#PostgreSQL</a>
<a href="#">#Python</a>
<a href="#"> #Google Cloud Platform</a>





