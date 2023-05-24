import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks

FILE_PATH = "./data/"

f = open(FILE_PATH + "Mo2Ti2C3_5mw-3020_1200_4.05.asc")
contents = f.readlines()
f.close()

x_axis = []
y_axis = []

for i in contents:
    x_axis.append(float(i.split('\t')[0]))
    y_axis.append(float(i.split('\t')[1]))

fig, ax = plt.subplots(figsize = (20,10))

ax.set_title("Raman spectrum for the sample Mo2Ti2C3")
ax.set_xlabel("Ramanshift[cm-1]")
ax.set_ylabel("Intensity")
ax.set_xlim(0,1350)
ax.set_ylim(18400,20000)
ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(50))

peaks, _ = find_peaks(y_axis[0:770],distance=25)
for p in range(len(peaks)):
    if p in [2,3,4,6,8,10]:
        #ax.axvline(x_axis[peaks[p]],ls = 'dashed')
        ax.plot([x_axis[peaks[p]], x_axis[peaks[p]]],[18450, 18400], color = '#1f77b4')

ax.plot(x_axis,y_axis)
plt.savefig('./Mo2Ti2C3_Raman_4.05GPa.png', dpi = 300, transparent = True)
plt.show()