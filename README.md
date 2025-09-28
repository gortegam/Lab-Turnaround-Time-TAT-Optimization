# Lab Turnaround Time Optimization

## Overview
This project analyzes **laboratory turnaround time (TAT)** across pre-analytical, analytical, and post-analytical stages.  
Goal: identify bottlenecks, quantify SLA compliance, and recommend optimization strategies.

## Data
- **File:** `data/lab_events.csv`  
- **Synthetic structure:** order_id, patient_id, test_code, test_name, priority, bench, instrument_id, collector_id, accessioner_id, technologist_id, collection_time, receipt_time, start_analysis_time, verification_time, report_time, canceled, recollect_flag, weekday, shift

## Key KPIs
- Total TAT (collection → report)
- SLA hit rate (by test type)
- Stage contributions (pre/analytical/post)
- 95th percentile TAT by test
- Bench & shift comparisons

## Repo Structure
- `data/` → synthetic dataset
- `notebooks/` → Jupyter notebooks
- `app.py` → Streamlit dashboard
- `requirements.txt`

## Next Steps
1. Run `notebooks/01_eda_tat_baseline.ipynb` for baseline metrics.
2. Deploy `app.py` on Streamlit Cloud for interactive dashboards.
3. Extend analysis with bottleneck/root cause notebooks.
