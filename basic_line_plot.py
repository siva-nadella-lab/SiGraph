import matplotlib.pyplot as plotter

squares = [1,4,9,16,25,36,49,64]
xaxis = [1,2,3,4,5,6,7,8]

plotter.style.use("tableau-colorblind10")
figure, axis = plotter.subplots()
axis.plot(xaxis, squares, linewidth=3)
axis.set_title("Squares", fontsize=24)
axis.set_xlabel("Numerics")
axis.set_ylabel("Squares of Numerics")
axis.tick_params(labelsize=14)



plotter.show()