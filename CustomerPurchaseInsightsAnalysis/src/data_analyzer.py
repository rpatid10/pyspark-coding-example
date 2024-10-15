from pyspark.sql import DataFrame
from pyspark.sql.functions import *


def analyze_data(optimized_df: DataFrame):
    # Total Sales per Customer
    total_sales_per_customer = optimized_df.groupBy("customer_id").agg(sum("amount").alias("total_sales"))
    total_sales_per_customer.show()

    # Most Popular Products
    popular_products = optimized_df.groupBy("product_id").agg(count("purchase_id").alias("purchase_count"))
    popular_products.show()

    # Sales Trends Over Time
    sales_trends = optimized_df.withColumn("date", to_date("timestamp")) \
        .groupBy("date").agg(sum("amount").alias("daily_sales"))
    sales_trends.show()

    # Save Results
    total_sales_per_customer.write.mode("overwrite").json("data/total_sales_per_customer.json")
    popular_products.write.mode("overwrite").json("data/popular_products.json")
    sales_trends.write.mode("overwrite").json("data/sales_trends.json")
/Users/rahul1.patidar/pyspark-project/CustomerPurchaseInsightsAnalysis