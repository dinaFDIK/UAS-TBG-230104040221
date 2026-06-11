import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(
page_title="Smart Retail Visitor Prediction",
layout="wide"
)

st.title("🛍 Smart Retail Visitor Prediction System")

BASE_PATH = "/home/dinamuzaina/bigdata-project/uas-tbg-230104040221/output"

# ==========================

# Load Parquet

# ==========================

visitor_total = pd.read_parquet(
f"{BASE_PATH}/visitor_total"
)

visitor_time = pd.read_parquet(
f"{BASE_PATH}/visitor_time"
)

ml_visitor = pd.read_parquet(
f"{BASE_PATH}/ml_visitor"
)

# ==========================

# Sidebar Filter

# ==========================

zone = st.sidebar.selectbox(
"Pilih Zona",
visitor_total["zone"].unique()
)

# ==========================

# KPI Total Pengunjung

# ==========================

total = visitor_total[
visitor_total["zone"] == zone
]["total_visitor"].iloc[0]

st.metric(
label="Total Pengunjung",
value=int(total)
)

# ==========================

# Grafik Tren Pengunjung

# ==========================

st.subheader("Tren Pengunjung Tiap 15 Menit")

filtered_time = visitor_time[
visitor_time["zone"] == zone
]

fig1 = px.line(
filtered_time,
x="time_group",
y="visitor_count",
markers=True,
title=f"Tren Pengunjung - {zone}"
)

st.plotly_chart(fig1, use_container_width=True)

# ==========================

# Machine Learning

# ==========================

st.subheader("Prediksi Pengunjung Berdasarkan Jam")

filtered_ml = ml_visitor[
ml_visitor["zone"] == zone
].copy()

X = filtered_ml[["hour"]]
y = filtered_ml["visitor_count"]

model = LinearRegression()
model.fit(X, y)

filtered_ml["prediction"] = model.predict(X)

fig2 = px.scatter(
filtered_ml,
x="hour",
y="visitor_count",
title=f"Prediksi Pengunjung - {zone}"
)

fig2.add_scatter(
x=filtered_ml["hour"],
y=filtered_ml["prediction"],
mode="lines",
name="Linear Regression"
)

st.plotly_chart(fig2, use_container_width=True)

peak_hour = filtered_ml.loc[
filtered_ml["visitor_count"].idxmax(),
"hour"
]

st.success(
f"Jam sibuk pengunjung diperkirakan pada pukul {peak_hour}:00"
)
