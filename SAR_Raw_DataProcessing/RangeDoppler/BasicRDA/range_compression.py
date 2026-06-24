import numpy as np
from parameters import *

def range_compress(raw):

    tau = (np.arange(Nrg) - Nrg//2) / Fs

    ref_mask = np.abs(tau) <= Tp/2

    ref = ref_mask * np.exp(
        1j * np.pi * Kr * tau**2
    )

    mf = np.conj(ref[::-1])

    rc = np.zeros_like(raw,dtype=complex)

    for az in range(raw.shape[0]):
        
        if az == Naz//2:
            peak = np.argmax(np.abs(rc[az,:]))

        rc[az,:] = np.convolve(
            raw[az,:],
            mf,
            mode='same'
        )

    return rc