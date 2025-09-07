import numpy as np
import os
from matplotlib import pyplot as plt

#Reference distance for correcting RSSI
ref_dis=4
#Correct the RSSI at the target distance
target_dis=2

#选择阅读器，0是R420，1是9900
reader_cho=0
#
target_ptx=30

color_arr=['blue','green','red','purple','orange']
figure_path='./figure/'
reader_name=['R420','9900']
tag_name=['U8','R6P','9640']
distance=[2,3,4,5,6,7,8]
file_path="./data/"
line_arr=['-','--','-.',':']
ref_dis_ind=distance.index(ref_dis)
target_dis_ind=distance.index(target_dis)

output_path="./data/processed_data/"

if os.path.exists(output_path)==False:
    os.mkdir(output_path)

x_reader=[[10.0+i*0.25 for i in range(91)],range(15,31,1)]
target_ptx_ind=x_reader[reader_cho].index(target_ptx)

pj_error=[[] for i in range(len(tag_name))]
dis_error=[[] for i in range(len(tag_name))]

with open('./data/processed_data/rssi_cor_error.txt', 'w') as f:
    pass

for target_tag in range(5):

    for tind in range(len(tag_name)):
        tag_num=0
        data=[]
        file_name = f"{reader_name[reader_cho]}_{tag_name[tind]}.txt"
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
        k=[[] for i in range(tag_num)]
        b=[[] for i in range(tag_num)]
        pj=[[] for i in range(tag_num)]
        s_x=[[] for i in range(tag_num)]
        s_y=[[] for i in range(tag_num)]

        for i in range(len(data)):
            tag_data[i%tag_num].append(data[i])

        for i in range(tag_num):
            x=np.array(x_reader[reader_cho])
            y=np.array(tag_data[i][ref_dis_ind])
            
            mask = ~np.isnan(x) & ~np.isnan(y)

            x_clean = x[mask]
            y_clean = y[mask]

            coeffs = np.polyfit(x_clean, y_clean, 1)
            k[i],b[i]=coeffs
            
            pj[i]=x_clean[0]

            s_x[i]=x_clean
            s_y[i]=x_clean-k[i]*x_clean-b[i]+k[i]*x_clean[-1]+b[i]-x_clean[-1]

        
        rssi_fix=[]
        rssi_fix_z=[]
        for i in range(len(tag_data[target_tag])):
            rssi=np.array(tag_data[target_tag][i])
            ptx=np.array(x_reader[reader_cho])
            mask = ~np.isnan(ptx) & ~np.isnan(rssi)
            x_clean = ptx[mask]
            y_clean = rssi[mask]
            rssi_fix.append(y_clean+(1-k[target_tag])* x_clean-(1-k[target_tag])*x_clean[-1])
            rssi_fix_z.append(y_clean+(1-k[target_tag])* x_clean-(1-k[target_tag])*x_clean[0])
            # rssi_fix.append([y_clean[a]+s_y[target_tag][a] for a in range(len(y_clean))])
            

        rssi=np.array(tag_data[target_tag][target_dis_ind])
        ptx=np.array(x_reader[reader_cho])
        mask = ~np.isnan(ptx) & ~np.isnan(rssi)
        x_clean = ptx[mask]
        y_clean = rssi[mask]
        y_ref=x_clean-x_clean[-1]+y_clean[-1]
        # y_ref=x_clean-x_clean[0]+y_clean[0]

        plt.plot(x_clean, y_clean, label="RSSI", linewidth=2)
        
        with open("./data/processed_data/rssi_cor_error.txt", 'a') as file:
            mask = (x_clean>=20) & (x_clean<=30) & (x_clean%1==0)
            y_avg_values_str = ' '.join(map(str, x_clean[mask]))
            file.write(y_avg_values_str+'\n')
            y=y_clean-y_ref
            y_avg_values_str = ' '.join(map(str, y[mask]))
            y= rssi_fix[target_dis_ind]-y_ref
            file.write(y_avg_values_str+'\n')
            y_avg_values_str = ' '.join(map(str,y[mask]))
            file.write(y_avg_values_str+'\n')

