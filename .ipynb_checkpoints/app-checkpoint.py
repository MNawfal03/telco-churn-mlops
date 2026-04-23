import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Configuration de la page
st.set_page_config(page_title="Telco Churn Predictor", layout="centered")

# 2. Chargement du modèle (On utilise le cache pour la rapidité)
@st.cache_resource
def load_model():
    # Remplace par le nom exact de ton fichier .pkl
    return joblib.load('telco_churn_model_final.pkl')

pkg = load_model()
model = pkg['model']
features_list = pkg['features']
threshold = pkg['threshold']

st.title("📡 Prédiction de Résiliation Client")
st.write("Saisissez les informations du client pour évaluer son risque de départ.")

# 3. Formulaire de saisie
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        tenure = st.number_input("Ancienneté (mois)", min_value=1, max_value=72, value=12)
        monthly_charges = st.number_input("Charges Mensuelles ($)", min_value=18, max_value=120, value=70)
        total_charges = st.number_input("Total des Charges ($)", min_value=0, max_value=9000, value=800)
    
    with col2:
        contract = st.selectbox("Type de Contrat", ["Month-to-month", "One year", "Two year"])
        internet = st.selectbox("Service Internet", ["Fiber optic", "DSL", "No"])
        security = st.selectbox("Sécurité en ligne", ["Yes", "No"])
        tech_support = st.selectbox("Support Technique", ["Yes", "No"])

    submit = st.form_submit_button("Calculer le risque")

# 4. Traitement des données et Prédiction
if submit:
    # Création du DataFrame brut (on simule les colonnes One-Hot)
    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'Contract_Month-to-month': 1 if contract == "Month-to-month" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'InternetService_Fiber optic': 1 if internet == "Fiber optic" else 0,
        'OnlineSecurity_No': 1 if security == "No" else 0,
        'TechSupport_No': 1 if tech_support == "No" else 0
    }
    
    df_input = pd.DataFrame([data])
    
    # --- TON FEATURE ENGINEERING ---
    df_input['HighPrice_NoCommitment'] = df_input['Contract_Month-to-month'] * df_input['MonthlyCharges']
    df_input['Price_Velocity'] = df_input['TotalCharges'] / (df_input['tenure'] + 1)
    df_input['Price_Diff'] = df_input['MonthlyCharges'] - df_input['Price_Velocity']
    
    # On s'assure d'avoir toutes les colonnes attendues par le modèle (même celles à 0)
    for col in features_list:
        if col not in df_input.columns:
            df_input[col] = 0
            
    # Réorganisation des colonnes pour matcher le modèle
    df_input = df_input[features_list]
    
    # Prédiction
    proba = model.predict_proba(df_input)[0, 1]
    
    # Affichage du résultat
    st.subheader(f"Probabilité de départ : {proba:.1%}")
    if proba >= threshold:
        st.error("⚠️ ALERTE : Risque de Churn élevé !")
    else:
        st.success("✅ Client stable.")