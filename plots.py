import matplotlib.pyplot as plt
import numpy as np

# Magnitude

def mag_plot(ym):
    plt.hist(ym, bins='auto', facecolor='r', alpha=0.75)
    plt.title("Magnitude Range of Events")
    plt.xlabel("Magnitude")
    plt.ylabel('No. of events')
    plt.show()


# Signal-to-noise ratio

def snr_plot(f):
    #sn = f[['snr_db']].to_numpy()
    plt.hist(f, bins='auto', facecolor='b', alpha=0.75)
    plt.title('Signal-to-Noise Ratio')
    plt.xlabel('SNR')
    plt.ylabel('Events')
    plt.show()
    

# Depth

def depth_plot(d):
    plt.hist(d, bins='auto', facecolor='c', alpha=0.75)
    plt.title('Source Depth')
    plt.xlabel('Source Depth in Km')
    plt.ylabel('Events')
    plt.show()
    
# Azimuth

def azimuth_plot(a):
    plt.hist(a, bins='auto', facecolor='m', alpha=0.75)
    plt.title('Back Azimuth')
    plt.xlabel('Back Azimuth in Degrees')
    plt.ylabel('Events')
    plt.show()