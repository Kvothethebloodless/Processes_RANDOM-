import numpy as np
import matplotlib.pyplot as plt

def gen_cdf(rand_seq,no_bins,plotsig):
    dist_hist = np.histogram(rand_seq,no_bins);
    cdf_freq_val = np.cumsum(dist_hist[0]);
    cdf_xvals=dist_hist[1];
    cdf_freq_val = np.insert(cdf_freq_val,0,0)/np.max(cdf_freq_val);
    if plotsig==1:
        fig = plt.figure()

        plt.plot(cdf_xvals,cdf_freq_val)
        fig.suptitle('CDF')
    return (cdf_freq_val,cdf_xvals)

def gen_pdf(seq,no_bins,plotsig):
    pdf = np.histogram(seq,no_bins);
    pdf_val = pdf[0];
    pdf_xval = pdf[1];
    pdf_xval = np.delete(pdf_xval,0);
    if plotsig==1:
        fig = plt.figure()
        plt.plot(pdf_xval,pdf_val)
        fig.suptitle('PDF')

    return (pdf_val,pdf_xval)
