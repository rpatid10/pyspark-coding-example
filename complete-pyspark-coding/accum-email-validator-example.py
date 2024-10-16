from pyspark.sql import SparkSession
import re

spark = SparkSession.builder \
    .appName("Accumulator Use Case Example") \
    .getOrCreate()

invalid_count_accumulator = spark.sparkContext.accumulator(0)

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def check_valid_email(row):
    global invalid_count_accumulator
    email = row['email']
    if email is None or not is_valid_email(email):
        invalid_count_accumulator.add(1)
    return row

data = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", None),
    (3, "Charlie", "charlie@domain"),
    (4, "David", "david@example.com")
]
df = spark.createDataFrame(data, ["id", "name", "email"])

df.rdd.foreach(check_valid_email)

df.count()

print(f"Number of invalid records: {invalid_count_accumulator.value}")
