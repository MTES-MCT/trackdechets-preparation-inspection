# Run web app
web: gunicorn --chdir src core.wsgi:application --log-file -

# Run celery worker
worker: celery --workdir src -A core worker -l info
