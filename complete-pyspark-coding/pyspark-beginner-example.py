from pyspark.sql import SparkSession
from pyspark.sql.functions import rand
from pyspark.sql.functions import expr, rand, broadcast


# Initialize Spark session
spark = SparkSession.builder.appName("pyspark").master("local").getOrCreate()

# Create a list
a = [1, 2, 3, 4, 5, 6]

b = spark.sparkContext.parallelize(a)

b_tuples = b.map(lambda x: (x,))

df= b_tuples.toDF(["id"])

df.show()

list=((1,"rahul"),(2,"sonu"),(1,"rohit"),(1,"rajat"))
schema=["id","name"]
df=spark.createDataFrame(list,schema)
df.show()

df2 = df.withColumn("salted", (rand() * 10).cast("int"))
df2.show()

df3=df.join(broadcast(df2),"id","inner")
df3.show()