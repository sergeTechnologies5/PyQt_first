import time
import psutil
import matplotlib.pyplot as plt

#matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x,y = [],[]
psutil.cpu_percent()

while 1:
    x.append(i)
    y.append(psutil.cpu_percent())
    ax.plot(x,y,color='b')
    fig.canvas.draw()
    ax.set_xlim(left=max(0,i-50),right=i+50)
    time.sleep(0.1)
    i+=1