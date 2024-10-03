import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axis import Axis


if __name__ == "__main__" :
   fig, ax = plt.subplots(figsize=(9,3))
   ax.spines['right'].set_color('none')
   ax.spines['top'].set_color('none')
   ax.xaxis.set_ticks_position('bottom')
   ax.yaxis.set_ticks_position('left')
   ax.spines['bottom'].set_position(('data', 0))
   ax.spines['left'].set_position(('data', -1))
   XPOINTS = np.array(['A', 'B', 'C', 'D', 'E'])
   XPOINTS=XPOINTS.reshape((5,))
   xs = np.linspace(0,20,5)
   ax.set_xticks(xs, labels = XPOINTS)
   y1 = [7.23, 5.67, 3.5, 2.72, 2.8]
   y2 = [11.55, 4.51, 2.42,	1.8, 1.05]
   plt.xlim(-1, 21)
   plt.ylim(-1, 21)
   plt.plot(xs, y1, color = 'red', label = 'e_э')
   plt.plot(xs, y2, color = 'blue', label ='e_расч')
   plt.annotate('', xy = (21, 0),xytext=(-1, 0),arrowprops = dict(arrowstyle = "->",color = 'black'))
   plt.annotate('', xy = (-1, 21),xytext=(-1, 0),arrowprops = dict(arrowstyle = "->",color = 'black'))
   plt.xlabel('мм', loc = "right" , labelpad = -3)
   plt.ylabel("N", loc = "top", rotation = 180, labelpad = 13)
   plt.legend(loc='upper right', frameon = False)
   plt.title("Графики e_э, e_расч в точках")
   if y1:
      for x, y in zip(xs, y1):
         plt.plot(x, y, 'o', markersize = 4)       
   if y2:
      for x, y in zip(xs, y2): 
         plt.plot(x, y, 'o', markersize = 4)
   ax.set_xlim(left=-1, right=21)  # Ограничиваем длину оси X
   ax.set_ylim(bottom=0, top=21)   # Ограничиваем длину оси Y выше 0
   plt.grid()
   plt.show()