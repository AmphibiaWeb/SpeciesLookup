import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
import ray_casting as r

coord=np.array([[0.2,0.2],[0.2,0.9],[0.9,0.2]])
test=r.points(0.3,0.5)

ps=[r.points(dot[0],dot[1]) for dot in coord]
poly=r.polygon(ps)

fig,ax=plt.subplots()

patches=[]
num_polygon=1
polygon=Polygon(coord,closed=True)
patches.append(polygon)
p=PatchCollection(patches,cmap=matplotlib.cm.jet,alpha=0.4)

ax.add_collection(p)
plt.plot([test.x],[test.y],'ro')
plt.title("tested point ("+str(test.x)+" ,"+str(test.y)+
    ") is contained in polygon"+str(poly.is_inside(test)))
plt.show()
