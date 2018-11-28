from zipfile import ZipFile 

with ZipFile('Ambystoma_andersoni.kmz') as myzip:
    print(myzip.printdir())
    print(myzip.extractall())
    
    #with myzip.open('doc.kml') as myfile:
    #    print(type(myfile.read()))