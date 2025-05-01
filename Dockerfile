# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du projet dans le conteneur
COPY . .

# ✅ Debug : Affiche le contenu de fixtures/lettings.json
RUN echo "=== Contenu initial de fixtures/lettings.json ===" && cat fixtures/lettings.json && echo "=== Fin ==="

# 🧹 Supprimer le BOM UTF-8 (Byte Order Mark) des fichiers JSON
RUN python3 -c "import glob; [open(p, 'wb').write(open(p, 'rb').read().lstrip(b'\xef\xbb\xbf')) for p in glob.glob('fixtures/*.json')]"

# ✅ Debug : Affiche à nouveau le contenu après nettoyage BOM
RUN echo '=== Contenu après nettoyage BOM ===' && cat fixtures/lettings.json && echo "=== Fin ==="

# Exposer le port utilisé par l'application
EXPOSE 8000

# CMD : applique migrations, charge les fixtures, collecte les statics, puis démarre Gunicorn
CMD ["sh", "-c", "\
    python manage.py migrate --noinput && \
    python manage.py loaddata fixtures/lettings.json fixtures/profiles.json && \
    python manage.py collectstatic --noinput && \
    gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000\
"]
