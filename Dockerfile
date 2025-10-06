FROM python:3.7-slim
RUN pip install Flask gunicorn
WORKDIR /app
COPY . .
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
