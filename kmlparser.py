# This should read in all the kml range maps and pass them to ray_casting module
# kml documentation comes from here https://fastkml.readthedocs.io/en/latest/usage_guide.html#read-a-kml-file-string
import ray_casting as rc
from fastkml import kml

kml_file="kml/Acanthixalus_sonjae.kml/doc.kml"
with open(kml_file, 'rt') as myfile:
    doc=myfile.read()
k = kml.KML()

# Read in the KML string
k.from_string(doc)
# waiting for kml files to upload
