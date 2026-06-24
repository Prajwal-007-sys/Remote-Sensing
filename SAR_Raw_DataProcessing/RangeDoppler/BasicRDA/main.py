from simulator import generate_raw_data
from range_compression import range_compress
from plots import show_image
import matplotlib.pyplot as plt
import numpy as np
from parameters import *
from azimuth__fft import azimuth_fft
from azimuth_compression import azimuth_compress
from rcmc import rcmc
from image_formation import image_formation

raw = generate_raw_data()

plt.imshow(
    np.real(raw),
    aspect='auto'
)

plt.title("Raw Data (Real Part)")
plt.colorbar()
plt.show()
rc = range_compress(raw)

plt.figure()

plt.imshow(
    20*np.log10(np.abs(rc)+1e-6),
    aspect='auto'
)

plt.title("Range Compressed Data")

plt.colorbar()

plt.show()

center_line = Naz//2

line = raw[center_line,:]

tau = np.arange(Nrg)/Fs

ref_mask = np.abs(tau) <= Tp/2

ref = ref_mask * np.exp(
    1j*np.pi*Kr*tau**2
)

mf = np.conj(ref[::-1])

test = np.convolve(
    line,
    mf,
    mode='same'
)
peak_rc = np.argmax(
    np.abs(rc[Naz//2,:])
)

print("Compressed peak =", peak_rc)

print(np.unravel_index(np.argmax(np.abs(rc)), rc.shape))

# plt.plot(np.abs(rc[:, peak_range]))
# plt.title("Azimuth Response at Peak Range Bin")
# plt.grid()
# plt.show()

# plt.plot(np.abs(rc[Naz//2, :]))
# plt.title("Range Response at Center Azimuth")
# plt.grid()
# plt.show()

plt.plot(np.abs(raw[Naz//2, :]))
plt.title("Range Response at Center Azimuth")
plt.grid()
plt.show()

center_line = Naz//2

peak_raw = np.argmax(np.abs(raw[center_line,:]))

print(peak_raw)

plt.show()

RD = azimuth_fft(rc)

peak_range = np.argmax(
    np.sum(np.abs(rc), axis=0)
)

plt.figure()

plt.plot(
    np.abs(RD[:, peak_range])
)

plt.title("Doppler Spectrum")
plt.grid()

plt.show()

RD = rcmc(RD)

RDc = azimuth_compress(RD)

img = image_formation(RDc)
print(
    np.unravel_index(
        np.argmax(np.abs(img)),
        img.shape
    )
)

plt.figure()

plt.imshow(
    np.log10(np.abs(img)+1e-6),
    aspect='auto'
)

plt.title("Focused SAR Image")
plt.colorbar()

plt.show()

plt.figure()
plt.imshow(
    np.log10(np.abs(RD)+1e-6),
    aspect='auto'
)
plt.title("Range Doppler Domain")
plt.colorbar()
plt.show()

peak_range = np.argmax(
    np.sum(np.abs(rc), axis=0)
)

doppler_slice = np.abs(RD[:, peak_range])

plt.figure()
plt.plot(doppler_slice)
plt.title("Doppler Spectrum at Target Range")
plt.grid()
plt.show()

print("Peak range bin =", peak_range)
# show_image(
#     rc,
#     "Range Compressed Data"
# )

# rc = range_compress(raw)

# show_image(
#     np.abs(rc),
#     "Range Compressed"
# )