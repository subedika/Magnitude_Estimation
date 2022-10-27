import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def coda_conv(s):
    s = s.split('[')
    s = s[2]
    s = s.split(']')
    return float(s[0])


def snr_conv(sr):
    sr2 = sr.split()
    SNR = []
    for i, d in enumerate(sr2):
        if d != '[' and d != ']':
            
            dL = d.split('[')
            dR = d.split(']')
            
            if len(dL) == 2:
                dig = dL[1]
            elif len(dR) == 2:
                dig = dR[0]
            elif len(dR) == 1 and len(dR) == 1:
                dig = d
            try:
                dig = float(dig)
            except Exception:
                dig = None
                
            SNR.append(dig)
    return(SNR)


def mda_proc(d):

    df = pd.read_csv(d)
    df = df[(df.source_distance_km <= 110)]
    df = df[(df.source_magnitude_type == 'ml')]
    #df = df[(df.trace_category=='earthquake_local')]
    df = df[df.p_arrival_sample >= 200]
    #df = df[df.p_arrival_sample+2900 <= 6000]
    #df = df[df.p_arrival_sample <= 1500]
    #df = df[df.s_arrival_sample >= 200]
    #df = df[df.s_arrival_sample <= 2500]
#df = df[df.coda_end_sample <= 3000]
    df = df[df.p_travel_sec.notnull()]
    df = df[df.p_travel_sec > 0]
    df = df[df.source_distance_km.notnull()]
    df = df[df.source_distance_km > 0]
    df = df[df.source_depth_km.notnull()]
    df = df[df.source_magnitude.notnull()]
    df = df[df.back_azimuth_deg.notnull()]
    df = df[df.back_azimuth_deg > 0]
#df2 = df[(df.source_magnitude_type == 'mb')]
#df3 = df[(df.source_magnitude_type == 'mw')] 
#df = df[(df.p_arrival_sample <= 2000)]
#df = df[(df.s_arrival_sample >= 2000)]
#df = df[(df.s_arrival_sample <= 4000)]
#df = df[df.p_arrival_sample >= 200]
#df = df[df.p_arrival_sample+2900 <= 6000]
#df = df[df.p_arrival_sample <= 1500]
#df = df[df.s_arrival_sample >= 200]
#df = df[df.s_arrival_sample <= 2500]
    df.snr_db = df.snr_db.apply(lambda x:np.mean(snr_conv(x)))
    df = df[df.snr_db > 20]
#df2.snr_db = df2.snr_db.apply(lambda x:np.mean(snr_conv(x)))
#df2 = df2[df2.snr_db > 20]
#df3.snr_db = df3.snr_db.apply(lambda x:np.mean(snr_conv(x)))
#df3 = df3[df3.snr_db > 20]
    df.coda_end_sample = df.coda_end_sample.apply(lambda x:coda_conv(x))
    df = df[df.coda_end_sample <= 6000]
#df2.coda_end_sample = df2.coda_end_sample.apply(lambda x:coda_conv(x))
#df2 = df2[df2.coda_end_sample <= 6000]
#df3.coda_end_sample = df3.coda_end_sample.apply(lambda x:coda_conv(x))
#df3 = df3[df3.coda_end_sample <= 6000]
    return df, len(df)
#print(len(df2))
#print(len(df3))


def wave_proc(dt, w):
    ev = dt['trace_name'].to_list()
    x = np.zeros((len(dt),6000,3),np.float32)
    y = np.zeros((len(dt),1),np.float32)

    dtf = h5py.File(w,'r')

    for c, evi in enumerate(ev):
        eg = dtf.get('data/'+str(evi))
        data = np.array(eg)
        mag = round(float(eg.attrs['source_magnitude']),2)    
        psamp = int(eg.attrs['p_arrival_sample'])
        ssamp = int(eg.attrs['s_arrival_sample'])
        BAZ = round(float(eg.attrs['back_azimuth_deg']), 2)
        dpt = eg.attrs['source_depth_km']
        dis = round(float(eg.attrs['source_distance_deg']), 2)
        SNR = eg.attrs['snr_db']
    #dshort = data[psamp-100:psamp+2900,:]
        x[c,:,:] = data
        y[c,0] = mag
    
    dtf.close()
    return x, y, x.shape, y.shape


