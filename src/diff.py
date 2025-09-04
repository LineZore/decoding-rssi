import numpy as np
import matplotlib.pyplot as plt

file_path="./data/"
figure_path='./figure/'
plt.rcParams['font.family'] = ['Times New Roman']
x_reader=[10.0+i*0.25 for i in range(91)]

labels=[ 'Outdoors', 'Lab', 'Office', 'Cup']
color_arr=['dodgerblue','forestgreen','darkorange','indianred','orange']
line_arr=['-','--','-.',':']
marker_arr=['o','s','^','v']
data=[]

with open(file_path+'diff.txt', 'r') as file:
    for line in file:
        if line.strip() != '':
            data.append( list(map(float,line.strip().split())))

for i in range(4):
    plt.plot(data[2*i][::5],data[2*i+1][::5],label=labels[i],color=color_arr[i],linestyle=line_arr[i],linewidth=3,marker=marker_arr[i],markersize=10, markeredgecolor=color_arr[i], markerfacecolor='none',markeredgewidth=2)


plt.xlabel(r"$\chi$ (dB)",fontsize=26)
plt.ylabel(r"h$(\chi)$ (dB)",fontsize=26)
plt.tick_params(axis='both', labelsize=22)
plt.grid(True)
plt.legend(fontsize=20)
plt.tight_layout()

plt.xticks(np.arange(0, 21, 2))
plt.xlim([0, 18])    
plt.yticks(np.arange(5, 66, 10))
plt.ylim([5, 65])
plt.savefig(f'{figure_path}figure10.svg', format='svg')
plt.show()
