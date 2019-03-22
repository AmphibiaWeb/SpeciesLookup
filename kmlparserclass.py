# This file parses kmz files and creates a parser instance for each specie
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
import ray_casting as r
import xml.etree.ElementTree as ET
from zipfile import ZipFile


class parser:
    namespace = "{http://www.opengis.net/kml/2.2}"
    Use_KML = False

    def __init__(self, scientific_name):
        self.scientific_name = scientific_name
        # we used to kmz not kmls are no longer supported
        if self.Use_KML:
            self.kml_path = self.find_kml(scientific_name)
            self.read_in_polygons_from_kml()
        else:
            self.kmz_path = self.find_kmz(scientific_name)
            self.read_in_polygons_from_kmz()

    def find_kmz(self, scientific_name):
        return "range_shapefiles/" + scientific_name + ".kmz"

    def read_in_polygons_from_kmz(self):
        with ZipFile(self.kmz_path) as myzip:
            with myzip.open('doc.kml') as myfile:
                root = ET.fromstring(myfile.read())
        # finding family name
        description = root.findall(".//{}description".format(self.namespace))[1].text
        index = description.find("family_nam")
        # brute force string manipulation
        self.family = description[index:].split("<td>")[1].split("</td>")[0].lower()

        index = description.find("class_name")
        # brute force string manipulation
        self.class_name = description[index:].split("<td>")[1].split("</td>")[0].lower()

        index = description.find("order_name")
        # brute force string manipulation
        self.order = description[index:].split("<td>")[1].split("</td>")[0].lower()

        # url formatting
        genus, sp = self.scientific_name.split("_")
        self.url = "https://amphibiaweb.org/cgi/amphib_query?where-genus={}&where-species={}".format(genus,sp)
        # polygon manipulation
        polys = root.findall(".//{0}Polygon".format(self.namespace))
        self.outer = []
        self.inner = []
        for each_polygon in polys:
            outer = each_polygon.findall(".//{0}outerBoundaryIs".format(self.namespace))
            inner = each_polygon.findall(".//{0}innerBoundaryIs".format(self.namespace))
            for each in outer:
                cords = self.find_coordinates(each)
                good = self.format_vertices(cords)
                self.outer.append(good)

            for each in inner:
                cords = self.find_coordinates(each)
                good = self.format_vertices(cords)
                self.inner.append(good)
        self.min_x = min([min([cord[0] for cord in shape]) for shape in self.outer])
        self.max_x = max([max([cord[0] for cord in shape]) for shape in self.outer])
        self.min_y = min([min([cord[1] for cord in shape]) for shape in self.outer])
        self.max_y = max([max([cord[1] for cord in shape]) for shape in self.outer])

    # this method is no longer used
    def read_in_polygons_from_kml(self):
        root = ET.parse(self.kml_path).getroot()
        polys = root.findall(".//{0}Polygon".format(self.namespace))
        self.outer = []
        self.inner = []
        for each_polygon in polys:
            outer = each_polygon.findall(".//{0}outerBoundaryIs".format(self.namespace))
            inner = each_polygon.findall(".//{0}innerBoundaryIs".format(self.namespace))
            for each in outer:
                cords = self.find_coordinates(each)
                good = self.format_vertices(cords)
                self.outer.append(good)

            for each in inner:
                cords = self.find_coordinates(each)
                good = self.format_vertices(cords)
                self.inner.append(good)
        self.min_x = min([min([cord[0] for cord in shape]) for shape in self.outer])
        self.max_x = max([max([cord[0] for cord in shape]) for shape in self.outer])
        self.min_y = min([min([cord[1] for cord in shape]) for shape in self.outer])
        self.max_y = max([max([cord[1] for cord in shape]) for shape in self.outer])

    # this method should only be used for debugging. It visualizes the range map
    def visualize(self, point=None):
        outer_patches = []
        inner_patches = []

        for good in self.outer:
            polygon = Polygon(good, closed=True)
            outer_patches.append(polygon)
        for ps in self.inner:
            polygon = Polygon(good, closed=True)
            inner_patches.append(polygon)

        fig, ax = plt.subplots()
        o = PatchCollection(outer_patches, cmap=matplotlib.cm.jet, alpha=0.4)
        i = PatchCollection(inner_patches, cmap=matplotlib.cm.jet, alpha=0.6)
        ax.add_collection(o)
        ax.add_collection(i)

        if point:
            plt.plot([point.x], [point.y], 'ro')

        plt.axis([self.min_x, self.max_x, self.min_y, self.max_y])
        plt.show()

    def find_kml(self, scientific_name):
        return "kml/" + scientific_name + ".kml/doc.kml"

    def find_coordinates(self, boundary_node):
        in_str_form = boundary_node[0][0].text
        after_space_split = in_str_form.split(" ")
        after_comma_split = [triple.split(',') for triple in after_space_split if len(triple.split(',')) == 3]
        return after_comma_split

    def format_vertices(self, arr):
        # take off the elevation data and convert everything to float
        return np.array([[float(arr[i][0]), float(arr[i][1])] for i in range(len(arr))])

    def inside(self, query_point):
        # This takes in the point object and checks to see if rangemap intersects the query point
        if query_point.x < self.min_x or query_point.x > self.max_x or query_point.y < self.min_y or query_point.y > self.max_y:
            return False
        a = False
        b = False
        for good in self.outer:
            ps = [r.points(dot[0], dot[1]) for dot in good]
            poly = r.polygon(ps)
            if poly.is_inside(query_point):
                a = True
        for good in self.inner:
            ps = [r.points(dot[0], dot[1]) for dot in good]
            poly = r.polygon(ps)
            if poly.is_inside(query_point):
                b = True
        return a and not b

