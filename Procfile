# Render Procfile for CoffeeGuard
# Uses gunicorn with optimized settings for fast startup and response times

web: gunicorn --workers=4 --worker-class=sync --timeout=60 --keep-alive=5 --bind 0.0.0.0:$PORT --access-logfile - --error-logfile - --log-level info app:app
