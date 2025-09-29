# 🏥 Lab Turnaround Time Optimization

## 📌 Overview
Laboratory turnaround time (TAT) is one of the most critical performance metrics for clinical labs.  
This project analyzes **synthetic lab workflow data** to identify bottlenecks across pre-analytical, analytical, and post-analytical stages.  
The goal is to **reduce delays, improve SLA compliance, and optimize resource allocation**.

## 📂 Dataset
- **File:** `data/lab_events.csv`  
- **Size:** ~20,000 synthetic lab events  
- **Columns include:**  
  - Patient/test info (`order_id`, `patient_id`, `test_code`, `priority`)  
  - Workflow stages (`collection_time`, `receipt_time`, `start_analysis_time`, `verification_time`, `report_time`)  
  - Operational context (`bench`, `instrument_id`, `shift`, `weekday`)  
  - QA indicators (`canceled`, `recollect_flag`)  

> 🔒 Note: This dataset is synthetic and safe to share publicly. In practice, the same analysis can be applied to real, de-identified lab data.

## 📊 Key Metrics
- **Total TAT**: collection → report  
- **Stage TATs**: pre-analytical, analytical, post-analytical  
- **SLA hit rate**: % of tests meeting defined TAT thresholds  
- **95th percentile TAT**: robust measure of outliers  
- **Shift/bench comparisons**: where bottlenecks occur  

## 🚀 Usage

### Run Locally
```bash
git clone https://github.com/gortegam/lab-tat-optimization.git
cd lab-tat-optimization
pip install -r requirements.txt
streamlit run app.py
The dashboard will launch at **http://localhost:8501**

### Live Demo
👉 [**Try the Streamlit Dashboard**](https://gortegam-lab-tat-optimization.streamlit.app)

*(If inactive, fork this repo and deploy on your own Streamlit Cloud account.)*

---

## 📈 Dashboard Features
- **Filters:** by test type, shift, and priority  
- **KPIs:** Median TAT, 95th percentile TAT, SLA hit rate  
- **Breakdowns:**  
  - TAT by test (median vs 95th percentile)  
  - TAT by shift  
  - TAT by priority  
- **Trends:**  
  - Daily median TAT over time  
  - Daily SLA compliance rate  

---

## 📑 Repo Structure
```
lab-tat-optimization/
├─ data/
│  └─ lab_events.csv            # synthetic dataset
├─ notebooks/
│  └─ 01_eda_tat_baseline.ipynb # baseline EDA & bottleneck analysis
├─ app.py                       # Streamlit dashboard
├─ requirements.txt
└─ README.md
```

---

## 🔍 Preliminary Insights (from synthetic dataset)
- CBC and CMP tests show **shorter TATs** (median <2h) vs Pathology Review (median ~2 days).  
- **Evening shift** experiences the highest delays (median TAT ↑ 20% vs Day).  
- **STAT requests** cut pre-analytical time in half, but increase routine backlog.  
- **Instrument InstC** has a higher cancellation rate, contributing to TAT outliers.  

*(Replace with real findings as analysis progresses.)*

---

## 🛠️ Next Steps
- Add root cause analysis (bench & instrument level).  
- Simulate staffing changes (queueing model).  
- Generate optimization recommendations (e.g., shift coverage adjustments).  

---

## 📜 License
This project is released under the MIT License.  
