function [yhat] = wienerFilter(ideal,observation)


Fs=256;
R=1;  
noise = observation-ideal;

N=length(observation);

Sf2=real(fft(ideal,N*2-1)).^2;  
Nf2=real(fft(noise,N*2-1)).^2;   
Cf=real(fft(observation,N*2-1)); 
H=Sf2./(Sf2+Nf2);             
Yhat=H.*Cf/R;                 
yhat=real(ifft(Yhat));        
yhat=yhat(1:length(observation)); 

end
