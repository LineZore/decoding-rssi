import numpy as np
from matplotlib import pyplot as plt

file_path="./data/processed_data/itp/"
figure_path='./figure/'

tag_name=['R6P','U8','9640']
figure_letter=['a','b','c']
color_array=['#4586BD','#D13C3C','#55AC3D']
label_name=['3m','4m','5m']
line_type=['-','-.',':']
plt.rcParams['font.family'] = ['Times New Roman']

for tind in range(len(tag_name)):
    file_name = f"{tag_name[tind]}.txt"
    data=[]
    with open(file_path+file_name, 'r') as file:
        for line in file:
            if line.strip() != '':
                data.append( list(map(float,line.strip().split())))

    for i in range(len(data)):
        x = np.sort(data[i])
        y = np.arange(1, len(x)+1) / len(x)
        plt.step(x, y,color=color_array[i],label=label_name[i],linewidth=4,linestyle=line_type[i])


    plt.xlabel('Error(dB)',fontsize=26)
    plt.ylabel('CDF',fontsize=26)
    plt.grid(True)
    plt.grid(which="both",alpha=0.4)
    plt.tick_params(axis='both', labelsize=26)
    plt.xticks(np.arange(0, 3.1, 0.3),minor=True)
    plt.xticks(np.arange(0, 3.1, 0.6))
    plt.xlim([0, 3])    
    plt.yticks(np.arange(0, 1.1, 0.2))
    plt.ylim([0, 1])
    plt.legend(fontsize=26)
    plt.tight_layout()

    plt.savefig(f'{figure_path}figure17_{figure_letter[tind]}.svg', format='svg')
    plt.show()