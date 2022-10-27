import numpy as np

# Hanning Taper

def myHanningTaper(sig,ptap):
    '''
    Take signal and taper edges to zero with ptap being the % of original signal
    over which the taper will be applied.
    
    '''
    nt = np.size(sig)
    tlen = int(nt * ptap / 100)
    tap1 = np.hanning(2 * tlen)
    tap2 = np.ones_like(sig)
    tap2[:tlen] = tap1[:tlen]
    tap2[-tlen:] = tap1[-tlen:]
    sig2 = tap2 * sig
    return sig2
