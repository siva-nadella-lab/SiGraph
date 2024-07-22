import matplotlib.pyplot as plotter
from random_walker import RandomWalker as RndWalkr
from settings import RandomWalkSettings as RndSettings

while True:

    settings = RndSettings()
    rWalker = RndWalkr(settings.plotPoints)
    rWalker.fillWalk()

    plotter.style.use(settings.plotStyle)
    figure,axis = plotter.subplots(figsize=(20,15), dpi=50)
    nOfPoints = range(rWalker.numPoints)

    #Trying plot instead of scatter
    if (settings.scatterType == 'line'):
        axis.plot(rWalker.xValues, rWalker.yValues, 12)

    # Plot all the points
    if (settings.scatterType == 'dot'):
        axis.scatter(rWalker.xValues, rWalker.yValues, c=nOfPoints, cmap=settings.gradientColor, s=settings.pointSize)
    #Plot the first; highlighted
    axis.scatter(0, 0, c=settings.startColor,edgecolors=settings.edgeColorNone, s=settings.startPointSize)
    #Plot the last; highlighted
    axis.scatter(rWalker.xValues[-1], rWalker.yValues[-1], c=settings.endColor, edgecolors=settings.edgeColorNone,s=settings.endPointSize)
    axis.set_aspect(settings.aspect)

    axis.get_xaxis().set_visible(settings.showAxis)
    axis.get_yaxis().set_visible(settings.showAxis)

    plotter.show()

    if (settings.runMultipleTimes):
        enoughAndStop = input("Press n to quit!")
        if (enoughAndStop == 'n'):
            break
    else:
        break