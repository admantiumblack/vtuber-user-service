FROM apache/airflow:2.1.0
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential libopenmpi-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get update
USER airflow

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt