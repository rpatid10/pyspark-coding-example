from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import Window

# Create Spark Session
spark = SparkSession.builder \
    .appName("Comprehensive PySpark Example") \
    .getOrCreate()

# 1. Create RDDs
data = [1, 2, 3, 4, 5]
rdd1 = spark.sparkContext.parallelize(data)

# From a text file
# rdd2 = spark.sparkContext.textFile("hdfs://path/to/textfile.txt")

# 2. Create DataFrames
df1 = rdd1.map(lambda x: (x, x * 2)).toDF(["value", "double_value"])

# From a CSV file
# df2 = spark.read.csv("hdfs://path/to/data.csv", header=True, inferSchema=True)

# From a JSON file
# df3 = spark.read.json("hdfs://path/to/data.json")

# 3. Create Datasets (simulated as DataFrames in PySpark)
ds = df1

# 4. Convert DataFrames to RDDs
rdd_from_df = df1.rdd

# 5. Wide and Narrow Transformations
# Narrow Transformation
rdd_narrow = rdd1.map(lambda x: x * 2)

# Wide Transformation
rdd_wide = rdd1.groupBy(lambda x: x % 2)

# 6. Actions
count = rdd1.count()
collected_data = rdd1.collect()

# 7. Joins (dummy DataFrames for demonstration)
df2 = spark.createDataFrame([(1, "A"), (2, "B"), (3, "C")], ["key", "value"])
df_join = df1.join(df2, df1.value == df2.key, "inner")

# Broadcast Join
df_broadcast = df1.join(broadcast(df2), df1.value == df2.key, "inner")

# 8. Window Functions
window_spec = Window.partitionBy("value").orderBy("double_value")
df_with_rank = df1.withColumn("rank", rank().over(window_spec))

# 9. Salting
df_salted = df1.withColumn("salt", expr("floor(rand() * 5)"))

# 10. Accumulator
accum = spark.sparkContext.accumulator(0)

def count_elements(x):
    global accum
    accum += 1
    return x

rdd1.foreach(count_elements)
print(f"Accumulator value: {accum.value}")

# 11. Cache/Persist
df_cached = df1.cache()

# 12. Repartition/Coalesce
df_repartitioned = df1.repartition(10)
df_coalesced = df1.coalesce(5)

# 13. Group By and Window Functions
df_grouped = df1.groupBy("value").agg(sum("double_value").alias("sum_value"))

# 14. Case Statements
df_case = df1.withColumn("case_col", when(col("value") > 0, "Positive").otherwise("Negative"))

# 15. Explode
# Assuming df with an array column
df_array = spark.createDataFrame([(1, ["A", "B"]), (2, ["C", "D"])], ["id", "letters"])
df_exploded = df_array.select("id", explode("letters").alias("letter"))

# 16. StructType and StructField
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("value", StringType(), True)
])
df_struct = spark.createDataFrame([(1, "A"), (2, "B")], schema=schema)

# 17. Map and FlatMap
rdd_map = rdd1.map(lambda x: x + 1)
rdd_flatmap = rdd1.flatMap(lambda x: (x, x * 2))

# 18. Select Columns from RDD and DataFrame
df_selected = df1.select("value")
rdd_selected = rdd1.map(lambda x: (x,))

# 19. Save DataFrame as Table (bucket, partition)
# df1.write.format("parquet").partitionBy("value").saveAsTable("my_table")

# 20. Save to HDFS
# df1.write.csv("hdfs://path/to/save/location", header=True)

# Show results for verification
df1.show()
df_join.show()
df_broadcast.show()
df_with_rank.show()
df_case.show()
df_exploded.show()
df_selected.show()

# Stop the Spark session
spark.stop()



