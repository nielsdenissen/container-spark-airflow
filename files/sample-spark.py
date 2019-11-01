# import necessary libraries
from pyspark.sql import SparkSession

# create sparksession
spark = SparkSession \
    .builder \
    .appName("Pysparkexample") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.csv("/tmp/files/sample.csv", header="true")
df.show()
