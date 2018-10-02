import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
import ray_casting as r
import xml.etree.ElementTree as ET
class parser:

    namespace="{http://www.opengis.net/kml/2.2}"

    def __init__(self,scientific_name):
        self.scientific_name = scientific_name
        self.kml_path = self.find_kml(scientific_name)
        self.read_in_polygons_from_kml()

    def read_in_polygons_from_kml(self):
        root=ET.parse(self.kml_path).getroot()
        polys=root.findall(".//{0}Polygon".format(namespace))
        self.outer=[]
        self.inner=[]
        for each_polygon in polys:
            outer=each_polygon.findall(".//{0}outerBoundaryIs".format(namespace))
            inner=each_polygon.findall(".//{0}innerBoundaryIs".format(namespace))
            for each in outer:
                cords=find_coordinates(each)
                good=format_vertices(cords)
                ps=[r.points(dot[0],dot[1]) for dot in good]
                self.outer.append(ps)

            for each in inner:
                cords=find_coordinates(each)
                good=format_vertices(cords)
                ps=[r.points(dot[0],dot[1]) for dot in good]
                self.inner.append(ps)

    // # TODO: visualize the range map
    def visualize(self,point=None):

        poly=r.polygon(ps)
        test=r.points(-2.6,5.27)
        fig,ax=plt.subplots()
        patches=[]
        num_polygon=1
        polygon=Polygon(good,closed=True)
        patches.append(polygon)
        p=PatchCollection(patches,cmap=matplotlib.cm.jet,alpha=0.4)
        ax.add_collection(p)
        plt.plot([test.x],[test.y],'ro')
        plt.title("tested point ("+str(test.x)+" ,"+str(test.y)+
                    ") is contained in polygon"+str(poly.is_inside(test)))
        plt.show()


    def find_kml(self,scientific_name):
        return "kml/"+scientific_name+".kml/doc.kml"

    def find_coordinates(self,boundary_node):
        in_str_form= boundary_node[0][0].text
        after_space_split=in_str_form.split(" ")
        after_comma_split=[triple.split(',') for triple in after_space_split if len(triple.split(','))==3]
        return after_comma_split

    def format_vertices(self,arr):
        # take off the elevation data and convert everything to float
        return np.array([[float(arr[i][0]),float(arr[i][1])] for i in range(len(arr))])

    // # TODO:
    def inside(self,query_point):
        return True
