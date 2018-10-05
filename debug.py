# This tests the ray_casting module
import os 
import time 
import kmlparserclass as k
import ray_casting as r
point=r.points(-7.2,6)
all_species = [name.split('.')[0] for name in next(os.walk('kml'))[1] if name]

accoutants = [k.parser(specie) for specie in all_species]

start = time.clock()
result = [account.scientific_name for account in accoutants if account.inside(point)]
stop = time.clock()
print(stop-start)
print(result)