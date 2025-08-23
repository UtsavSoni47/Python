import pylab as uk

x = [1, 2, 3, 4]
y = [3, 8, 1, 10]
uk.plot(x, y, ls='dotted')
font1={'family':'curlz MT','color':'blue','size':20}
uk.title('example',fontdict=font1)
uk.xlabel('X')
uk.ylabel('Y')
uk.grid()
uk.show()
