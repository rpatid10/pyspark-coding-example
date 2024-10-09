from pyspark.sql import DataFrame
from pyspark.sql.functions import col, expr, broadcast

def transform_data(customers_df: DataFrame, products_df: DataFrame, purchases_df: DataFrame) -> DataFrame:
    # Flatten nested structures
    customers_flat_df = customers_df.select(
        col("customer_id").alias("customer_id_customers"),
        col("name"),
        col("location.city").alias("city"),
        col("location.state").alias("state")
    )

    # Optionally rename columns in products_df if needed
    products_flat_df = products_df.select(
        col("product_id").alias("product_id_products"),
        col("product_name")
    )

    # Salting to handle data skew
    salted_purchases_df = purchases_df.withColumn("salt", expr("rand() % 10"))
    salted_purchases_df = salted_purchases_df.withColumn("salted_customer_id", expr("concat(customer_id, '_', salt)"))

    # Broadcast joins
    joined_df = salted_purchases_df.join(
        broadcast(customers_flat_df),
        salted_purchases_df.salted_customer_id.substr(1, 4) == customers_flat_df.customer_id_customers
    ).join(
        broadcast(products_flat_df),
        salted_purchases_df.product_id == products_flat_df.product_id_products
    )

    # Cache the joined DataFrame
    joined_df.cache()

    # Repartitioning
    optimized_df = joined_df.repartition("customer_id_customers")

    return optimized_df
