# implementation of ray_casting algorithm
class points:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class edge:

    def __init__(self, pointa, pointb):
        self.a = pointa
        self.b = pointb

    def intersect(self, point):
        # I am assuming the ray always goes straight down along x = point.x line
        hit = 0
        # ray casting method here
        # The edge is entirely left of the point
        if min(self.a.x, self.b.x) > point.x:
            return hit
        # The edge is entirely right of the point
        if max(self.a.x, self.b.x) < point.x:
            return hit

        # This is for a vertical edge
        if self.b.x == self.a.x:
            # tangents are not counted as inside the polygon
            return 0
        projected_y = self.a.y + (self.b.y - self.a.y) / (self.b.x - self.a.x) * (point.x - self.a.x)
        if projected_y <= point.y:
            # ignore the right point if the query point is right on top of it.
            if point.x == max(self.a.x, self.b.x):
                # Have to account for overcounting
                hit = 0
                return hit
            else:
                hit = 1
                return hit
        else:
            return hit


class polygon:

    def __init__(self, points):
        # convert points to a list of edges
        self.edges = [edge(points[i], points[(i + 1) % len(points)]) for i in range(len(points))]

    def is_inside(self, query_point):
        hits = sum([edge.intersect(query_point) for edge in self.edges])
        if hits % 2 == 1:
            # odd number of intersections
            return True
        else:
            return False
