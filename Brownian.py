#Weiner process is generated by adding gaussians consecutively.
#W_t-W_S ==> N(0,t-s)
#We are generating a sequential Wiener Process

import numpy as np
import matplotlib.pyplot as plt
import poission as pos



def genrand_seq(n_dims,N_samples):
    seq = np.empty((n_dims,N_samples));
    mean = 0;
    std = 1;
    seq = np.random.normal(mean,std,(n_dims,N_samples))
    return(seq)

def gen_proc(seq):
    proc = np.cumsum(seq,axis=1);
    return proc


if __name__ == "__main__":
    n_dims = 1;
    N_samples = 1000;
    seq = genrand_seq(n_dims,N_samples);
    seq = gen_proc(seq);
    plt.plot(np.transpose(seq))
    cdf = pos.gen_cdf(seq[0],100,1)
    pdf = pos.gen_pdf(seq[0],100,1)






