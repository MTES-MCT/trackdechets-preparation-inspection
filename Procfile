# Run web app
web: gunicorn --chdir src config.wsgi:application --log-file - --timeout 120

# Run celery worker
worker: celery --workdir src -A config worker -l info
