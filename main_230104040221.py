from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, hour, minute, floor, concat_ws
from datetime import datetime, timedelta
import random

# Spark Session
spark = SparkSession.builder \
    .appName("Retail Visitor Prediction") \
    .getOrCreate()

# Generate Data
zones = ["FoodCourt", "FashionArea", "Cinema"]

data = []

start_time = datetime.now()

for i in range(180):
    for zone in zones:
        data.append((
            start_time + timedelta(minutes=i),
            zone,
            random.randint(10, 500)
        ))

df = spark.createDataFrame(
    data,
    ["timestamp", "zone", "visitor_count"]
)

# ==================================
# Total Pengunjung per Zona
# ==================================
visitor_total = df.groupBy("zone") \
    .agg(sum("visitor_count").alias("total_visitor"))

# ==================================
# Tren Pengunjung per 15 Menit
# ==================================
visitor_time = df.withColumn(
    "time_group",
    concat_ws(
        ":",
        hour("timestamp"),
        floor(minute("timestamp") / 15) * 15
    )
)

visitor_time = visitor_time.groupBy(
    "zone",
    "time_group"
).agg(
    sum("visitor_count").alias("visitor_count")
)

# ==================================
# Dataset AI
# ==================================
ml_visitor = df.withColumn(
    "hour",
    hour("timestamp")
)

ml_visitor = ml_visitor.groupBy(
    "zone",
    "hour"
).agg(
    sum("visitor_count").alias("visitor_count")
)

BASE_PATH = "/home/dinamuzaina/bigdata-project/uas-tbg-230104040221/output"

visitor_total.write.mode("overwrite").parquet(
    f"{BASE_PATH}/visitor_total"
)

visitor_time.write.mode("overwrite").parquet(
    f"{BASE_PATH}/visitor_time"
)

ml_visitor.write.mode("overwrite").parquet(
    f"{BASE_PATH}/ml_visitor"
)

print("PARQUET BERHASIL DIBUAT")

spark.stop()
