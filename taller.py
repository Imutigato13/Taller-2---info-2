import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.ion()

matriz_4D = np.random.randint(100,size = (10,15,20,40))
matriz_3D = np.copy(matriz_4D)[0,:,:,:]

print(f"""\rDimension: {matriz_3D.ndim}
\rTamaño: {matriz_3D.size}
\rForma: {matriz_3D.shape}
\rTipo: {matriz_3D.dtype}
\rTamaño por byte del array: {matriz_3D.itemsize}
\rTamaño de cada byte :{matriz_3D.nbytes}""")

matriz_2D = np.reshape(matriz_3D,(matriz_3D.shape[0],matriz_3D.shape[1]*matriz_3D.shape[2]))
print(matriz_2D)

def df_trans(matriz):
    try:
        df = pd.DataFrame(matriz)
        return df
    except:
        print("Valor no valido")

