import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy.stats import linregress
import os
import numpy as np

FILE_PATH = "./I_Raman/"
#2,3,5

def readFile(filename, mode=1):
    f = open(FILE_PATH+filename)
    contents = []
    if mode == 1:
        f.seek(1414)
        contents = f.readlines()
        f.close()
    else:
        for _ in range(1024):
            contents.append(f.readline().strip())
        f.close()
    return contents

def func(x, A, B):
    return A*x + B

if __name__ == '__main__':
    files = os.listdir(FILE_PATH)

    files.sort(key=lambda x:float(x.split('_')[4][:-3]))
    p1 = []
    p2 = []
    p3 = []
    Pressure = []
    for index,file in enumerate(files):
        #color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        contents = readFile(file, 0)
        Pressure.append(float(file.split('_')[4][:-3]))
        x_axis = []
        y_axis = []

        for i in contents:
            if index < 5:
                raman_shift = ((1e7)/457) - ((1e7)/float(i.split('\t')[0]))
                x_axis.append(raman_shift)
            else:
                x_axis.append(float(i.split('\t')[0]))
            y_axis.append(float(i.split('\t')[1]))
        
        peaks, _ = find_peaks(y_axis[17:365],distance=25)
            
        if index == 0 or index == 1 or index == 3 or Pressure[-1] == 9:
            p1.append(x_axis[peaks[0]+17])
            p2.append(x_axis[peaks[1]+17])
            p3.append(x_axis[peaks[3]+17])
        else:
            p1.append(x_axis[peaks[1]+17])
            p2.append(x_axis[peaks[2]+17])
            p3.append(x_axis[peaks[4]+17])
    
    del p1[8]
    del p2[8]
    del p3[8]
    del Pressure[8]

    FILE_PATH = "./D_Raman/"
    files = os.listdir(FILE_PATH)

    files.sort(key=lambda x:float(x.split('_')[5][:-3]))
    for index,file in enumerate(files):
        #color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        contents = readFile(file, 0)

        Pressure.append(float(file.split('_')[5][:-3]))
        x_axis = []
        y_axis = []

        for i in contents:
            x_axis.append(float(i.split('\t')[0]))
            y_axis.append(float(i.split('\t')[1]))
        
        peaks, _ = find_peaks(y_axis[17:365],distance=10)
            
        
        if index in [2,3,5,6,7]:
            p1.append(x_axis[peaks[2]+17])
            p2.append(x_axis[peaks[4]+17])
            p3.append(x_axis[peaks[9]+17])
        elif index in [0,4]:
            p1.append(x_axis[peaks[2]+17])
            p2.append(x_axis[peaks[4]+17])
            p3.append(x_axis[peaks[10]+17])
        elif index == 1:
            p1.append(x_axis[peaks[1]+17])
            p2.append(x_axis[peaks[3]+17])
            p3.append(x_axis[peaks[8]+17])
        elif index in [8,13,16]:
            p1.append(x_axis[peaks[2]+17])
            p2.append(x_axis[peaks[5]+17])
            p3.append(x_axis[peaks[9]+17])
        elif index in [9,10,14]:
            p1.append(x_axis[peaks[2]+17])
            p2.append(x_axis[peaks[5]+17])
            p3.append(x_axis[peaks[10]+17])
        elif index == 12:
            p1.append(x_axis[peaks[1]+17])
            p2.append(x_axis[peaks[4]+17])
            p3.append(x_axis[peaks[8]+17])
        elif index == 15:
            p1.append(x_axis[peaks[2]+17])
            p2.append(x_axis[peaks[4]+17])
            p3.append(x_axis[peaks[8]+17])
        elif index == 11:
            p1.append(x_axis[peaks[1]+17])
            p2.append(x_axis[peaks[3]+17])
            p3.append(x_axis[peaks[8]+17])

    fig, ax = plt.subplots(figsize = (20,10))
    
    ax.scatter(Pressure,p1,s = 80)
    ax.scatter(Pressure,p2,s = 80)
    ax.scatter(Pressure,p3,s = 80)

    x = np.linspace(0, 35)

    coeffp1,_ = curve_fit(func, Pressure, p1)
    ax.plot(x, coeffp1[0]*x+coeffp1[1],'-',label='Peak in 139.58cm-1')


    coeffp2,_ = curve_fit(func, Pressure, p2)
    ax.plot(x, coeffp2[0]*x+coeffp2[1],'-',label='Peak in 247.49cm-1')

    

    coeffp3,_ = curve_fit(func, Pressure, p3)
    ax.plot(x, coeffp3[0]*x+coeffp3[1],'-',label='Peak in 490.04cm-1')

    ax.set_title("F vs P Curve - All Process",fontsize = 15)
    ax.set_xlabel("Pressure[GPa]",fontdict={'size':15})
    ax.set_ylabel("Location of the Peak[cm-1]",fontdict={'size':15})
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_tick_params(labelsize = 15)
    ax.xaxis.set_tick_params(labelsize = 15)
    ax.grid()

    plt.legend()
    plt.savefig('./Mo2C_PA.png', dpi = 300, transparent = True)
    plt.show()

