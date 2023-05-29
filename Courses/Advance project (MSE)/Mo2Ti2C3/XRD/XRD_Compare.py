import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from Tools import convertQ


CU_SOURCE = 1.5406
ANOTHER = 0.494590
Pressures = ['1.0GPA','3.7GPA','6.9GPA','9.8GPA','12.0GPA','15.1GPA',
             '20.2GPA','24.5GPA','28.0GPA','30.0GPA','33.5GPA','36.8GPA',
             '32.0GPA']
Path = "./data/"


fig, ax = plt.subplots(figsize = (20,10))

ax.set_title("XRD in Q scale",fontsize = 15)
ax.set_xlabel("Q(A-1)",fontdict={'size':15})
ax.set_ylabel("Intensity",fontdict={'size':15})

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_tick_params(labelsize = 15)
ax.yaxis.set_ticks([])

for i in range(13):
    FILENAME = Path + 'P'+str(i)+'  0001.dat'
    file = open(FILENAME,"r")
    content = file.readlines()
    file.close()
    
    x_axis = []
    y_axis = []
    q_x = []

    for j in content:
        x_axis.append(eval(j.split('  ')[0]))
        y_axis.append(eval(j.split('  ')[1])+(i+1)*1000)
    
    #plt.plot(convertQ(x_axis,ANOTHER),y_axis,label=Pressures[i])
    ax.plot(convertQ(x_axis,ANOTHER),y_axis)
    ax.text(7,y_axis[-1],Pressures[i],fontdict={'size' : 15})

FILENAME = Path + 'Mo2Ti2C3_Si.dat'
file = open(FILENAME,"r")
content = file.readlines()
file.close()

x_axis = []
y_axis = []
q_x = []

for j in content:
    x_axis.append(eval(j.split(' ')[0]))
    y_axis.append(eval(j.split(' ')[1])*0.08)


ax.plot(convertQ(x_axis,CU_SOURCE),y_axis,label="Individual Sample")

plt.legend()
plt.savefig('XRD-Compare.png',transparent=True, dpi=200)
plt.show()

