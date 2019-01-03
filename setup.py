from flask import Flask
import os
import lookup_table as table
from os import listdir
from os.path import isfile, join
import pickle

if __name__ == '__main__':
    os.chdir("/home/chenyu_shi/SpeciesLookup")

    # grabbing all the species names from kmz
    onlyfiles = [f for f in listdir("range_shapefiles") if isfile(join("range_shapefiles", f))]
    all_species = [name.split(",")[0] for name in onlyfiles if name]
    grid_cells = table.create_table()
    pickle.dump(grid_cells, "grid.p")



