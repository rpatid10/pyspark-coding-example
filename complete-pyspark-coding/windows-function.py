import pyspark
from pyspark.sql import *
spark=SparkSession.builder.appName("test").master("local").getOrCreate()
data=[ [1,"rahul","IT",5000],
    [2,"umesh","CS",5000],
    [3,"kapil","IT",10000],
    [4,"ankit","CS",20000],
    [5,"ajit","HR",30000],
    [6,"vijay","CS",40000],
    [7,"avinash","managament",50000],
    [8,"ashish","HR",60000],
    [9,"jagadeesh","managament",70000],
    [10,"sanish","finance",80000],
]
schema=["id","name","department","salary"]
df=spark.createDataFrame(data,schema)


from pyspark.sql.functions import *
df2=df.withColumn("country",lit("india")).withColumnRenamed("id","empid")

from pyspark.sql.window import Window
windowSpec=Window.partitionBy("department").orderBy(desc("salary"))

windowSpecAgg=Window.partitionBy("department")

df3=df2.withColumn("rowNum",row_number().over(windowSpec)).withColumn("rankNum",rank().over(windowSpec)).withColumn("denseRank",dense_rank().over(windowSpec)).withColumn("lagSalary",lag("salary",1).over(windowSpec)).withColumn("leadSalary",lead("salary",1).over(windowSpec)).withColumn("TotalSalaryDepartmentWise",sum("salary").over(windowSpecAgg)).withColumn("AvgSalaryDepartmentWise", avg("salary").over(windowSpecAgg)).withColumn("MinSalaryDepartmentWise",min("salary").over(windowSpecAgg)).withColumn("MaxSalaryDepartmentWise",max("salary").over(windowSpecAgg))

df3.select("empid","name","department","salary","rowNum","rankNum","denseRank","lagSalary","leadSalary","TotalSalaryDepartmentWise","MaxSalaryDepartmentWise")

avg_salary = df.agg(avg("salary").alias("avg_salary"))

totalSalaryDepartWise=df.groupBy("department").agg(sum("salary").alias("HigesSalaryDepartment")).orderBy(desc("HigesSalaryDepartment"))

result_df= totalSalaryDepartWise.join(avg_salary).filter(col("HigesSalaryDepartment") < col("avg_salary"))

result_df.select("avg_salary","HigesSalaryDepartment")

avg_salary_collect=avg_salary.collect()[0]["avg_salary"]

totalSalaryDepartWise.filter(col("HigesSalaryDepartment")> avg_salary_collect).withColumnRenamed("HigesSalaryDepartment","salaryGreaterThenAvg").show()

