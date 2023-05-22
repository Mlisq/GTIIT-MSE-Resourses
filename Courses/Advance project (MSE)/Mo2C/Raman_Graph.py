import matplotlib.pyplot as plt
import os
import random

FILE_PATH = "./I_Raman/"

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
    files.sort(key=lambda x:float(x.split('_')[4][:-3]))

    fig, ax = plt.subplots(figsize = (20,10))

    ax.set_title("Increasing Process")
    ax.set_xlabel("Ramanshift[cm-1]")
    ax.set_ylabel("Intensity")
    ax.set_xlim(20,1300)
    ax.set_ylim(18200,23200)

    for times, file in enumerate(files):
        #print
        Pressure = file.split('_')[4][:-3] + "GPa"
        print(Pressure)
        color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        
        x_axis = []
        y_axis = []
        
        contents = readFile(file, 0)
        
        for i in contents:

            if times < 5:
                raman_shift = ((1e7)/457) - ((1e7)/float(i.split('\t')[0]))
                x_axis.append(raman_shift)
            else:
                x_axis.append(float(i.split('\t')[0]))


            if times == 9:
                y_axis.append(float(i.split('\t')[1])+times*200)
            elif times == 4:
                y_axis.append(float(i.split('\t')[1])+times*200)
            elif times == 6 or times == 1:
                y_axis.append(float(i.split('\t')[1])+times*210)
            elif times == 11:
                y_axis.append(float(i.split('\t')[1])+times*205)
            elif times == 14 or times == 13:
                y_axis.append(float(i.split('\t')[1])+times*200)
            elif times == 19:
                y_axis.append(float(i.split('\t')[1])+times*190)
            elif times == 12:
                y_axis.append(float(i.split('\t')[1])+times*195)
            elif times == 0:
                y_axis.append(float(i.split('\t')[1])-100)
            else:
                y_axis.append(float(i.split('\t')[1])+times*200)

        
       #plt.plot(peaks, y_axis[peaks],'*')
        ax.plot(x_axis, y_axis,color=color)
        ax.text(700, y_axis[198]+40, Pressure,color=color)
        '''
        peaks, _ = find_peaks(y_axis[17:365],distance=25)
        for p in peaks:
            plt.plot(x_axis[p+17],y_axis[p+17],'*',color=color)
        '''
        
    plt.savefig('./Mo2C_I.png', dpi = 300, transparent = True)
    plt.show()
