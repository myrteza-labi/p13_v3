# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du projet dans le conteneur
COPY . .

# 🔍 Debug : afficher le contenu du dossier fixtures
RUN echo "Contenu du dossier fixtures :" && ls -l fixtures

# 🧹 Retirer le BOM des fichiers .json
RUN python3 -c "import glob; [open(p, 'wb').write(open(p, 'rb').read().lstrip(b'\xef\xbb\xbf')) for p in glob.glob('fixtures/*.json')]"

# Exposer le port utilisé par l'application
EXPOSE 8000

# CMD : migrations, chargement fixtures, collectstatic, gunicorn
CMD ["sh", "-c", "\
    python manage.py migrate --noinput && \
    python manage.py loaddata fixtures/lettings.json fixtures/profiles.json && \
    python manage.py collectstatic --noinput && \
    gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000\
"]
