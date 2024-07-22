
class RandomWalkSettings:
    
    def __init__(self) -> None:
        self.startColor = 'red'
        self.endColor ='orange'
        self.gradientColor='twilight_shifted_r'
        self.startPointSize=150
        self.endPointSize=150
        self.pointSize=1
        self.aspect='equal'
        self.edgeColorNone='none'
        self.plotStyle='classic'
        self.showAxis=False
        self.runMultipleTimes=False
        self.plotPoints=50_000
        self.scatterType='dot' #dot/line