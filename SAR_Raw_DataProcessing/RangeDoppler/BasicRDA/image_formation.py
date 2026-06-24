import numpy as np

def image_formation(RDc):

    img = np.fft.ifft(
        np.fft.ifftshift(RDc, axes=0),
        axis=0
    )

    return img