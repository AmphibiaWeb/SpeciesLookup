class points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class edge:
    def __init__(self,pointa,pointb):
        self.a=pointa
        self.b=pointb
    def intersect(self,point):
        # Let's assume the ray always goes straight down
        hit = 0
        # ray casting method here
        return hit
    
class polygon:
    def __init__(points):
        # convert points to a list of edges
        self.edges=["to do"]
    def is_inside(query_point):
        hits=sum([edge.intersect(query_point) for edge in self.edges])
        if hits%2==1:
            # odd number of intersections
            return True
        return False
