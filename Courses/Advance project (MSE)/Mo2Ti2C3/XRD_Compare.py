import matplotlib.pyplot as plt

from Tools import convertQ


CU_SOURCE = 1.5406
ANOTHER = 0.494590
Pressures = ['1.0GPA','3.7GPA','6.9GPA','9.8GPA','12.0GPA','15.1GPA',
             '20.2GPA','24.5GPA','28.0GPA','30.0GPA','33.5GPA','36.8GPA',
             '32.0GPA']
FILENAME = ""

plt.figure(figsize = (20,10))
plt.xlabel('Q(A-1)')
plt.ylabel('Intensity')

for i in range(13):
    FILENAME = 'P'+str(i)+'  0001.dat'
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
    plt.plot(convertQ(x_axis,ANOTHER),y_axis)
    plt.text(6.58,y_axis[-1],Pressures[i])

FILENAME = 'Mo2Ti2C3_Si.dat'
file = open(FILENAME,"r")
content = file.readlines()
file.close()

x_axis = []
y_axis = []
q_x = []

for j in content:
    x_axis.append(eval(j.split(' ')[0]))
    y_axis.append(eval(j.split(' ')[1])*0.08)


plt.plot(convertQ(x_axis,CU_SOURCE),y_axis,label="Individual Sample")

plt.legend()
plt.savefig('XRD-Compare.png',transparent=True, dpi=200)
plt.show()

