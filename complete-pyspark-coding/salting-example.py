from pyspark.sql import *
from pyspark.sql.functions import *
import time



spark=SparkSession.builder.appName("performance").master("local").getOrCreate()
transaction_count_accumulator = spark.sparkContext.accumulator(0)


data=([1,"success"],[1,"success"],[2,"success"],[3,"success"],[4,"success"],[5,"failed"],[6,"initiated"])
df=spark.createDataFrame(data,["txnid","status"])
df.createTempView("tmp")
#df2=spark.sql("select count(*) as txnCount,status from tmp group by status")
#df2.show()
df3 = df.withColumn(
    "saltedStatus",
    when(df["status"] == "success", concat(df["status"], lit("_"), (rand() * 1000).cast("int")))
    .otherwise(df["status"])
)


df3.createTempView("tmp1")
df2_salted = (
    spark.sql("""SELECT COUNT(*) AS txnCount, SPLIT(saltedStatus, '_')[0] AS status FROM tmp1 GROUP BY SPLIT(saltedStatus, '_')[0]"""))






