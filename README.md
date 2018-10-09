# Species Lookup
Aim: create a service to generate a list of species expected to occur at a given point based on range maps (polygon intersections)
## File structure
debug.py tests the kmlparserclass.py functions locally

kmlparserclass.py contains all the functions needed to read in and process kml files

ray_casting.py implements the ray casting method

updater.py still needs more work but it contains function to update range maps on a regular basis

viz.py visualizes range maps and query points. 

webapi.py puts everything together into a web service 

