from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Criando a SparkSession com suporte ao Kafka
spark = SparkSession.builder \
    .appName("LeituraKafka") \
    .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true") \
    .getOrCreate()

print("Spark version:", spark.version)

schema = StructType() \
    .add("currency", StringType()) \
    .add("price", DoubleType()) \
    .add("volume", DoubleType()) \
    .add("time", StringType()) 

def transform_crypto_prices():
    df_raw = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "crypto_prices") \
        .option("startingOffsets", "latest") \
        .load()

    df_json = df_raw.selectExpr("CAST(value AS STRING) as json")

    df_parsed = df_json.select(from_json(col("json"), schema).alias("data")).select("data.*")

    # Printar os dados no console
    query = df_parsed.writeStream \
        .outputMode("append") \
        .format("console") \
        .option("truncate", False) \
        .option("numRows", 1) \
        .option("checkpointLocation", "/tmp/spark-checkpoints/crypto-prices") \
        .start()

    print("🚀 Spark Streaming iniciado, aguardando dados...")
    query.awaitTermination()

if __name__ == "__main__":
    transform_crypto_prices()
