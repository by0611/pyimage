import skimage.io as io 
from skimage import data
import matplotlib.pyplot as plt  

x = data.cell()
plt.figure(), io.imshow(x)

y = data.horse()
plt.figure(), io.imshow(y)

z = data.astronaut()
plt.figure(), io.imshow(z)

plt.show()
