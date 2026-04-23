# 📡 Telco Customer Churn Prediction - End-to-End MLOps

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://churn-app-790801494167.us-central1.run.app/)

> **Accéder à l'application web :** [Démo en direct sur Google Cloud Run](https://churn-app-790801494167.us-central1.run.app/)

## 🎯 Objectif Business
L'objectif est de prédire quels clients sont susceptibles de résilier leur abonnement (Churn). Cela permet à l'équipe marketing de concentrer ses efforts de rétention sur les profils à haut risque, optimisant ainsi les budgets de campagne et réduisant le taux d'attrition global.

## 🚀 Fonctionnalités
- **Analyse de données (EDA)** : Exploration des facteurs de résiliation (Contrats, Services, Facturation).
- **Feature Engineering** : Création de variables prédictives métier comme `HighPrice_NoCommitment` et `Price_Velocity`.
- **Modèle Prédictif** : Algorithme Random Forest optimisé pour la détection proactive des départs.
- **Déploiement** : Application web interactive conteneurisée avec Docker et hébergée sur **Google Cloud Run**.

## 📊 Modélisation & Performance

Pour ce projet, nous avons privilégié le **Recall** (Sensibilité). En entreprise, il est crucial de détecter un maximum de départs potentiels (Vrais Positifs), quitte à avoir quelques fausses alertes, plutôt que de laisser partir un client sans aucune action de rétention.

### Résultats (Seuil de décision optimisé à 0.38) :

| Métrique | Score | Impact Business |
| :--- | :--- | :--- |
| **Recall (Sensibilité)** | **79%** | Identifie près de 8 clients sur 10 prêts à partir. |
| **Précision** | **50%** | Une alerte sur deux déclenche une action marketing justifiée. |
| **Accuracy** | **74%** | Performance globale robuste sur l'ensemble du dataset. |

### Top 3 des facteurs de risque identifiés :
1. **Contrats "Month-to-month"** : Forte volatilité liée à l'absence d'engagement.
2. **HighPrice_NoCommitment** : Clients payant des frais élevés sans contrat long terme.
3. **Ancienneté (Tenure)** : Les nouveaux clients sont les plus fragiles durant les 6 premiers mois.

## 🛠️ Stack Technique
- **Langage** : Python 3.9
- **Data Science** : Scikit-learn, Pandas, Numpy, Joblib
- **Interface** : Streamlit
- **DevOps** : Docker, Google Cloud Run, Cloud Build, Artifact Registry

## 💻 Installation locale

1. **Cloner le dépôt** :
   ```bash
   git clone [https://github.com/MNawfal03/telco-churn-mlops.git](https://github.com/MNawfal03/telco-churn-mlops.git)
   cd telco-churn-mlops

2. **Installer les dépendances** :
  ```bash
  pip install -r requirements.txt
  ```

3. **Lancer l'application** :
  ```bash
  streamlit run app.py
   ```

### 💡 Rappel pour la mise à jour sur GitHub :
1. Ouvre ton terminal dans Vertex AI ou sur ton PC.
2. Tape `nano README.md` pour éditer le fichier (ou utilise l'interface graphique de GitHub).
3. Colle ce texte.
4. Sauvegarde et fais ton push :
   ```bash
   git add README.md
   git commit -m "docs: final update of business metrics and structure"
   git push origin main
