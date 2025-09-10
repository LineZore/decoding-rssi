import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# 要绘制的距
target_distance=2
#要画的图，1是阴影图，2是每个标签的，3和4是9900的
draw_mod=1

plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['figure.figsize'] = [6, 5]
color_arr=['dodgerblue','forestgreen','darkorange','orchid','orange']
figure_path='./figure/'
reader_name=['R420','9900']
tag_name=['U8','R6P','9640']
distance=[2,3,4,5,6,7,8]
file_path="./data/"
line_arr=['-','--','-.',':']

target_ind=distance.index(target_distance)

x_R420=[10.0+i*0.25 for i in range(91)]
x_9900=range(15,31,1)

for tind in range(len(tag_name)):
    y_R420=[]
    y_9900=[]
    
    for rind in range(len(reader_name)):
        file_name = f"{reader_name[rind]}_{tag_name[tind]}.txt"
        
        dind=0
        with open(file_path+file_name, 'r') as file:
            
            for line in file:
                if line.strip() == '':
                    dind+=1
                    continue
                if dind==target_ind:
                    if reader_name[rind]=='R420':
                        y_R420.append( list(map(float,line.strip().split())))
                    elif reader_name[rind]=='9900':
                        y_9900.append( list(map(float,line.strip().split())))

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

    if len(y_min)==len(x_R420):
        plt.fill_between(x_R420, y_min, y_max, color='#ADD8E6', alpha=0.7)
        plt.plot(x_R420, y_mean, label='R420', color='#1f77b4', linewidth=3)

    # 9900 rssi_ptx 
    y_min=[]
    y_max=[]
    y_mean=[]
    try:
        y_min = np.nanmin(y_9900, axis=0)  
        y_max = np.nanmax(y_9900, axis=0)  
        y_mean = np.nanmean(y_9900, axis=0)  
    except ValueError: 
        result = np.nan  

    if len(y_min)==len(x_9900):
        plt.fill_between(x_9900, y_min, y_max, color='#2ca02c', alpha=0.3,edgecolor='none')
        plt.plot(x_9900, y_mean, label='9900', color='#2ca02c', linewidth=3,linestyle='--')

    plt.title(f"{tag_name[tind]}",fontsize=24)
    plt.xlabel("Transmit Power (dBm)",fontsize=26)
    plt.ylabel("RSSI (dBm)",fontsize=26)
    plt.tick_params(axis='both', labelsize=22)

    plt.xticks(np.arange(10, 32, 2))
    if tind==0:
        plt.yticks(np.arange(-60, -29, 5))
        plt.ylim([-60, -30])
    elif tind==1:
        plt.yticks(np.arange(-55, -20, 5))
        plt.ylim([-55, -25])
    elif tind==2:
        plt.yticks(np.arange(-58, -20, 5))
        plt.ylim([-58, -28])
    # plt.yticks(np.arange(-47, -33, 2))
    plt.xlim([10, 30])
    plt.grid(True)
    plt.tight_layout()
    plt.legend(fontsize=22)
    plt.savefig(f'{figure_path}figure12_{tag_name[tind]}.svg', format='svg')
    plt.show()
