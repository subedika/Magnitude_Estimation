import numpy as np

# FFT

def fconv(tap,v,n):
    i = 0
    freqd = np.zeros((v,(n//2)+1,3),np.float32)
#freq_body = np.zeros((len(df2),3001,3),np.float32)
#freq_moment = np.zeros((len(df3),3001,3),np.float32)
    for i in range(v):
        b1 = tap[i,:,0]
        b2 = tap[i,:,1]
        b3 = tap[i,:,2]
        e = abs(np.fft.rfft(b1))
        n = abs(np.fft.rfft(b2))
        z = abs(np.fft.rfft(b3))
    #fdom = np.hstack((e,n,z))
    #fdom = fdom.reshape(1,1501,3)
        freqd[i,:,0] = e
        freqd[i,:,1] = n
        freqd[i,:,2] = z
    return freqd