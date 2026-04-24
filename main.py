from src.simulator import simulate_pipeline_data
from src.detector import (
    detect_anomalies_zscore,
    detect_anomalies_ai,
    detect_anomalies_threshold
)
from src.visualization import plot_results_final


def main():
    # Step 1: Generate simulated pipeline data
    data = simulate_pipeline_data(
        n_points=200,
        save_path="data/simulated_pipeline_data.csv"
    )
    # Step 2: Choose detection method

    # OPTION 1: Engineering view (matches your plot best)
    anomalies = detect_anomalies_threshold(
        data,
        upper=60,
        lower=40
    )

    # OPTION 2: AI view (advanced alternative)
    # anomalies = detect_anomalies_ai(data)

    # OPTION 3: Statistical view
    # anomalies = detect_anomalies_zscore(data)

    # Step 3: Visualization
    plot_results_final(
        data,
        anomalies,
        threshold_upper=60,
        threshold_lower=40
    )

    print(f"Total anomalies detected: {len(anomalies)}")


if __name__ == "__main__":
    main()
