import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks

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


contents = readFile('decomp_457nm_15mw_force2_3020_0.68GPa_2.asc',0)

x_axis = []
y_axis = []

for i in contents:
    x_axis.append(float(i.split('\t')[0]))
    y_axis.append(float(i.split('\t')[1]))

fig, ax = plt.subplots(figsize = (20,10))

ax.set_title("Raman spectrum for the sample Mo2C",fontsize = 15)
ax.set_xlabel("Ramanshift[cm-1]",fontdict={'size':15})
ax.set_ylabel("Intensity",fontdict={'size':15})
#ax.set_xlim(20,1300)
#ax.set_ylim(18200,19000)
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))
ax.yaxis.set_ticks([])
ax.xaxis.set_tick_params(labelsize = 15)
'''
peaks, _ = find_peaks(y_axis[17:365],distance=25)
for p in range(len(peaks)):
    if p in [0,1,3]:
        ax.axvline(x_axis[peaks[p]+17],ls = 'dashed')
        #ax.plot([x_axis[peaks[p]+17], x_axis[peaks[p]+17]],[18230, 18200], color = '#1f77b4')
'''
ax.plot(x_axis,y_axis)

plt.savefig('./Mo2C_Raman_All.png', dpi = 300, transparent = True)
plt.show()