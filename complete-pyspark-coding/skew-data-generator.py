import random
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

# Initialize Spark session
spark = SparkSession.builder.appName("SaltingExample").getOrCreate()

# Generate skewed data
data = []
statuses = ['success', 'failed', 'initiated']

for i in range(1, 101):
    status = 'success' if random.random() < 0.9 else random.choice(['failed', 'initiated'])
    txnid = i
    txndate = f'2024-08-{random.randint(1, 30):02d}'
    data.append((txnid, txndate, status))

schema = StructType([
    StructField("txnid", IntegerType(), True),
    StructField("txndate", StringType(), True),
    StructField("status", StringType(), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Define highly skewed statuses
highly_skewed_statuses = ['success']

# Add salt to the DataFrame
df_with_salt = df.withColumn(
    "salt",
    F.when(F.col("status").isin(highly_skewed_statuses), F.floor(F.rand() * 10)).otherwise(F.lit(0))
)

# Create a new column with salted status
df_with_salt = df_with_salt.withColumn("salted_status", F.concat(F.col("status"), F.lit("_"), F.col("salt")))

# Show the distribution of salted statuses
status_distribution = df_with_salt.groupBy("salted_status").count().show()

# Optionally, show the original DataFrame with salt
df_with_salt.show()
