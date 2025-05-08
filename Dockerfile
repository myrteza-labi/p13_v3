# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du projet dans le conteneur
COPY . .

# ✅ Debug : Affiche le contenu initial de fixtures/lettings.json
RUN echo "=== Contenu initial de fixtures/lettings.json ===" && cat fixtures/lettings.json && echo "=== Fin ==="

# ✅ Ajouter un script pour nettoyer le BOM
RUN echo '\
import glob\n\
for p in glob.glob("fixtures/*.json"):\n\
    with open(p, "rb") as f:\n\
        content = f.read()\n\
    if content.startswith(b"\xef\xbb\xbf"):\n\
        with open(p, "wb") as f_out:\n\
            f_out.write(content.lstrip(b"\xef\xbb\xbf"))\n\
' > remove_bom.py

# ✅ Exécuter le script de nettoyage BOM
RUN python3 remove_bom.py

# ✅ Debug : Affiche le contenu après nettoyage BOM
RUN echo '=== Contenu après nettoyage BOM ===' && cat fixtures/lettings.json && echo "=== Fin ==="

# Exposer le port utilisé par l'application
EXPOSE 8000

# CMD : applique migrations, charge les fixtures, collecte les statics, puis démarre Gunicorn
CMD ["sh", "-c", "\
    echo '🧪 Fichiers JSON présents :' && ls -lh fixtures && \
    echo '📄 Contenu de lettings.json :' && cat fixtures/lettings.json && \
    echo '🚀 MIGRATIONS' && python manage.py migrate --noinput && \
    echo '📦 LOADDATA' && python manage.py loaddata fixtures/users.json fixtures/lettings.json fixtures/profiles.json && \
    echo '🧹 COLLECTSTATIC' && python manage.py collectstatic --noinput && \
    echo '🔥 Gunicorn Start' && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000 --timeout 120
"]
