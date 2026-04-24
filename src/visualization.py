import matplotlib.pyplot as plt
import pandas as pd

def plot_results_final(data, anomalies, threshold_upper=60, threshold_lower=40):
    if data.empty:
        print("Warning: Data is empty.")
        return

    plt.figure(figsize=(12, 6))

    # 1. Plot the Main Pressure Line
    plt.plot(data["time"], data["pressure"], 
             label="Live Pressure", 
             color="#2c3e50", 
             linewidth=1.5, 
             alpha=0.7, 
             zorder=1)

    # 2. Add Threshold Lines (Horizontal)
    plt.axhline(y=threshold_upper, color="#c0392b", linestyle="--", 
                linewidth=1.5, label=f"Upper Limit ({threshold_upper})", zorder=2)
    plt.axhline(y=threshold_lower, color="#c0392b", linestyle="--", 
                linewidth=1.5, label=f"Lower Limit ({threshold_lower})", zorder=2)

    # 3. Fill the "Safe Operating Zone" with a light green tint
    plt.fill_between(data["time"], threshold_lower, threshold_upper, 
                     color="#27ae60", alpha=0.1, label="Safe Operating Range")

    # 4. Highlight Anomalies
    if anomalies is not None and len(anomalies) > 0:
        plt.scatter(
            data["time"].iloc[anomalies],
            data["pressure"].iloc[anomalies],
            label="Anomalies Detected",
            color="#e74c3c",
            edgecolor="black",
            s=80,
            zorder=4
        )

    # Professional Formatting
    plt.gcf().autofmt_xdate() # Auto-rotate date labels
    plt.xlabel("Timestamp")
    plt.ylabel("Pressure (PSI)")
    plt.title("Pipeline Monitoring: Pressure & Safety Thresholds", fontweight='bold')
    plt.grid(True, linestyle=":", alpha=0.6)
    
    # Place legend outside or in a clear corner
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.show()
