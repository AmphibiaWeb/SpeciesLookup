# this script should create lookup tables for individual range maps
import os
import time
import kmlparserclass as k


class grid_cell:

    def __init__(self, left_top_long, left_top_lat, right_bottom_long, right_bottom_lat):
        self.left_top_long = left_top_long
        self.left_top_lat = left_top_lat
        self.right_bottom_long = right_bottom_long
        self.right_bottom_lat = right_bottom_lat
        self.species = []
        # static method here

    def chop(long_range, lat_range, interval):
        cells = []
        cells_in_grid = [None] * (360 // interval[0] - 1)
        for i in range(360 // interval[0] - 1):
        	cell_array = [None] * (180 // interval[1] - 1)
        	cells_in_grid[i] = cell_array
	        for j in range(180 // interval[1] - 1):
                
                # add a grid cell
        	    cell = grid_cell(-180 + i * interval[0], -90 + (j + 1) * interval[
                             1], -180 + (i + 1) * interval[0], -90 + j * interval[1])
       		    cells.append(cell)
       		    cell_array[j] = cell 
        return cells,cells_in_grid

    def add_species(self, scientific_name):
        self.species.append(scientific_name)

    def array_index(longa, lat, interval):
        # this should return the index for the cells array
        return (longa+180)//interval[0],(lat+90)//interval[1]

def create_table(long_interval=4, lat_interval=2):
    # what we are going to return
    long_range = (-180, 180)
    lat_range = (-90, 90)

    if 360 % long_interval or 180 % lat_interval:
        raise ValueError("inappropriate interval values!")
        # feel free to change it but make sure long and lat interval can divide
        # 360 and 180

    interval = (long_interval, lat_interval)

    cells,cells_in_grid = grid_cell.chop(long_range, lat_range, interval)

    # grid cells are divided into
    all_species = [name.split('.')[0]
                   for name in next(os.walk('kml'))[1] if name]
    parsers = [k.parser(specie) for specie in all_species]

    for cell in cells:
        for parser in parsers:
            if parser.min_x > cell.right_bottom_long or parser.max_x < cell.left_top_long or parser.min_y > cell.left_top_lat or parser.max_y < cell.right_bottom_lat:
                pass
            else:
                cell.add_species(parser.scientific_name)
        print("cell coordinates are (", cell.left_top_long, " ,", cell.left_top_lat,
              "), (", cell.right_bottom_long, " ,", cell.right_bottom_lat, ")")
        print("Species occurring in this regions are :", cell.species)
    return cells_in_grid
    #
#start = time.clock()
#create_table()
# possibly dump this into a json file
#stop = time.clock()
#print("total runtime is ", stop - start)
