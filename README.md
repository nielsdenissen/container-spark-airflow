# Container Spark Airflow

A small project to setup a container with Python, Spark and Airflow.
This project is meant for development purposes to easily run and test Airflow DAGs with Spark code in them.

# Getting Started

## 1. Build
Build the docker container as follows:

    docker build -t container-spark-airflow .

## 2. Run
Then run it:

    docker run -v `pwd`/dags:/home/jovyan/airflow/dags/ -v `pwd`/files:/tmp/files/ -p 8080:8080 container-spark-airflow sh -c "airflow scheduler & airflow webserver -p 8080"

Airflow can now be found on: http://localhost:8080

In the UI you should be able to find the dag that is present under the `dags/` directory of this repository, it's called `sample-spark` and uses Spark to print the CSV file present in `files/`.

## How do I work with it?
We'll discuss a few topics here:

### How can I run a new DAG?

Simply create a python file with your new DAG definition (e.g. `new_dag.py`) and put it in the `dags/` folder. Then go to the airflow UI, refresh it and see your new dag pop up.

### How can I add data or other files that my DAG needs?

Every file you put in the `files` directory will be mounted inside the container under `/tmp/files`.
So if you put an `example.csv` file in your `files` directory, you can reference it as `/tmp/files/example.csv`.

### How can I write data and access it outside my container?

Same as reading data you can use the mounted `/tmp/files` directory. Any data you write to this folder (e.g. from your Spark application) will show up in your `files` directory.

### How do I install new packages?

In the `Dockerfile` add run commands as follows:

    RUN pip install pandas

Once you've done this you'll need to rerun the build command as listed above and you can restart your docker container.


## How does it work?
### Folder mounts
Folders are mounted as such in the docker container (IN THIS REPO -> INSIDE DOCKER CONTAINER):

- files/ -> /tmp/files/
- dags/ -> /home/jovyan/airflow/dags/

This means that if you have a file inside de `files` directory that you'd like to reference (let's take `sample.csv` as example), you'd do that as follows: `/tmp/files/sample.csv`.

### Logs
The logs can of course be seen in the airflow UI, but in case you like to see the logs directory as they're written to disk, you can add the following parameter to the run command above:

    -v `pwd`/logs:/home/jovyan/airflow/logs/

> Ensure you have created a `logs` directory from wherever you start your docker container.

This will map the logs directory as follows:

- logs/ -> /home/jovyan/airflow/logs/

Thus you'll be able to find your logs in the local `logs` directory.

> Be aware that if you don't clean up these logs yourself, they'll be appended by airflow on any subsequent run and thus will also contain all logs from previous runs.
