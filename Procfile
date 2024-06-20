# Run web app
web: gunicorn --chdir src config.wsgi:application --log-file - --timeout 120

# post-deploy tasks
postdeploy: bash src/bin/post_deploy

# Run celery worker
worker: celery --workdir src -A config worker -Q web-queue -l info
worker: celery --workdir src -A config worker -Q api-queue -l info
