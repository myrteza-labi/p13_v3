# Utiliser une image officielle de Python
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Apply migrations, strip BOM from fixtures, load fixtures, collect statics, then start Gunicorn
CMD ["sh", "-c", "\
    python manage.py migrate --noinput && \
    # Retire l’éventuel BOM au début des fichiers fixtures JSON \
    for f in fixtures/*.json; do sed -i '1s/^\\xEF\\xBB\\xBF//' \"$f\"; done && \
    python manage.py loaddata fixtures/lettings.json fixtures/profiles.json && \
    python manage.py collectstatic --noinput && \
    gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000\
"]
