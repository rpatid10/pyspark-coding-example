ifrom pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Create a simple DataFrame
data = [("Alice", 1), ("Bob", 2), ("Catherine", 3)]
df = spark.createDataFrame(data, ["Name", "Value"])

# Show DataFrame
df.show()

# Stop Spark session
spark.stop()

