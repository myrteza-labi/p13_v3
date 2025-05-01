# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du projet dans le conteneur
COPY . .

# Exposer le port utilisé par l'application
EXPOSE 8000

# CMD : applique les migrations, collecte les fichiers statiques, puis démarre Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]
