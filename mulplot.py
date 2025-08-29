import pylab as plt

#plot 1:
x = [0, 1, 2, 3]
y = [3, 8, 1, 10]

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title('first')

#plot 2:
x = [0, 1, 2, 3]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title('second')
plt.suptitle('Main plot')
plt.show()