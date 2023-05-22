import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks

FILENAME = './data/Mo2Ti2C3_Si.dat'
file = open(FILENAME,"r")
content = file.readlines()
file.close()

x_axis = []
y_axis = []


for j in content:
    x_axis.append(eval(j.split(' ')[0]))
    y_axis.append(eval(j.split(' ')[1]))


fig, ax = plt.subplots(figsize = (20,10))


peaks, _ = find_peaks(y_axis,distance=150,prominence=2e+03)

for i in range(len(peaks)):
    
    #ax.axvline(x = x_data[peaks[i]], ls='dashed',color='purple')
    ax.plot([x_axis[peaks[i]], x_axis[peaks[i]]],[1000, 0], color = '#1f77b4')
    print(x_axis[peaks[i]])

ax.plot(x_axis, y_axis)
ax.set_xlabel('2θ(°)')
ax.set_ylabel('Intensity')
ax.set_title('Source - CU')
ax.set_ylim(0,30000)
ax.set_xlim(0,90)

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

plt.savefig('./Mo2Ti2C3.png', dpi = 300, transparent = True)
plt.show()