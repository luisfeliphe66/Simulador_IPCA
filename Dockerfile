ARG PYTHON_VERSION=3.9-slim
ARG MYSQL_VERSION=8.0.32

FROM python:${PYTHON_VERSION} AS streamlit

WORKDIR /app

COPY ./src/streamlit /app
COPY ./data /app/data

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["streamlit", "run", "/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]

FROM python:${PYTHON_VERSION} AS consumer

WORKDIR /app

COPY ./src/consumer /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "consumer.py"]
