from random import choice

class RandomWalker:
    ## A class to random walk...

    def __init__(self, numPoints=5000):
        self.numPoints = numPoints

        self.xValues = [0]
        self.yValues = [0]

    def fillWalk(self):

        while len(self.xValues) < self.numPoints:

            x_step = self.getStep()
            y_step = self.getStep()

            if (x_step == 0 and y_step ==0):
                continue

            x = self.xValues[-1] + x_step
            y = self.yValues[-1] + y_step

            self.xValues.append(x)
            self.yValues.append(y)

    def getStep(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction * distance

        return step