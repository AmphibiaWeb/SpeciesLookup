# This should read in all the kml range maps and pass them to ray_casting module
# kml documentation comes from here https://docs.python.org/3/library/xml.etree.elementtree.html
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
import ray_casting as r
import xml.etree.ElementTree as ET

kml_file="kml/Acanthixalus_sonjae.kml/doc.kml"
root=ET.parse(kml_file).getroot()

doc=root[0]
scientific_name=doc[0].text
namespace="{http://www.opengis.net/kml/2.2}"

def find_coordinates(boundary_node):
    # indexing into linear ring and coordinates
    return boundary_node[0][0].text

def format_vertices(arr):
    return np.array([[arr[i*3],arr[i*3+1]] for i in range(len(arr)//3)])

polys=root.findall(".//{0}Polygon".format(namespace))
for each_polygon in polys:
    outer=each_polygon.findall(".//{0}outerBoundaryIs".format(namespace))
    inner=each_polygon.findall(".//{0}innerBoundaryIs".format(namespace))
    for each in outer:
        cords=find_coordinates(each)
        
        good=format_vertices(cords)
        ps=[r.points(dot[0],dot[1]) for dot in good]
        poly=r.polygon(ps)
        test=r.points(0.4,0.9)
        fig,ax=plt.subplots()
    
        patches=[]
        num_polygon=1
        print(cords)
        polygon=Polygon(cords,closed=True)
        patches.append(polygon)
        p=PatchCollection(patches,cmap=matplotlib.cm.jet,alpha=0.4)
        
        ax.add_collection(p)
        plt.plot([test.x],[test.y],'ro')
        plt.title("tested point ("+str(test.x)+" ,"+str(test.y)+
            ") is contained in polygon"+str(poly.is_inside(test)))
        plt.show()
    for each in inner:
        coords=find_coordinates(each)
        
    