import numpy as np

def azimuth_fft(rc):

    RD = np.fft.fftshift(
        np.fft.fft(rc, axis=0),
        axes=0
    )

    return RD