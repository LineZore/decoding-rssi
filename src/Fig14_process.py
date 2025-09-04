import pandas as pd
import numpy as np


with open("./data/processed_data/rssi_cor_error.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

distances = [20,21,22,23,24,25,26,27,28,29,30]


data_lines = [line for line in lines if not line.startswith("20.0")]


groups = [data_lines[i:i+2] for i in range(0, len(data_lines), 2)]

tags = ["U8", "R6P", "9640"]

for tag_index, tag in enumerate(tags):
    # 
    rows = []
    for idx, dist in enumerate(distances):
        
        rssi_vals = []
        rssi_fix_vals = []
        for g in range(5):  
            RSSI = list(map(float, groups[g*3+tag_index][0].split()))
            RSSI_fix = list(map(float, groups[g*3+tag_index][1].split()))
            rssi_vals.append(abs(RSSI[idx]))
            rssi_fix_vals.append(abs(RSSI_fix[idx]))

        
        rssi_vals = np.round(rssi_vals, 2)
        rssi_fix_vals = np.round(rssi_fix_vals, 2)

        
        mean_rssi = np.round(np.mean(rssi_vals), 3)
        std_rssi = np.round(np.std(rssi_vals, ddof=0), 6)
        mean_rssi_fix = np.round(np.mean(rssi_fix_vals), 3)
        std_rssi_fix = np.round(np.std(rssi_fix_vals, ddof=0), 6)

        row = [dist] + list(rssi_vals) + list(rssi_fix_vals) + [mean_rssi, std_rssi, mean_rssi_fix, std_rssi_fix]
        rows.append(row)

    
    columns = ["Distance"] \
              + [f"RSSI_{i+1}" for i in range(5)] \
              + [f"RSSI_fix_{i+1}" for i in range(5)] \
              + ["Mean_RSSI", "Std_RSSI", "Mean_RSSI_fix", "Std_RSSI_fix"]

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(f"./data/processed_data/csv/Fig14_{tag}.csv", index=False)