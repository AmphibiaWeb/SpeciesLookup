class points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class edge:
    def __init__(self,pointa,pointb):
        self.a=pointa
        self.b=pointb
    def intersect(self,point):
        # ray casting method here 
