FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir aiohttp

EXPOSE 9000

CMD ["python", "main.py"]
