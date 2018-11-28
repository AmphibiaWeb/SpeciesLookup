# testing out the web api functions 
import os 
import time 
import kmlparserclass as k
import ray_casting as r
import lookup_table as table 

all_species = [name.split('.')[0] for name in list(os.walk('range_shapefiles'))[0][2] if name]
start = time.clock()
grid_cells = table.create_table()
end = time.clock()
print(end-start," seconds for updating grid")
# print(grid_cells)
points="-63.043301,-2.217128"

count = [[len(cell.species) for cell in row]for row in grid_cells]
print(sum([sum(row) for row in count]))

start = time.clock()
print(points)
longa, lat = float(points.split(",")[0]),float(points.split(",")[1])        
i,j = table.grid_cell.array_index(longa,lat,(1,1))
print(i,j)
point = r.points(longa,lat)
cell = grid_cells[i][j]
result = []
for species in cell.species: 
    par = k.parser(species)
    if par.inside(point):
        result.append(species)

stop = time.clock()
print(str(stop-start))
print(result)