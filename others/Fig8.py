import numpy as np
import matplotlib.pyplot as plt
import math

plt.rcParams['font.family'] = ['Times New Roman']

color_arr=['red','yellow','orange','green','blue']
figure_path='./figure/'
reader_name=['R420','9900']
tag_name=['H47','R6P','9640']
distance=[1,2,3,4,6,8,9]
file_path="./data/"
marker_arr=['o','s','v','^','*','>']

x_reader=[[10.0+i*0.25 for i in range(91)],range(15,31,1)]


tag_num=0
data=[]
file_name = f"{reader_name[0]}_{tag_name[0]}.txt"
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

pj=[math.nan for i in range(len(distance))]
for i in range(len(tag_data[0])):
    x=np.array(x_reader[0])
    y=np.array(tag_data[0][i])
    # 
    mask = ~np.isnan(x) & ~np.isnan(y)
    x_clean = x[mask]
    y_clean = y[mask]

    y_clean=-y_clean-x_clean
    x_begin=x_clean[0]
    x_clean=x_clean-x_begin
    pj[i]=y_clean[0]
    # plt.plot(x_clean, y_clean, label=f'{distance[i]}m', linewidth=2,marker=marker_arr[i],markersize=4)


x=np.array(distance)
y=np.array(pj)
mask = ~np.isnan(x) & ~np.isnan(y)
x_clean = x[mask]
y_clean = y[mask]
#Supplementary measurements were taken for 5m and 7m
x_clean=np.append(x_clean,5)
y_clean=np.append(y_clean,30.71)
x_clean=np.append(x_clean,7)
y_clean=np.append(y_clean,29.48)
stdev=np.array([1.2470038,0.733570038,0.291547595,0.614662442,0.533853913,0.857321409,0.956556323,0.85732141])
# x_clean=list(map(str, x_clean))
plt.bar(x_clean,y_clean,yerr=stdev, capsize=5,alpha=0.8, zorder=3)
# plt.legend(fontsize=16)
plt.xticks(np.arange(1, 9, 1))
# plt.yticks(np.arange(0, 36, 5))
# plt.xlim([0, 18])
# plt.ylim([0, 35])
plt.grid(True, zorder=1)
plt.xlabel("Distance (m)",fontsize=26)
plt.ylabel("h(0) (dB)",fontsize=26)
plt.tick_params(axis='both', labelsize=22)

plt.tight_layout()
plt.savefig(f'{figure_path}figure8.svg', format='svg')

plt.show()