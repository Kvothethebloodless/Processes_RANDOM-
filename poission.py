#Poission distribution reference: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video-lectures/lecture-14-poisson-process-i/#vid_transcript
#lamba*delta = p
#Lambda --> Poission Parameter
#Delta --> Bernoulli trial window. In this code its one
#p --> Bernoulli success probability
#threshold --> To get a bernoulli process from a random process with probability of p -> threshold 1-p

import numpy as np
import matplotlib.pyplot as plt
import densityfunctions as df

def threshold_loc(rand_seq,threshold):
    loc = np.where(rand_seq>threshold);
    return loc

def calc_interarrival_times(loc_seq):
    no_of_arrivals = np.size(loc_seq)
    ia_times = [];
    ia_times.append(loc_seq[0][0]);
    for k in range(no_of_arrivals-1):
        ia_times.append(loc_seq[0][k+1] - loc_seq[0][k]);
    ia_times = np.array(ia_times);
    return(ia_times,no_of_arrivals)

def gen_rand_seq(N):
    rand_seq = np.random.rand(N);
    return rand_seq



if __name__ == "__main__":
    N = 1000000;
    lambda_poisson = .7;
    delta = 1;
    p = lambda_poisson*delta;
    threshold = 1-p;

    seq = gen_rand_seq(N);
    loc_seq = threshold_loc(seq,threshold);
    (ia_times,n_arrivals) = calc_interarrival_times(loc_seq);
    x_val = np.arange(n_arrivals);
    #dist_hist = np.histogram(ia_times,10);
    (cdf_freq_val,cdf_xvals) = df.gen_cdf(ia_times,10,1);
    (pdf_val,pdf_xval) = df.gen_pdf(ia_times,10,1);
    #plt.plot(cdf_xvals,cdf_freq_val,'o')
    #plt.figure()
    #plt.plot(pdf_val,pdf_xval)
    plt.show()
    #plt.figure
    #plt.plot(dist_hist[0])

    #plt.figure
    #plt.plot(x_val,ia_times)

