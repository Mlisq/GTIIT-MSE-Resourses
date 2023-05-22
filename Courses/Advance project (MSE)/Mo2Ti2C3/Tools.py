import matplotlib.pyplot as plt
import numpy as np

def PrintGraph(arrayX, arrayY, labelX, labelY, title='Graph'):
    plt.plot(arrayX, arrayY,label=title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.legend()
    plt.savefig(title+'.png')
    plt.show()

def convertQ(arrayX, sourceWl):
    result = []
    for i in arrayX:
        result.append(
            ((4*np.pi)/sourceWl)*
            np.sin((i/2)*(np.pi/180))
        )
    return result
