function [  ] = fun_set_3daxis_size( x_label, y_label, z_label,size,a)
%FUN_SET_AXIS Summary of this function goes here
%   Detailed explanation goes here
%   size: font size 
aaa = [100 100 a];
% set(gcf,'Position',[100 100 420 300]);  % get a figure with fixed size
set(gcf,'Position',aaa);  % get a figure with fixed size


label_size = size;
axis_size = size;

set(gca,'FontSize',axis_size,'fontname','Times New Roman');
xlabel(x_label,'Fontsize',label_size,'fontname','Times New Roman');
ylabel(y_label,'Fontsize',label_size,'fontname','Times New Roman');
zlabel(z_label,'Fontsize',label_size,'fontname','Times New Roman');


end


