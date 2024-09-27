import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin,freqz
wp=0.375*np.pi
ws=0.5*np.pi
wt=ws-wp
n1=np.ceil(8*np.pi/wt)
N=int(n1+(n1-1)%2)
print('Order of the FIR filtr N=',N)
h_hamming=firwin(N,Wc,window='hamming')
h_blackman=firwin(N,Wc,window='blackman')
beta=8
h_kaiser=firwin(N,Wc,window=('kaiser',beta))
plt.figure(1)
w,H_hamming=freqz(h_hamming)
w,H_blackman=freqz(h_blackman)
w,H_kaiser=freqz(h_kaiser)
plt.plot(w,np.abs(H_hamming),label='Hamming')
plt.plot(w,np.abs(H_blackman),label="Blackman")
plt.plot(w,np.abs(H_kaiser),label='Kasier')
plt.title('Frequency Response')
plt.xlabel('Frequency(radians)')
plt.ylabel('Magnitude')
plt.legend()
plt