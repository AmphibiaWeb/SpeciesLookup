# everything to do with api creation
from flask import Flask, current_app, jsonify
import os
import kmlparserclass as k
import ray_casting as r
import lookup_table as table
import pickle

os.chdir("/home/chenyu_shi/SpeciesLookup")
app = Flask(__name__, static_url_path='/static')

file_Name = "gridtable"
fileObject = open(file_Name, 'rb')
grid_cells = pickle.load(fileObject)
fileObject.close()

@app.route('/')
def home():
    return current_app.send_static_file("index.html")

@app.route('/about/')
def api_root():
    """

    :return: instruction on how to use this
    """
    instruction = """Welcome to Species Lookup web api! 
    Try formulate your query in this format( specieslookup.berkeley.edu/search/[longitude,latitude]) to get proper result
    here's an example: specieslookup.berkeley.edu/search/-122.264776,37.870871
    Note: do not add space between long and lat """
    return instruction


@app.route('/search/<points>')
def get(points):
    """

    :param points: (long,lat)
    :return: a count of species and their scientific names
    """
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
        message = """unknown error, try specieslookup.berkeley.edu/about/ for instructions on query formatting"""
        return message, 400

@app.route('/search_json/<points>')
def get(points):
    """

    :param points: (long,lat)
    :return: a count of species and their scientific names
    """
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
        return jsonify(species=result, length=len(result)), 200
    except:
        message = """unknown error, try specieslookup.berkeley.edu/about/ for instructions on query formatting"""
        return message, 400

if __name__ == '__main__':
    app.run()
