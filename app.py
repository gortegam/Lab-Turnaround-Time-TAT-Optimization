import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/lab_events.csv", parse_dates=[
        "collection_time","receipt_time","start_analysis_time","verification_time","report_time"
    ])

df = load_data()

st.title("🏥 Lab Turnaround Time Optimization")

# ======================
# Sidebar Filters
# ======================
st.sidebar.header("🔎 Filters")

test_filter = st.sidebar.multiselect(
    "Test Type", options=df["test_code"].unique(), default=list(df["test_code"].unique())
)

shift_filter = st.sidebar.multiselect(
    "Shift", options=df["shift"].unique(), default=list(df["shift"].unique())
)

priority_filter = st.sidebar.multiselect(
    "Priority", options=df["priority"].unique(), default=list(df["priority"].unique())
)

# Apply filters
filtered_df = df[
    df["test_code"].isin(test_filter) &
    df["shift"].isin(shift_filter) &
    df["priority"].isin(priority_filter)
]

# ======================
# KPI Calculations
# ======================
filtered_df["tat_total"] = (filtered_df["report_time"] - filtered_df["collection_time"]).dt.total_seconds()/60

median_tat = filtered_df["tat_total"].median()
p95_tat = np.percentile(filtered_df["tat_total"], 95)
sla_rate = (filtered_df["tat_total"] <= filtered_df["sla_min"]).mean() * 100

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Median TAT (min)", f"{median_tat:.1f}")
col2.metric("95th Percentile TAT (min)", f"{p95_tat:.1f}")
col3.metric("SLA Hit Rate", f"{sla_rate:.1f}%")

# ======================
# Grouped Tables & Charts
# ======================

# By Test
st.subheader("TAT by Test")
by_test = filtered_df.groupby("test_code").agg(
    n=("order_id","count"),
    tat_median=("tat_total","median"),
    tat_p95=("tat_total", lambda x: np.percentile(x,95)),
    sla_hit_rate=("sla_hit","mean")
).reset_index()

st.dataframe(by_test.style.format({
    "tat_median":"{:.1f}",
    "tat_p95":"{:.1f}",
    "sla_hit_rate":"{:.1%}"
}))

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(by_test["test_code"], by_test["tat_median"], color="skyblue", label="Median TAT")
ax.bar(by_test["test_code"], by_test["tat_p95"], color="lightcoral", alpha=0.6, label="95th pct TAT")
ax.set_ylabel("TAT (minutes)")
ax.set_title("TAT by Test")
ax.legend()
st.pyplot(fig)

# By Shift
st.subheader("TAT by Shift")
by_shift = filtered_df.groupby("shift").agg(
    n=("order_id","count"),
    tat_median=("tat_total","median"),
    sla_hit_rate=("sla_hit","mean")
).reset_index()
st.dataframe(by_shift)

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(by_shift["shift"], by_shift["tat_median"], color="mediumseagreen")
ax.set_ylabel("Median TAT (minutes)")
ax.set_title("Median TAT by Shift")
st.pyplot(fig)

# By Priority
st.subheader("TAT by Priority")
by_priority = filtered_df.groupby("priority").agg(
    n=("order_id","count"),
    tat_median=("tat_total","median"),
    sla_hit_rate=("sla_hit","mean")
).reset_index()
st.dataframe(by_priority)

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(by_priority["priority"], by_priority["tat_median"], color="orange")
ax.set_ylabel("Median TAT (minutes)")
ax.set_title("Median TAT by Priority")
st.pyplot(fig)

# ======================
# Time Trend
# ======================
st.subheader("Daily Median TAT Over Time")
by_day = filtered_df.groupby(filtered_df["receipt_time"].dt.date).agg(
    tat_median=("tat_total","median"),
    sla_hit_rate=("sla_hit","mean")
).reset_index()

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(by_day["receipt_time"], by_day["tat_median"], marker="o", label="Median TAT")
ax.set_ylabel("Median TAT (minutes)")
ax.set_xlabel("Date")
ax.set_title("Daily Median TAT Trend")
ax.grid(True)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10,4))
ax.plot(by_day["receipt_time"], by_day["sla_hit_rate"]*100, marker="o", color="purple", label="SLA Hit Rate")
ax.set_ylabel("SLA Hit Rate (%)")
ax.set_xlabel("Date")
ax.set_ylim(0, 100)
ax.set_title("Daily SLA Compliance Trend")
ax.grid(True)
st.pyplot(fig)

st.markdown("✅ Use the sidebar to filter by test, shift, and priority.")
