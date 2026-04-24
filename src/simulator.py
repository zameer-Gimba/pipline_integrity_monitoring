import numpy as np
import pandas as pd

def simulate_pipeline_data(n_points=200, save_path=None):
    np.random.seed(42)

    time = np.arange(n_points)

    # Normal pressure
    pressure = np.random.normal(loc=110, scale=5, size=n_points)

    # Leak event
    leak_start, leak_end = 80, 100
    pressure[leak_start:leak_end] = np.random.normal(loc=70, scale=5, size=(leak_end - leak_start))

    # Gradual corrosion
    for i in range(120, n_points):
        pressure[i] -= (i - 120) * 0.2

    data = pd.DataFrame({
        "time": time,
        "pressure": pressure
    })

    if save_path:
        data.to_csv(save_path, index=False)

    return data
