# Rn = 20             # Slant range of scene center; units - Km
# Vr = 150            # Effective radar velocity   ; units - m/s
# Tr = 2.5            # Transmitted Pulse duration ; units - micro sec
# Kr = 20 * 10^12     # Range FM Rate - rate at which the transmitted radar frequency changes in one  
# f0 = 5.3            # Radar center frequency     ; units - G Hz
# fdop = 80           # doppler bandwidth          ; units - Hz
# Fr = 60             # Range sampling rate        ; units - MHz
# Fa = 100            # PRF (Azimuth sampling rate); units - Hz
# Naz = 256           # number of range lines      ; 
# Nrg = 320           # samples per range line     ; 
# Theta = [3.5, 21.9] # Beam squint angle          ; units - deg
# nc = [-8.1, -49.7]  # Beam center crossing time  ; units - sec
# fnc = [320, 1975]   # Doppler centroid frequency ; units - Hz

import numpy as np

c = 3e8

fc = 5.3e9
lam = c / fc

B = 30e6
Tp = 2.5e-6

Kr = B / Tp

PRF = 1000
Fs = 40e6

V = 1000
R0 = 200

Naz = 1024
Nrg = 1024

Ka = -(2*V**2)/(lam*R0)