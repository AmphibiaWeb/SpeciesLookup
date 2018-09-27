# This should read in all the kml range maps and pass them to ray_casting module
# kml documentation comes from here https://docs.python.org/3/library/xml.etree.elementtree.html
import ray_casting as rc
import xml.etree.ElementTree as ET

kml_file="kml/Acanthixalus_sonjae.kml/doc.kml"
root=ET.parse(kml_file).getroot()

doc=root[0]
scientific_name=doc[0].text
namespace="{http://www.opengis.net/kml/2.2}"
def find_coordinates(boundary_node):
    # indexing into linear ring and coordinates
    return boundary_node[0][0].text
polys=root.findall(".//{0}Polygon".format(namespace))
for each_polygon in polys:
    outer=each_polygon.findall(".//{0}outerBoundaryIs".format(namespace))
    inner=each_polygon.findall(".//{0}innerBoundaryIs".format(namespace))
    for each in outer:
        cords=find_coordinates(each)
        
    for each in inner:
        coords=find_coordinates(each)
        
    