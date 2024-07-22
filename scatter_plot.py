import matplotlib.pyplot as plotter

# squares = [1,4,9,16,25,36,49,64]
# xaxis = [1,2,3,4,5,6,7,8]
x_axis = range(1, 1001)
squares = [x**2 for x in x_axis]

plotter.style.use('seaborn-v0_8-talk')
figure,axis = plotter.subplots()

# axis.scatter(x_axis,squares,color='red',s=10)
axis.scatter(x_axis,squares,c=squares, cmap=plotter.cm.Greens,s=10) #Gradient coloring of scatter plot along an axis values

axis.set_title('Scatter Plotter', fontsize=24)
axis.set_xlabel('X Plot', fontsize=15)
axis.set_ylabel('Y Plot', fontsize=20)
axis.ticklabel_format(style='plain')

#Setting the axis range; First two are for X-Axis and the remaining two are for Y-Axis
axis.axis([0,1100, 0, 1_100_000])

#Saving the image into the file system
plotter.savefig('1.png', bbox_inches='tight')

#Plotting the image on to a viewer
plotter.show()

