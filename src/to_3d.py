import numpy as np
import os
import math

#Reference distance for estimating ITP using in-situ method
ref_itp=2
#Reference distance for estimating distance using ITP-based method
ref_dis=4
#Target tag, select one of the five tags of the same type, range 0-4
target_tag=0
#Choose whether to update RSSI distance data
rssi_cor_dis_option=1

figure_path='./figure/'
file_path="./data/"
output_path="./data/processed_data/"

if os.path.exists(output_path)==False:
    os.mkdir(output_path)
    
if os.path.exists(output_path+"itp/")==False:
    os.mkdir(output_path+"itp")

if os.path.exists(output_path+"dis/")==False:
    os.mkdir(output_path+"dis")

if os.path.exists(output_path+"3d/")==False:
    os.mkdir(output_path+"3d")

if os.path.exists(output_path+"csv/")==False:
    os.mkdir(output_path+"csv")

color_arr=['red','yellow','orange','green','blue']
reader_name='R420'
tag_name=['U8','R6P','9640']
distance=[2,3,4,5,6,7,8]
ref_itp_ind=distance.index(ref_itp)
ref_dis_ind=distance.index(ref_dis)

x_reader=[10.0+i*0.25 for i in range(91)]

pj_error=[[] for i in range(len(tag_name))]
dis_error=[[] for i in range(len(tag_name))]
if rssi_cor_dis_option==1:
    with open('./data/processed_data/rssi_cor_dis_error.txt', 'w') as f:
        pass

for ttag in range(5):
    for tind in range(len(tag_name)):
        tag_num=0
        data=[]
        file_name = f"{reader_name}_{tag_name[tind]}.txt"
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

        for i in range(len(data)):
            tag_data[i%tag_num].append(data[i])
            
        for i in range(tag_num):
            x=np.array(x_reader)
            y=np.array(tag_data[i][ref_itp_ind])
            
            mask = ~np.isnan(x) & ~np.isnan(y)

            x_clean = x[mask]
            y_clean = y[mask]
            pj[i]=x_clean[0]

        pj_mean=[[] for i in range(len(distance))]
        dis_mean=[[] for i in range(len(distance))]
        pj_error_mean=[[[] for j in range(tag_num)] for i in range(len(distance))]
        for i in range(tag_num):
            ref_y=[-a1-b1 for a1,b1 in zip(x_reader,tag_data[i][ref_itp_ind])]
            for j in range(len(tag_data[i])):
                
                if j!=ref_itp_ind :
                    x=np.array(x_reader)
                    y=np.array(tag_data[i][j])
                    

                    mask = ~np.isnan(x) & ~np.isnan(y)
                    x_clean = x[mask]
                    y_clean = y[mask]

                    for ii in range(len(x_clean)):
                        rssi_pj=-y_clean[ii]-x_clean[ii]
                        for idx, val in enumerate(ref_y):
                            if not np.isnan(val) and val <= rssi_pj:
                                pj_fix=x_clean[ii]-(x_reader[idx]-pj[i])
                                # error=np.abs(pj_fix-x_clean[0])                             
                                error=(pj_fix-x_clean[0])
                                error_d=np.abs(np.power(10,(pj_fix-pj[i])/20)*distance[ref_itp_ind]-distance[j])/distance[j]*100  #距离误差
                                pj_mean[j].append(error)
                                dis_mean[j].append(error_d)
                                pj_error_mean[j][i].append(error)
                                break
        if ttag==target_tag:
            with open(output_path+"itp/"+tag_name[tind]+".txt", 'w') as file:
                for j in range(1,4):
                    min_length = min(len(sublist) for sublist in pj_error_mean[j])
                    aligned_data = [sublist[-min_length:] for sublist in pj_error_mean[j]]
                    mean_values = np.mean(aligned_data, axis=0)
                    y_avg_values_str = ' '.join(map(str, np.abs(mean_values)))
                    file.write(y_avg_values_str+'\n')
                
        pj_error[tind]=[sum(lst) / len(lst) if len(lst) > 0 else 0 for lst in pj_mean]
        dis_error[tind]=[sum(lst) / len(lst) if len(lst) > 0 else 0 for lst in dis_mean]

        if ttag==target_tag:
            for i in range(len(tag_data[target_tag])):
                x=np.array(x_reader)
                y=np.array(tag_data[target_tag][i])
                mask = ~np.isnan(x) & ~np.isnan(y)
                x_clean = x[mask]
                y_clean = y[mask]

                y_clean=-y_clean-x_clean
                x_begin=x_clean[0]
                x_clean=x_clean-x_begin

                for j in range(len(x_clean)):
                    r=distance[i]
                    chi=x_clean[j]
                    h_chi=y_clean[j]
                    with open(output_path+"3d/"+tag_name[tind]+".txt", 'a') as file:
                        file.write(f"{r} {chi} {h_chi}\n")

        for i in range(tag_num):
            x=np.array(x_reader)
            y=np.array(tag_data[i][ref_dis_ind])
            
            mask = ~np.isnan(x) & ~np.isnan(y)

            x_clean = x[mask]
            y_clean = y[mask]

            coeffs = np.polyfit(x_clean, y_clean, 1)
            k[i],b[i]=coeffs

        rssi_raw=[]
        rssi_fix=[]
        rssi_fix_z=[]
        db_val=[]
        for i in range(len(tag_data[ttag])):
            rssi=np.array(tag_data[ttag][i])
            ptx=np.array(x_reader)
            mask = ~np.isnan(ptx) & ~np.isnan(rssi)
            x_clean = ptx[mask]
            y_clean = rssi[mask]
            db_val.append(y_clean[0]-x_clean[0])

            x = ptx
            y = rssi
            rssi_fix.append(y+(1-k[ttag])* x-(1-k[ttag])*x[-1])
            rssi_fix_z.append(y+(1-k[ttag])* x-(1-k[ttag])*x_clean[0])
            rssi_raw.append(y)
        
        rssi_error=[]
        fix_rssi_error=[]
        for i in range(len(tag_data[ttag])):
            if i !=0:
                rssi_error.append(abs(distance[0]*np.power(10,((rssi_raw[0]-rssi_raw[i])/40))-distance[i]))
                fix_rssi_error.append(abs(np.power(10,((rssi_fix_z[0]-rssi_fix_z[i])/40))*distance[0]-distance[i]))

        if ttag==target_tag:
            with open(output_path+"dis/"+tag_name[tind]+".txt", 'w') as ofile:
                for line in fix_rssi_error:
                    mask=~np.isnan(line)
                    y_avg_values_str = ' '.join(map(str,line[mask]))
                    ofile.write(y_avg_values_str+' ')
                ofile.write('\n')
                for line in rssi_error:
                    mask=~np.isnan(line)
                    y_str = ' '.join(map(str,line[mask]))
                    ofile.write(y_str+' ')


        if  rssi_cor_dis_option==1:
            rssi_error=[]
            fix_rssi_error=[]
            for i in range(len(tag_data[ttag])):
                if i !=0:
                    db_error=40*math.log10(distance[i]/distance[0])
                    rssi_error.append((rssi_raw[0]-rssi_raw[i]-db_error))
                    fix_rssi_error.append((rssi_fix_z[0]-rssi_fix_z[i]-db_error))

            with open("./data/processed_data/rssi_cor_dis_error.txt", 'a') as file:
                y_avg_values_str = ' '.join(map(str, distance[1:]))
                file.write(y_avg_values_str+'\n')

                rssi_mean=np.abs(np.nanmean(rssi_error, axis=1))

                y_avg_values_str = ' '.join(map(str, rssi_mean))
                file.write(y_avg_values_str+'\n')

                fix_rssi_mean=np.abs(np.nanmean(fix_rssi_error, axis=1))

                y_avg_values_str = ' '.join(map(str,fix_rssi_mean))

                file.write(y_avg_values_str+'\n')
