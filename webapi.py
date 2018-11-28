# everything to do with api creation
from flask import Flask
import os
import kmlparserclass as k
import ray_casting as r
import lookup_table as table
from os import listdir
from os.path import isfile, join

os.chdir("/home/chenyu_shi/SpeciesLookup")
app = Flask(__name__)

# grabbing all the species names from kmz
onlyfiles = [f for f in listdir("range_shapefiles") if isfile(join("range_shapefiles", f))]
all_species = [name.split(",")[0] for name in onlyfiles if name]
grid_cells = table.create_table()


@app.route('/species_lookup/')
def api_root():
    instruction = """Welcome to Species Lookup web api! 
    Try formulate your query in this format( beagle.bnhm.berkeley.edu/species_lookup/search/[longitude,latitude]) to get proper result
    here's an example: beagle.bnhm.berkeley.edu/species_lookup/search/-122.264776,37.870871
    Note: do not add space between long and lat """
    return instruction


@app.route('/species_lookup/search/<points>')
def get(points):
    try:
        # parse input coordinates
        longa, lat = float(points.split(",")[0]), float(points.split(",")[1])
        i, j = table.grid_cell.array_index(longa, lat, (1, 1))
        point = r.points(longa, lat)
        cell = grid_cells[i][j]
        result = []
        for species in cell.species:
            par = k.parser(species)
            if par.inside(point):
                # check cached results to see if each specie's range map contains this point
                result.append(species)
        result.append("count: " + str(len(result)))
        return str(result), 200
    except:
        message = """unknown error, try beagle.berkeley.edu/species_lookup for instructions on query formatting"""
        return message, 400

if __name__ == '__main__':
    app.run()
