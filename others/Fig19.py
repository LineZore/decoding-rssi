import math
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Times New Roman']

# Target distance
target_dis=2

color_arr=['dodgerblue','forestgreen','darkorange','orchid','orange']
figure_path='./figure/'
reader_name=['R420','9900']
tag_name=['U8','R6P','9640']
distance=[2,3,4,5,6,7,8]
file_path="./data/"
marker_arr=['o','s','v','^','*','>','<']
line_arr=['-','--','-.',':']
target_dis_ind=distance.index(target_dis)

x_reader=[[10.0+i*0.25 for i in range(91)],range(15,31,1)]

for tag_cho in range(3):
    tag_num=0
    data=[]
    file_name = f"{reader_name[0]}_{tag_name[tag_cho]}.txt"
    with open(file_path+file_name, 'r') as file:
        tag_num_t=0
        for line in file:
            if line.strip() != '':
                
                data.append( list(map(float,line.strip().split())))
                tag_num_t+=1
            else :
                tag_num=max(tag_num,tag_num_t)
                tag_num_t=0

    tag_data=[[] for i in range(tag_num)]
    for i in range(len(data)):
        tag_data[i%tag_num].append(data[i])



    plt.clf()
    # plt.rcParams['figure.figsize'] = [4.2, 3.6]
    for i in range(tag_num-1):
        x=np.array(x_reader[0])
        y=np.array(tag_data[i][target_dis_ind])
        
        mask = ~np.isnan(x) & ~np.isnan(y)
        x_clean = x[mask]
        y_clean = y[mask]

        y_clean=-y_clean-x_clean
        x_begin=x_clean[0]
        x_clean=x_clean-x_begin

        plt.plot(x_clean, y_clean, label=f'Tag{i+1}', color=color_arr[i],linestyle=line_arr[i],linewidth=3)

    plt.title(f"{tag_name[tag_cho]}",fontsize=18)
    plt.xlabel(r"$\chi$ (dB)",fontsize=26)
    plt.ylabel(r"h($\chi$) (dB)",fontsize=26)
    plt.tick_params(axis='both', labelsize=26)
    if tag_cho==0:
        plt.yticks(np.arange(2, 45, 6))
        plt.ylim([2, 44])
    elif tag_cho==1:
        plt.yticks(np.arange(0, 45, 6))
        plt.ylim([0, 42])
    elif tag_cho==2:
        plt.yticks(np.arange(2, 45, 6))
        plt.ylim([2, 44])

    plt.xticks(np.arange(0, 21, 2))
    plt.xlim([0, 20])
    plt.grid(True)


    legend = plt.legend(fontsize=22)

    legend.get_frame().set_linewidth(1)  
    legend.get_frame().set_edgecolor('black')

    plt.tight_layout()

    plt.savefig(f'{figure_path}figure19_{tag_name[tag_cho]}.svg', format='svg')
    plt.show() 
