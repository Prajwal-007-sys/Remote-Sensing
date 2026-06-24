import numpy as np

def rcmc(RD):

    Naz, Nrg = RD.shape

    RD_corr = np.zeros_like(RD)

    center = Naz // 2

    for fd in range(Naz):

        shift = int(
            20 *
            ((fd - center)/center)**2
        )

        RD_corr[fd,:] = np.roll(
            RD[fd,:],
            -shift
        )

    return RD_corr