# Utilise une image Python légère
FROM python:3.9-slim

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Copie tous les fichiers de ton dossier actuel dans le conteneur
COPY . .

# Installe les bibliothèques
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port 8080 (le port standard pour Cloud Run)
EXPOSE 8080

# Lance l'application Streamlit sur le bon port
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]