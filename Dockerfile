FROM python:3.6
WORKDIR /app
COPY src/app.py .
ENTRYPOINT ["python", "app.py"]