import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.ion()

matriz_4D = np.random.randint(100,size = (10,15,20,40))
matriz_3D = np.copy(matriz_4D)[0,:,:,:]

