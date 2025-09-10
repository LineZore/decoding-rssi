import numpy as np
import matplotlib.pyplot as plt

# Target distance
target_dis=2
# Target transmit power
line_ptx=25

plt.rcParams['font.family'] = ['Times New Roman']

color_arr=['red','yellow','orange','green','blue']
figure_path='./figure/'
reader_name=['R420','9900']
tag_name=['H47','R6P','9640']
distance=[1,2,3,4,6,8,9]
file_path="./data/"
marker_arr=['o','s','v','^','*','>']
target_dis_ind=distance.index(target_dis)

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
x=np.array(x_reader[0])
y=np.array(tag_data[1][target_dis_ind])

mask = ~np.isnan(x) & ~np.isnan(y)
x_clean = x[mask]
y_clean = y[mask]
pj=x_clean[0]

y_clean=-y_clean-x_clean
x_begin=x_clean[0]
x_clean=x_clean-x_begin

# plt.scatter(x_clean, y_clean,marker='^',s=40,color='darkorange',zorder=2)
plt.plot(x_clean, y_clean,marker='^',markersize=7, linewidth=3,zorder=1)


highlight_x=line_ptx-pj
highlight_y=y_clean[np.where(x_clean==highlight_x)[0]][0]


plt.axvline(x=highlight_x, color='darkorange', linestyle='--', linewidth=3,zorder=1)  # 
plt.axhline(y=highlight_y, color='g', linestyle='--', linewidth=3,zorder=1)  # 


plt.scatter(highlight_x, highlight_y, color='r',s=75,zorder=3)  # 
plt.text(highlight_x+0.2, highlight_y+0.4, f'({highlight_x}, {highlight_y:.0f})', color='black', fontsize=22,  ha='left')  # 在点旁边标注数据

# plt.text(0, 0, f'{pj}dBm', color='black', fontsize=16,  ha='center',alpha=0.8)
# plt.bar(x_clean[::2],y_clean[::2],width=0.4,color='#1f77b4',alpha=0.8)

plt.xticks(np.arange(0, 16, 2))
plt.yticks(np.arange(14, 35, 5))
plt.xlim([0, 12])
plt.ylim([14, 34])

plt.xlabel(r"$\chi$ (dB)",fontsize=26)
plt.ylabel(r"h($\chi$) (dB)",fontsize=26)
plt.tick_params(axis='both', labelsize=22)
plt.grid(True)
plt.tight_layout()
plt.savefig(f'{figure_path}figure9.svg', format='svg')
    
# plt.title(f"{tag_name[0]}",fontsize=18)
# plt.xlabel(r"$P_{tx}-P_{tx}^{min}$ (dB)",fontsize=18)
# plt.ylabel(r"$-RSSI-P_{tx}^{[dBm]}$ (dB)",fontsize=18)
plt.show() 
