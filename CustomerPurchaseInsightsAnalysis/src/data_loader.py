from pyspark.sql import SparkSession


def load_data(spark: SparkSession):
    customersPath="/Users/rahul1.patidar/pyspark-project/CustomerPurchaseInsightsAnalysis/data/customers.json"
    productsPath = "/Users/rahul1.patidar/pyspark-project/CustomerPurchaseInsightsAnalysis/data/products.json"
    purchasesPath = "/Users/rahul1.patidar/pyspark-project/CustomerPurchaseInsightsAnalysis/data/purchases.json"
    customers_df = spark.read.option("mode", "PERMISSIVE").option("multiline",True).json(customersPath)
    customers_df.printSchema()
    customers_df.show(truncate=False)


    products_df = spark.read.option("mode", "PERMISSIVE").option("multiline",True).json(productsPath)
    products_df.printSchema()
    products_df.show(truncate=False)
    purchases_df = spark.read.option("mode", "PERMISSIVE").option("multiline",True).json(purchasesPath)
    purchases_df.printSchema()
    purchases_df.show(truncate=False)
    return customers_df, products_df, purchases_df


