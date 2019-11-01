FROM jupyter/pyspark-notebook:latest

RUN pip install apache-airflow \
    && mkdir ~/airflow

ENV AIRFLOW_HOME=~/airflow
RUN cd ~/airflow && airflow initdb

COPY airflow.cfg /tmp/airflow.cfg
RUN cp /tmp/airflow.cfg ~/airflow/airflow.cfg
