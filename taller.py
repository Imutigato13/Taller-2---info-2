import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sp

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

def cargar_mt_csv(dir:''):
    try:
        if dir.endswith('.mat'):
            return sp.loadmat(dir)
        elif dir.endsith('.csv'):
            return pd.read_csv(dir)
        else:
            print("Ruta no reconocida")
    except:
        print("Valor no valido")

def sum(mat, eje = None):
    try:
        r = np.sum(mat, axis = eje)
        return r
    except:
        print("Valores no validos")
def rest(mat, eje = None):
    try:
        r = np.subtract.reduce(mat, axis = eje)
        return r
    except:
        print("Valores no validos")
def mult(mat, eje = None):
    try:
        r = np.multiply(mat, axis = eje)
        return r
    except:
        print("Valores no validos")
def div(mat, eje = None):
    try:
        r = np.divide(mat, axis = eje)
        return r
    except:
        print("Valores no validos")
def log(mat, eje = None):
    try:
        r = np.log(mat, axis = eje)
        return r
    except:
        print("Valores no validos")
def prom(mat, eje = None):
    try:
        r = np.mean(mat, axis = eje)
        return r
    except:
        print("Valores no validos")
def desv(mat, eje = None):
    try:
        r = np.std(mat, axis = eje)
        return r
    except:
        print("Valores no validos")


