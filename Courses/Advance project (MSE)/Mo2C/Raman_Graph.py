import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import random

FILE_PATH = "./D_Raman/"

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

if __name__ == '__main__':

    files = os.listdir(FILE_PATH)
    files.sort(key=lambda x:float(x.split('_')[5][:-3]))

    fig, ax = plt.subplots(figsize = (20,10))

    ax.set_title("Decompression Process",fontsize = 15)
    ax.set_xlabel("Ramanshift[cm-1]",fontdict={'size':15})
    ax.set_ylabel("Intensity",fontdict={'size':15})
    ax.set_xlim(20,1300)
    ax.set_ylim(18200,19800)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
    ax.yaxis.set_ticks([])
    ax.xaxis.set_tick_params(labelsize = 15)

    counts = 0

    for times, file in enumerate(files):
        #print
        if times not in [0,2,5,8,10,14,16]:
            continue
        Pressure = file.split('_')[5][:-3] + "GPa"
        color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        
        x_axis = []
        y_axis = []
        
        contents = readFile(file, 0)
        
        for i in contents:
            '''
            if times < 5:
                raman_shift = ((1e7)/457) - ((1e7)/float(i.split('\t')[0]))
                x_axis.append(raman_shift)
            else:
                x_axis.append(float(i.split('\t')[0]))
            if times == 12:
                y_axis.append(float(i.split('\t')[1])+counts*205)
            else:
                y_axis.append(float(i.split('\t')[1])+counts*200)
            '''
            x_axis.append(float(i.split('\t')[0]))
            y_axis.append(float(i.split('\t')[1])+counts*200)
        
        
       #plt.plot(peaks, y_axis[peaks],'*')
        ax.plot(x_axis, y_axis,color=color)
       # ax.text(1310, y_axis[198]+40, Pressure,color=color,size=15)
        ax.text(1310, 18400+counts*200, Pressure,color=color,size=15)
        '''
        peaks, _ = find_peaks(y_axis[17:365],distance=25)
        for p in peaks:
            plt.plot(x_axis[p+17],y_axis[p+17],'*',color=color)
        '''
        counts += 1
        
    plt.savefig('./Mo2C_D.png', dpi = 300, transparent = True)
    plt.show()
