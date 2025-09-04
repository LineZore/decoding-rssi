import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12

def plot_fig15(tag_name, save=True):
    """
    绘制 Fig15 的 RSSI vs RSSI_fix 校正误差对比图
    tag_name: "U8", "R6P", "9640"
    """
    df = pd.read_csv(f"./data/processed_data/csv/Fig15_{tag_name}.csv")

    plt.figure(figsize=(8, 6))

    color_before = 'teal'     
    color_after = 'gold'     

    x_pos = np.arange(len(df))
    bar_width = 0.35

    # RSSI
    plt.bar(x_pos - bar_width/2, df['Mean_RSSI'], bar_width,
            yerr=df['Std_RSSI'], capsize=4,
            color=color_before, label='RSSI', alpha=0.8, edgecolor='black')

    # RSSI_fix
    plt.bar(x_pos + bar_width/2, df['Mean_RSSI_fix'], bar_width,
            yerr=df['Std_RSSI_fix'], capsize=4,
            color=color_after, label='RSSI_fix', alpha=0.8, edgecolor='black')

    plt.xlabel('Distance (m)', fontweight='bold')
    plt.ylabel('Error (dB)', fontweight='bold')
    plt.xticks(x_pos, df['Distance'])
    plt.grid(True, alpha=0.3, axis='y')
    plt.legend(loc="upper left")
    plt.title(f"Fig15 - {tag_name}", fontweight='bold')

    plt.ylim(0, max(df['Mean_RSSI'].max(), df['Mean_RSSI_fix'].max()) * 1.1)

    plt.yticks(np.arange(0, 6, 1))
    plt.tight_layout()

    if save:
        plt.savefig(f"./figure/figure15_{tag_name}.svg", dpi=300, bbox_inches='tight')
    plt.show()


# plot_fig15("R6P")

for tag in ["U8", "R6P", "9640"]:
    plot_fig15(tag)
