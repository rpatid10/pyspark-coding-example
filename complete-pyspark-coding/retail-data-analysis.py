from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, count as spark_count, row_number
from pyspark.sql.window import Window

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Customer and Merchant Analysis") \
    .getOrCreate()

# Sample data for Account_transaction_history
txn_data = [
    (29310088, 146596905, '2023091913:24:00', 579, 747.44, 'F2F'),
    (15776446, 146596905, '2023092313:24:00', 982, 964.63, 'Online'),
    (88714126, 146596905, '2023062713:24:00', 957, 499.71, 'Online'),
    (83307091, 146596905, '2023091113:24:00', 982, 332.94, 'Online'),
    (29310089, 146596906, '2023092013:24:00', 579, 1000.00, 'F2F'),
    (15776447, 146596906, '2023092413:24:00', 982, 500.00, 'Online')
]

# Sample data for Merchant_Details
merchant_data = [
    (579, 'CHARITY', 88752),
    (982, 'AIRLINES', 58890),
    (957, 'AUTOMOTIVE', 19900)
]

# Create DataFrames
txn_df = spark.createDataFrame(txn_data, ['txn_id', 'card_number', 'txn_date', 'merchant_code', 'txn_amount', 'channel'])
merchant_df = spark.createDataFrame(merchant_data, ['merchant_code', 'merchant_catg', 'merchant_zip_code'])

# Step 1: Join DataFrames on 'merchant_code'
merged_df = txn_df.join(merchant_df, on='merchant_code', how='inner')

# Step 2: Calculate total spend per merchant in each category
merchant_spend = merged_df.groupBy('merchant_catg', 'merchant_code') \
    .agg(spark_sum('txn_amount').alias('total_spend'))
merchant_spend.show()

# Calculate total spend per category
category_total_spend = merged_df.groupBy('merchant_catg') \
    .agg(spark_sum('txn_amount').alias('total_category_spend'))

# Calculate share of spend for each merchant in each category
merchant_share = merchant_spend.join(category_total_spend, on='merchant_catg') \
    .withColumn('share_of_spend', (col('total_spend') / col('total_category_spend')) * 100)

# Show share of spend results
merchant_share.show()

# Step 3: Find the merchant with the highest transactions and spend share for each customer
# Calculate total transaction count per merchant and category
merchant_txn_count = merged_df.groupBy('card_number', 'merchant_catg', 'merchant_code') \
    .agg(spark_count('txn_id').alias('txn_count'))

# Join the spend share data back to transaction count data
merchant_stats = merchant_txn_count.join(merchant_share, on=['merchant_catg', 'merchant_code'])

# Create window specifications
window_spec_txn = Window.partitionBy('card_number', 'merchant_catg').orderBy(col('txn_count').desc())
window_spec_share = Window.partitionBy('card_number', 'merchant_catg').orderBy(col('share_of_spend').desc())

# Get the merchant with highest transactions and spend share
top_merchants_by_txn = merchant_stats.withColumn('row_num', row_number().over(window_spec_txn)).filter(col('row_num') == 1)
top_merchants_by_share = merchant_stats.withColumn('row_num', row_number().over(window_spec_share)).filter(col('row_num') == 1)

# Show results for top merchants by transactions and spend share
print("Merchant with Highest Transactions per Customer and Category:")
top_merchants_by_txn.select('card_number', 'merchant_catg', 'merchant_code', 'txn_count').show()

print("Merchant with Highest Spend Share per Customer and Category:")
top_merchants_by_share.select('card_number', 'merchant_catg', 'merchant_code', 'share_of_spend').show()

# Step 4: Find the most 'loyal' merchant in each category (highest total spend)
# Create window specification for highest total spend
window_spec_loyal = Window.partitionBy('merchant_catg').orderBy(col('total_spend').desc())

# Get the most loyal merchant (highest total spend) per category
most_loyal_merchants = merchant_spend.withColumn('row_num', row_number().over(window_spec_loyal)) \
    .filter(col('row_num') == 1)

# Show the most loyal merchants
print("Most Loyal Merchant per Category:")
most_loyal_merchants.select('merchant_catg', 'merchant_code', 'total_spend').show()
