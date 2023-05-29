import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy.stats import linregress
import os
import numpy as np

FILE_PATH = "./D_Raman/"
#1,2,5

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

def writeFile(filename, arr1, arr2):
    f = open("./"+filename, 'w+')
    for i in range(len(arr1)):
        f.write(str(arr1[i])+'\t'+str(arr2[i])+'\n')
    f.write("The first column: Pressure[GPa] \nThe second column: Ramanshift[cm-1]")
    f.close()

def func(x, A, B):
    return A*x + B

if __name__ == '__main__':
    files = os.listdir(FILE_PATH)

    files.sort(key=lambda x:float(x.split('_')[5][:-3]))
    p1 = []
    p2 = []
    p3 = []
    Pressure = []
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
    _, _, r_value, _, _ = linregress(Pressure, p1)
    info = "Slope: "+str(coeffp1[0]) + " || R-Square = "+str(r_value)
    #ax.annotate(info, xy=(30,coeffp1[0]*30+coeffp1[1]),xytext=(27,coeffp1[0]+coeffp1[1]-20),xycoords='data',arrowprops=dict(facecolor='black',shrink=0.05))

    coeffp2,_ = curve_fit(func, Pressure, p2)
    ax.plot(x, coeffp2[0]*x+coeffp2[1],'-',label='Peak in 247.49cm-1')
    _, _, r_value, _, _ = linregress(Pressure, p2)
    info = "Slope: "+str(coeffp2[0]) + " || R-Square = "+str(r_value)
    #ax.annotate(info, xy=(30,coeffp2[0]*30+coeffp2[1]),xytext=(27,coeffp2[0]+coeffp2[1]-20),xycoords='data',arrowprops=dict(facecolor='black',shrink=0.05))

    coeffp3,_ = curve_fit(func, Pressure, p3)
    ax.plot(x, coeffp3[0]*x+coeffp3[1],'-',label='Peak in 490.04cm-1')
    _, _, r_value, _, _ = linregress(Pressure, p3)
    info = "Slope: "+str(coeffp3[0]) + " || R-Square = "+str(r_value)
    #ax.annotate(info, xy=(30,coeffp3[0]*30+coeffp3[1]),xytext=(27,coeffp3[0]+coeffp3[1]-20),xycoords='data',arrowprops=dict(facecolor='black',shrink=0.05))
    

    ax.set_title("F vs P Curve",fontsize = 15)
    ax.set_xlabel("Pressure[GPa]",fontdict={'size':15})
    ax.set_ylabel("Location of the Peak[cm-1]",fontdict={'size':15})
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_tick_params(labelsize = 15)
    ax.xaxis.set_tick_params(labelsize = 15)
    ax.grid()
    plt.legend()
    plt.savefig('./Mo2C_PD.png', dpi = 300, transparent = True)
    plt.show()

