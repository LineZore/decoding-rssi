close all
clear all
% load BostonTemp.mat
% yearIdx = 16;
discol = 1;
txcol = 2;
chicol =3;
data = load('.\data\processed_data\3d\9640.txt');
dises = unique(data(:,1));
txes = unique(data(:,2));
m= length(dises);
n = length(txes);
data2 = zeros(m,n);
for i = 1:length(data)
    index1 = dises == data(i,1);
    index2 = txes == data(i,2);
    data2(index1,index2) = data(i,3);
end
figure
b = bar3(data2(:,1:10:length(txes)),0.7);
colormap('turbo');
% caxis([1,40]);
for k = 1:length(b)
    zdata = b(k).ZData;
    b(k).CData = zdata;
    b(k).FaceColor = 'interp';
end
 xticks(1:2:8)
  yticks(1:2:7)
set(gca,'yticklabel',{'2','4','6','8'})
set(gca,'xticklabel',{'0','5','10','15','20'})
% zlim([0.5,5.5]);
% ylim([0.5,5.5]);
view(63.767781716549187,29.30643142089788)
fun_set_3daxis_size('\chi (dB)','Distance (m)','h(\chi) (dB)',32,[640 480])