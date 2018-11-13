# everything to do with api creation
from flask import Flask
#from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

import time
import kmlparserclass as k
import ray_casting as r
import lookup_table as table
import os
from os import listdir
from os.path import isfile, join
os.chdir("/home/pi/Desktop/SpeciesLookup")
onlyfiles = [f for f in listdir("range_shapefiles") if isfile(join("range_shapefiles", f))]

all_species = [name.split(",")[0] for name in onlyfiles if name]

grid_cells = table.create_table()
os.chdir("/home/pi/Desktop/SpeciesLookup")

# print(grid_cells)

@app.route('/')
def api_root():
    return "Welcome to Species Lookup"

@app.route('/species_lookup/<points>')
def get(points):
    start = time.clock()
    longa, lat = float(points.split(",")[0]), float(points.split(",")[1])
    i, j = table.grid_cell.array_index(longa, lat, (1, 1))
    point = r.points(longa, lat)
    cell = grid_cells[i][j]
    result = []
    for species in cell.species:
        par = k.parser(species)
        if par.inside(point):
            result.append(species)
    stop = time.clock()
    print(stop - start)
    result.append("count: " + str(len(result)))
    return str(result), 200



if __name__ == '__main__':
    app.run(debug=True)
