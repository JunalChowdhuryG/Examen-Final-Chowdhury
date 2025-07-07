
FROM python:3.10-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.10-slim as runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8001
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN ./entrypoint.sh
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]