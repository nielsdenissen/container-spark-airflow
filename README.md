# Container Spark Airflow

A small project to setup a container with Python, Spark and Airflow.
This project is meant for development purposes to easily run and test Airflow DAGs with Spark code in them.

# How to use

## 1. Build

    docker build -t container-spark-airflow .

## 2. Run

    docker run -v `pwd`/dags:/home/jovyan/airflow/dags/ -v `pwd`/files:/tmp/files/ -p 8080:8080 container-spark-airflow sh -c "airflow scheduler & airflow webserver -p 8080"

Airflow can now be found on: http://localhost:8080

### Folder mounts

Folders are mounted as such in the docker container (IN THIS REPO -> INSIDE DOCKER CONTAINER):

- files/ -> /tmp/files/
- dags/ -> /home/jovyan/airflow/dags/

This means that if you have a file inside de `files` directory that you'd like to reference (let's take `sample.csv` as example), you'd do that as follows: `/tmp/files/sample.csv`.

### Logs

The logs can of course be seen in the airflow UI, but in case you like to see the logs directory as they're written to disk, you can add the following parameter to the run command above:

    -v `pwd`/logs:/home/jovyan/airflow/logs/

This will map the logs directory as follows:

- logs/ -> /home/jovyan/airflow/logs/

Thus you'll be able to find your logs in the local `logs` directory.

> Be aware that if you don't clean up these logs yourself, they'll be appended by airflow on any subsequent run and thus will also contain all logs from previous runs.
