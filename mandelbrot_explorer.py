import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(width, height, xmin=-2, xmax=2, ymin=-2, ymax=2, max_iter=256):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            mandelbrot_image[i, j] = mandelbrot(x[i] + 1j*y[j], max_iter)

    return mandelbrot_image

def plot_mandelbrot(width, height, xmin=-2, xmax=2, ymin=-2, ymax=2, max_iter=256):
    mandelbrot_image = mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter)
    plt.imshow(mandelbrot_image.T, cmap='inferno', extent=[xmin, xmax, ymin, ymax])
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Set')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()

if __name__ == "__main__":
    plot_mandelbrot(800, 800)
