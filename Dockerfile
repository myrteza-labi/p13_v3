# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet (hors .sqlite3 grâce à .dockerignore)
COPY . .

# Exposer le port
EXPOSE 8000

# À l'exécution :
# 1) Appliquer les migrations
# 2) Collecter les fichiers statiques
# 3) Démarrer Gunicorn
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]
