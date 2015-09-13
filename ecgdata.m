ecgdata = importdata('ecgsyn.dat');
ecgdata = ecgdata(:,0:1);
time_points = ecgdata(:,0);
data_points = ecgdata(:,1);
[~,no_samples] = size(ecg_data);

data_points = ((data_points/max(data_points))*2)-1;


gaussian_sigma = 0;
gaussian_var = .5;
gaussian_noise = normrnd(gaussian_sigma,gaussian_var,size(ecg_data) );

poission_lambda = .3;
poission_noise = poissrnd(poisson_lambda,size(ecg_data));

gaussian_polluted_signal = data_points+gaussian_noise;
poission_polluted_signal = data_points+poission_noise;
ideal_signal = data_points;

fltsig1 = wienerFilter(ideal_signal,gaussian_polluted_signal);
fltsig2 = wienerFilter(ideal_signal,poission_polluted_signal);
order_median_filter = 3;

fltsig3 = medfilt1(gaussian_polluted_signal,order_median_filter);
fltsig4 = medfilt1(poission_polluted_signal,order_median_filter);

figure

%subplot(4,2,1)
plot(data_points,time_points)
hold all
plot(gaussian_polluted_signal,time_points)
plot(poission_polluted_signal,time_points)
plot(fltsig1,time_points)
plot(fltsig2,time_points)
plot(fltsig3,time_points)
plot(fltsig4,time_points)














