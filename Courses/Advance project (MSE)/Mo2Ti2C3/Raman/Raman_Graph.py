import matplotlib.pyplot as plt
import os
import random

FILE_PATH = "./data/"

if __name__ == '__main__':

    files = os.listdir(FILE_PATH)
    files.sort(key=lambda x:float(x.split('_')[3][:-4]))

    fig, ax = plt.subplots(figsize = (20,10))

    ax.set_title("Increasing Process")
    ax.set_xlabel("Ramanshift[cm-1]")
    ax.set_ylabel("Intensity")
    ax.set_xlim(0,1300)
    ax.set_ylim(18200,22000)

    for times, file in enumerate(files):
        if file == "Mo2Ti2C3_5mw-3020_1200_4.05.asc":
            continue
        #print
        Pressure = file.split('_')[3][:-4] + "GPa"
        print(Pressure)
        color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        
        x_axis = []
        y_axis = []
        
        f = open(FILE_PATH + file)
        contents = f.readlines()
        f.close()
        
        for i in contents:

            x_axis.append(float(i.split('\t')[0]))
            #if times == 2:
                #y_axis.append(float(i.split('\t')[1])+times*200)
            #else:
            y_axis.append(float(i.split('\t')[1])+times*400)

        
       #plt.plot(peaks, y_axis[peaks],'*')
        ax.plot(x_axis, y_axis,color=color)
        ax.text(700, y_axis[580]+80, Pressure,color=color)

    #plt.savefig('./Mo2T2C3_I.png', dpi = 300, transparent = True)    
    plt.show()
