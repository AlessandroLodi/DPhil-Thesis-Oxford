#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, point):
        return (self.x + point.x, self.y + point.y)
    def add_x(self, point):
        return (self.x + point.x, self.y)
    def add_y(self, point):
        return (self.x, self.y + point.y)
    def __str__(self):
        return f"{self.x}, {self.y}"

def plot_point(point):

    fig = plt.figure(figsize=(3.5,2.9))
    ax = plt.subplot(111)
    ax.plot(point.x, point.y, '-ro')

def draw_triangle():
    pass

def load_data(filename=None):
    import os
    os.chdir("C:\\Users\\albus\\OneDrive - Nexus365\\Desktop\\projects\\gnr-aom-uv")
    if filename is None:
        filename = 'data.txt'
    data = pd.read_csv(filename, sep='\t', header=None).values
    x = data[:,0]
    y = data[:,1]
    return x, y

def plot_data():
    wavelength, intensity = load_data()
    plt.plot(wavelength,intensity)
    plt.show()

def plot_integration(filename=None):
    wavelength, intensity = load_data()  
    x1 = wavelength[100:200]
    y1 = intensity[100:200]
    yint = np.trapz(x1,y1)
    print("Integrated area under the curve from",wavelength[100],"to",wavelength[200],"=", yint)
    plt.plot(wavelength,intensity)
    plt.axvspan(wavelength[100], wavelength[200], color='red', alpha=0.5)
    plt.show()


def main():
    p = Point(5, 5)
    plot_point(p)

if __name__=='__main__':
    plot_integration()

# %%
