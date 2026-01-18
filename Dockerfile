FROM python:3.10-slim

WORKDIR /app

COPY build-a-budget-app.py .

CMD ["python", "build-a-budget-app.py"]
