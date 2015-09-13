import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

def import_data():
    ecg_data = [];
    ecg_data.append(scio.loadmat('matlab'));
    ecg_data.append(scio.loadmat('matlab1'));
    ecg_data = np.array(ecg_data)
    return(ecg_data)

