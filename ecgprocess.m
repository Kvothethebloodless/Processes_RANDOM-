close all
ecgdata = importdata('ecgsyn.dat');
ecgdata = ecgdata(:,1:2);

time_points = ecgdata(:,1);
data_points = ecgdata(:,2);
[~,no_samples] = size(ecgdata);
clear ecgdata
data_points = ((data_points/max(data_points))*2)-1;


gaussian_sigma = 0;
gaussian_var = .5;
gaussian_noise = normrnd(gaussian_sigma,gaussian_var,size(data_points) );

poission_lambda = .3;
poission_noise = poissrnd(poission_lambda,size(data_points));

gaussian_polluted_signal = data_points+gaussian_noise;
poission_polluted_signal = data_points+poission_noise;
ideal_signal = data_points;

fltsig1 = wienerFilter(ideal_signal,gaussian_polluted_signal);
fltsig2 = wienerFilter(ideal_signal,poission_polluted_signal);
order_median_filter = 10;

fltsig3 = medfilt1(gaussian_polluted_signal,order_median_filter);
fltsig4 = medfilt1(poission_polluted_signal,order_median_filter);

figure

subplot(3,1,1)
plot(time_points,data_points)
ylabel('Original Data')
subplot(3,1,2)
plot(time_points,gaussian_polluted_signal)
ylabel('Gaussian Noise Added Signal')
subplot(3,1,3)
plot(time_points,poission_polluted_signal)
ylabel('Poission Noise Added Signal')

figure
subplot(4,1,1)
plot(time_points,data_points)
ylabel('Original Data')
subplot(4,1,2)
plot(time_points,gaussian_polluted_signal)
ylabel('Gaussian Noise Added Signal')
subplot(4,1,3)
plot(time_points,fltsig1)
ylabel('Filtered with Wiener Filter')
subplot(4,1,4)
plot(time_points,fltsig3)
ylabel('Filtered with Median Filter')

figure
subplot(4,1,1)
plot(time_points,data_points)
ylabel('Original Data')
subplot(4,1,2)
plot(time_points,poission_polluted_signal)
ylabel('Poission Noise Added Signal')
subplot(4,1,3)
plot(time_points,fltsig2)
ylabel('Filtered with Wiener Filter')
subplot(4,1,4)
plot(time_points,fltsig4)
ylabel('Filtered with Median Filter')















