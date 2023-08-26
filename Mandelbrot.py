from PIL import Image
from math import log
import matplotlib.cm

def escape_count(c, max_iter):
    """
    Input- complex number, maximum iteration
    Output- If diverges return that (step + 1 - log(log(abs(z)))/log(2))
    else If not diverges max_iterations
    """
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > escape_radius:
            return i + 1 - log(log(abs(z)))/log(2)
    return max_iter


def stability(c, max_iter):
    """
    Output- Point not diverge give 1
    point diverge give 0 or cloase to zero
    """
    value = escape_count(c, max_iter)/max_iter
    return max(0.0, min(value, 1.0))


def denormailize(palette):
    return [tuple(int(channel*255) for channel in color) for color in palette]
#print(stability(1,100))

colormap = matplotlib.cm.get_cmap('inferno').colors
#print(colormap[0])

palette = denormailize(colormap)

(width, height) = (600, 512)

max_iter = 25

scale = 0.0085
escape_radius = 1000

image = Image.new(mode='RGB', size = (width, height))

for y in range(height):
    for x in range(width):
        c = scale*complex(x-width/2, height/2 -y)
        value= stability(c, max_iter)
        index = int( min(value*len(palette), len(palette)-1))
        image.putpixel( (x,y), palette[index % len(palette)])

image.show()
image.save("Mandelbrot_image.jpg")