
# Migration de données d'une base PostgreSQL vers le cloud (Google Cloud Platform)

Ce projet met en œuvre des pipelines ETL Python pour extraire, transformer et charger les données depuis PostgreSQL vers Google Cloud Platform, démontrant ainsi ma capacité à migrer et à valoriser des données dans un environnement cloud. Les principaux avantages de la migration cloud sont la réduction des frais informatiques et l'amélioration des performances, ainsi que des avantages en termes de sécurité et de commodité, entre autres. Le cloud fournit également un package de technologie qui permet de développer des dashboards (Looker Studio), de développer et de mettre en production plus facilement des modèles de machine learning (AutoML, BigQueryML, VertexAI). 

## Méthodologie

- Extraction de ma table cible dans ma base de données avec le code **extract_transfrom_from_postgres.py**
- Chargement de ma table dans Google Cloud Storage (Google Cloud Storage est le Datalake de GCP)  avec le code **load_to_GCS.py**
- Migration de ma table de Google Cloud Storage vers le Datawarehouse Big Query avec le code **load_to_bigquery.py**

## Résultats


<img width="958" alt="Capture1" src="https://github.com/user-attachments/assets/10750c8d-003c-4be4-b704-b7c3e16219e8">

<img width="946" alt="Capture3" src="https://github.com/user-attachments/assets/d59588f2-e00e-4390-ae07-08b212c91312">



