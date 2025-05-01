# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# 1. migrate
# 2. strip BOM des fixtures (en Python)
# 3. loaddata
# 4. collectstatic
# 5. démarrage de gunicorn
CMD ["sh", "-c", "\
    python manage.py migrate --noinput && \
    python -c \"import glob;[open(p,'wb').write(open(p,'rb').read().lstrip(b'\\xef\\xbb\\xbf')) for p in glob.glob('fixtures/*.json')]\" && \
    python manage.py loaddata fixtures/lettings.json fixtures/profiles.json && \
    python manage.py collectstatic --noinput && \
    gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000\
"]
