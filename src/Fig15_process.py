import pandas as pd
import numpy as np

with open("./data/processed_data/rssi_cor_dis_error.txt", "r") as f:   # 换成你的文件名
    lines = [line.strip() for line in f if line.strip()]

distances = [3,4,5,6,7,8]

data_lines = [line for line in lines if not line.startswith("3 ")]

groups = [data_lines[i:i+2] for i in range(0, len(data_lines), 2)]

tags = ["U8", "R6P", "9640"]

for tag_index, tag in enumerate(tags):
    rows = []
    for idx, dist in enumerate(distances):
        rssi_vals = []
        rssi_fix_vals = []

        num_rounds = len(groups) // 3
        for g in range(num_rounds):
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

        row = [dist] + list(rssi_vals) + list(rssi_fix_vals) + \
              [mean_rssi, std_rssi, mean_rssi_fix, std_rssi_fix]
        rows.append(row)

    columns = ["Distance"] \
              + [f"RSSI_{i+1}" for i in range(len(rssi_vals))] \
              + [f"RSSI_fix_{i+1}" for i in range(len(rssi_fix_vals))] \
              + ["Mean_RSSI", "Std_RSSI", "Mean_RSSI_fix", "Std_RSSI_fix"]

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(f"./data/processed_data/csv/Fig15_{tag}.csv", index=False)
