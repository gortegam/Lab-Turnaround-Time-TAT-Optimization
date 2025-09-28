import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data():
    return pd.read_csv("data/lab_events.csv", parse_dates=[
        "collection_time","receipt_time","start_analysis_time","verification_time","report_time"
    ])

df = load_data()

st.title("🏥 Lab Turnaround Time Optimization")

# KPIs
df["tat_total"] = (df["report_time"] - df["collection_time"]).dt.total_seconds()/60
st.metric("Median TAT (min)", f"{df['tat_total'].median():.1f}")
st.metric("95th Percentile TAT (min)", f"{np.percentile(df['tat_total'],95):.1f}")

by_test = df.groupby("test_code").agg(
    n=("order_id","count"),
    tat_median=("tat_total","median"),
    tat_p95=("tat_total", lambda x: np.percentile(x,95))
).reset_index()

st.subheader("TAT by Test")
st.dataframe(by_test)
