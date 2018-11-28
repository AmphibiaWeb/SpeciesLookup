# this is debugging for lookup_table
# need to create the class that filters request 
import kmlparserclass as k 
from ray_casting import points
aspecie = k.parser("Adenomera_ajurauna")
point=points(-46.5,-23.825)
aspecie.visualize(point)

print(aspecie.inside(point))