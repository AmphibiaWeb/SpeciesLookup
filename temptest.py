# testing out the web api functions 
import os 
import time 
import kmlparserclass as k
import ray_casting as r
import lookup_table as table 

all_species = [name.split('.')[0] for name in next(os.walk('kml'))[1] if name]

grid_cells = table.create_table()
# print(grid_cells)
points="-122.258423,37.871853"
start = time.clock()
print(points)
longa, lat = float(points.split(",")[0]),float(points.split(",")[1])        
i,j = table.grid_cell.array_index(longa,lat,(4,2))
print(i,j)
point = r.points(longa,lat)
cell = grid_cells[i][j]
result = []
for species in cell.species: 
    par = k.parser(species)
    if par.inside(point):
        result.append(species)

stop = time.clock()
print(stop-start)
print(result)