from zipfile import ZipFile 

with ZipFile('Acanthixalus_sonjae.kmz') as myzip:
    with myzip.open('doc.kml') as myfile:
        print(type(myfile.read()))