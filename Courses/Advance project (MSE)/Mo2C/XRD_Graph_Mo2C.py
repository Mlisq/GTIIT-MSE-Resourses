import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import find_peaks

f = open('./XRD/Mo2C.dat')
contents = f.readlines()

fig, ax = plt.subplots(figsize = (20,10))

x_data = []
y_data = []

for i in contents:
    x_data.append(eval(i.split(' ')[0]))
    y_data.append(eval(i.split(' ')[1]))


ax.plot(x_data, y_data)
ax.set_xlabel('2θ(°)')
ax.set_ylabel('Intensity')
ax.set_title('Source - CU')
ax.set_ylim(0,51500)
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

peaks, _ = find_peaks(y_data,distance=150,prominence=2e+03)

for i in range(len(peaks)):
    if i in [6,12]:
        continue
    #ax.axvline(x = x_data[peaks[i]], ls='dashed',color='purple')
    ax.plot([x_data[peaks[i]], x_data[peaks[i]]],[2000, 0], color = '#1f77b4')
    print(x_data[peaks[i]])


peaks = [34.5, 38.1, 39.5, 52.3, 61.7, 69.6, 74.7, 75.7]

for i in peaks:
    ax.axvline(x = i, ls='dashed',color='red')


plt.legend()
plt.savefig('./XRD/Mo2C.png', dpi = 300, transparent = True)
plt.show()