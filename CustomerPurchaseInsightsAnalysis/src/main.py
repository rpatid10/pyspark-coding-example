from pyspark.sql import SparkSession
from data_loader import load_data
from data_transformer import transform_data
from data_analyzer import analyze_data

def main():
    spark = SparkSession.builder \
        .appName("Customer Purchase Insights Analysis") \
        .getOrCreate()

    # Load data
    customers_df, products_df, purchases_df = load_data(spark)

    # Transform data
    optimized_df = transform_data(customers_df, products_df, purchases_df)

    # Analyze data
    analyze_data(optimized_df)

    spark.stop()

if __name__ == "__main__":
    main()
