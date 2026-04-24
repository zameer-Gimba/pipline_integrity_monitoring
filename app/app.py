import streamlit as st
from src.simulator import simulate_pipeline_data
from src.detector import detect_anomalies_zscore, detect_anomalies_ai
import matplotlib.pyplot as plt

st.title("Pipeline Integrity Monitoring System")

# Generate data
data = simulate_pipeline_data(n_points=200)

method = st.selectbox(
    "Choose detection method",
    ["Z-Score (Statistical)", "AI (Isolation Forest)"]
)

# Detect anomalies
if method == "Z-Score (Statistical)":
    anomalies = detect_anomalies_zscore(data)
else:
    anomalies = detect_anomalies_ai(data)

# Plot
fig, ax = plt.subplots()
ax.plot(data["time"], data["pressure"], label="Pressure")

if len(anomalies) > 0:
    ax.scatter(
        data["time"].iloc[anomalies],
        data["pressure"].iloc[anomalies],
        color="red",
        label="Anomalies"
    )

ax.set_xlabel("Time")
ax.set_ylabel("Pressure")
ax.legend()

st.pyplot(fig)

st.write(f"Detected anomalies: {len(anomalies)}")
