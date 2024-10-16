from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder.appName("LogProcessing").master("local").getOrCreate()

# Create accumulators for counting successful and failed requests
success_count = spark.sparkContext.accumulator(0)
failure_count = spark.sparkContext.accumulator(0)

# Sample log data (transactionId, status)
log_data = [
    (101, "SUCCESS"),
    (102, "FAILURE"),
    (103, "SUCCESS"),
    (104, "SUCCESS"),
    (105, "FAILURE")
]
log_df = spark.createDataFrame(log_data, ["transactionId", "status"])

# Function to update the accumulators based on status
def update_status_counts(row):
    global success_count, failure_count
    if row.status == "SUCCESS":
        success_count += 1
    elif row.status == "FAILURE":
        failure_count += 1

# Apply the function to each row of the DataFrame
log_df.foreach(update_status_counts)

# Output the counts
print(f"Total Successful Requests: {success_count.value}")
print(f"Total Failed Requests: {failure_count.value}")

# Show the original DataFrame
print("Log DataFrame:")
log_df.show()
