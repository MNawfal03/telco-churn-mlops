# 📡 Telco Customer Churn Prediction - End-to-End MLOps

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([TON_LIEN_CLOUD_RUN](https://churn-app-790801494167.us-central1.run.app/))

## 🎯 Objectif Business
L'objectif est de prédire quels clients sont susceptibles de résilier leur abonnement (Churn) afin de permettre à l'équipe marketing de mettre en place des campagnes de rétention ciblées.

## 🚀 Fonctionnalités
- **Analyse de données (EDA)** : Identification des facteurs clés (Contrats, Services, Facturation).
- **Feature Engineering** : Création de variables métier (`HighPrice_NoCommitment`, `Price_Velocity`).
- **Machine Learning** : Modèle Random Forest avec un **Recall de 79%** (priorité à la détection des départs).
- **Déploiement** : Web App interactive déployée sur **Google Cloud Run** via **Docker**.

## 🛠️ Stack Technique
- **Langage** : Python 3.9
- **Data** : Pandas, Scikit-learn, BigQuery
- **Interface** : Streamlit
- **DevOps** : Docker, Google Artifact Registry, Google Cloud Run

## 💻 Installation locale
1. Cloner le dépôt : `git clone https://github.com/MNawfal03/telco-churn-mlops.git`
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer l'app : `streamlit run app/app.py
