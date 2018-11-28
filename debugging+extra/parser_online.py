# This file pulls the newest shapefiles and update the current record
###
### Unused file
###

import requests as re 
import kmlparerclass as k
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import numpy as np
import ray_casting as r
import xml.etree.ElementTree as ET

def online_parser(k.parser):
	url = ''

	def __init__(self,scientific_name):
		k.parser.__init__(self,scientific_name)
		make_url()

	def make_url(self):
		self.url = ""

	def read_inpolygons_from_kml(self):
		try:
			# hopefully this gets a string 
			response = re.get(url)
			root=ET.parse(response.txt).getroot()
	        polys=root.findall(".//{0}Polygon".format(self.namespace))
	        self.outer=[]
	        self.inner=[]
	        for each_polygon in polys:
	            outer=each_polygon.findall(".//{0}outerBoundaryIs".format(self.namespace))
	            inner=each_polygon.findall(".//{0}innerBoundaryIs".format(self.namespace))
	            for each in outer:
	                cords=self.find_coordinates(each)
	                good=self.format_vertices(cords)
	                self.outer.append(good)

	            for each in inner:
	                cords=self.find_coordinates(each)
	                good=self.format_vertices(cords)
	                self.inner.append(good)
	        self.min_x = min([min([cord[0] for cord in shape]) for shape in self.outer])
	        self.max_x = max([max([cord[0] for cord in shape]) for shape in self.outer])
	        self.min_y = min([min([cord[1] for cord in shape]) for shape in self.outer])
	        self.max_y = max([max([cord[1] for cord in shape]) for shape in self.outer])
	        
		except: 
			k.parser.read_in_polygons_from_kml(self)
			print("read local data, check internet connection!")
