import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12

def plot_tag(tag_name, save=True):
    """
    tag_name: "U8", "R6P", "9640"
    """

    df = pd.read_csv(f"./data/processed_data/csv/Fig14_{tag_name}.csv")


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


    plt.xlabel('Transmit Power (dBm)', fontweight='bold')
    plt.ylabel('Error (dB)', fontweight='bold')
    plt.xticks(x_pos, df['Distance'])
    plt.grid(True, alpha=0.3, axis='y')
    plt.legend()
    plt.title(f"Fig14 - {tag_name}", fontweight='bold')


    plt.yticks(np.arange(0, 7, 1))
    plt.tight_layout()


    if save:
        plt.savefig(f"./figure/figure14_{tag_name}.svg", dpi=300, bbox_inches='tight')
    plt.show()



for tag in ["U8", "R6P", "9640"]:
    plot_tag(tag)
