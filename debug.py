# This tests the ray_casting module
import os 
import kmlparserclass as k
import ray_casting as r
point=r.points(-7.2,6)
par = k.parser("Acanthixalus_sonjae")
par.visualize(point)

print(par.inside(point))
