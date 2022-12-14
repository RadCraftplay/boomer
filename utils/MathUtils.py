import numpy as np

def cos_sim(v1, v2):
    denominator = (np.linalg.norm(v1)*np.linalg.norm(v2))
    if denominator == 0:
        return 0.0
    else:
        costheta = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
        return costheta