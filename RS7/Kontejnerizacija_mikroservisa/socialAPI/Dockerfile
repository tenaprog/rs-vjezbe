FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pydantic

EXPOSE 3500

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3500"]
