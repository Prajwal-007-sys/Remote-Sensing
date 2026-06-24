import matplotlib.pyplot as plt
import numpy as np

def show_image(data, title):

    plt.figure(figsize=(8,6))

    plt.imshow(
        np.abs(data),
        aspect='auto'
    )

    plt.title(title)

    plt.colorbar()

    plt.show()
    
    