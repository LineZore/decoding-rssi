import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Target transmit power
R420_target_ptx=30
F9900_target_ptx=30

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['figure.figsize'] = [6, 5]
color_arr=['dodgerblue','forestgreen','darkorange','orchid','orange']
figure_path='./figure/'
reader_name=['R420','9900']
tag_name=['U8','R6P','9640']
distance=[2,3,4,5,6,7,8]
file_path="./data/"
line_arr=['-','--','-.',':']

x_R420=[10.0+i*0.25 for i in range(91)]
x_F9900=range(15,31,1)

target_ind_R420=x_R420.index(R420_target_ptx)
target_ind_F9900=x_F9900.index(F9900_target_ptx)

for tind in range(len(tag_name)):
    y_R420=[[np.nan for j in range(len(distance))] for i in range(5)]
    y_F9900=[[np.nan for j in range(len(distance))] for i in range(5)]
    
    for rind in range(len(reader_name)):
        file_name = f"{reader_name[rind]}_{tag_name[tind]}.txt"
        with open(file_path+file_name, 'r') as file:
            i=0
            dind=0
            for line in file:
                if line.strip() == '':
                    dind+=1
                    i=0
                    continue
                
                if reader_name[rind]=='R420':
                    y_R420[i][dind]=(list(map(float,line.strip().split()))[target_ind_R420])
                elif reader_name[rind]=='9900':
                    y_F9900[i][dind]=(list(map(float,line.strip().split()))[target_ind_F9900])
                
                i+=1
    
    # plt.figure(tind)
    plt.clf()
    
    y_min=[]
    y_max=[]
    y_mean=[]
    try:
        y_min = np.nanmin(y_R420, axis=0)  
        y_max = np.nanmax(y_R420, axis=0)  
        y_mean = np.nanmean(y_R420, axis=0)  

    except ValueError:  
        result = np.nan  

    # if len(y_min)==len(distance):
    plt.fill_between(distance, y_min, y_max, color='#1f77b4', alpha=0.3,edgecolor='none')
    plt.plot(distance, y_mean, label='R420', color='#1f77b4', linewidth=3)


    y_min=[]
    y_max=[]
    y_mean=[]
    try:
        y_min = np.nanmin(y_F9900, axis=0)  
        y_max = np.nanmax(y_F9900, axis=0)  
        y_mean = np.nanmean(y_F9900, axis=0) 
    except ValueError:  
        result = np.nan  
    # if len(y_min)==len(distance):
    plt.fill_between(distance, y_min, y_max, color='#2ca02c', alpha=0.3,edgecolor='none')
    plt.plot(distance, y_mean, label='9900', color='#2ca02c', linewidth=3,linestyle='--')

    plt.title(f"{tag_name[tind]}",fontsize=24)
    plt.xlabel("Distance (m)",fontsize=26)
    plt.ylabel("RSSI (dBm)",fontsize=26)
    plt.tick_params(axis='both', labelsize=22)
    plt.xticks(np.arange(1, 9, 1))
    plt.xlim([2, 8])
    
    # plt.xticks(np.arange(14, 32, 2))
    if tind==0:
        plt.yticks(np.arange(-65, -25, 5))
    elif tind==1:
        plt.yticks(np.arange(-60, -20, 5))
        plt.ylim([-60, -25])
    elif tind==2:
        plt.yticks(np.arange(-63, -23, 5))
        plt.ylim([-63, -28])
    # plt.xlim([14, 30])
    plt.grid(True)
    plt.tight_layout()
    plt.legend(fontsize=22)
    plt.savefig(f'{figure_path}figure13_{tag_name[tind]}.svg', format='svg',bbox_inches='tight')
    plt.show()
    