from pyspark.sql import *
from pyspark.sql.functions import *
import time



spark=SparkSession.builder.appName("performance").master("local").getOrCreate()
transaction_count_accumulator = spark.sparkContext.accumulator(0)


merchant_data = [(1, "HDFC Bank"),
                 (2, "ICICI Bank"),
                 (3, "SBI Bank")]
merchant_df = spark.createDataFrame(merchant_data, ["merchantId", "merchantName"])


transaction_data = [(101, 1, 100.0),
                    (102, 2, 150.0),
                    (103, 1, 200.0),
                    (104, 3, 250.0),
                    (105, 8, 300.0)]
transaction_df = spark.createDataFrame(transaction_data, ["transactionId", "merchantId", "amount"])


# Perform a broadcast join
joined_df = transaction_df.join(broadcast(merchant_df), on="merchantId", how="inner")


# After processing, get the value of the accumulator
# Function to update the accumulator
joined_df.show()