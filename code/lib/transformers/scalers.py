import numpy as np

def minmax(list_data):
    data = np.array(list_data)
    data = np.nan_to_num(data.astype(float))
    if data.max() == data.min():
        return np.zeros(len(data))
    return (data - data.min()) / (data.max()-data.min())