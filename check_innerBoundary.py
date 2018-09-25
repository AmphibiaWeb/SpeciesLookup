import os
folders=list(os.walk(os.getcwd()))
folders=[fol[0] for fol in folders if 'kml' in fol[0] and '_' in fol[0]]

for each in folders:
    with open(each+'\\doc.kml','r') as myfile:
        data=myfile.read()
        if "innerBoundary" in data:
            print("find one inner boundary in ",each)
        
    
print("There are exactly seven files that have inner boundaries. This could make things complicated")
