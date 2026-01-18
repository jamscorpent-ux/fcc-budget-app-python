FROM python:3.10-slim

WORKDIR /app

COPY budget_app.py

CMD ["python", "budget_app.py"
