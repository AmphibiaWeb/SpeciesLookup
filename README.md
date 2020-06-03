# Species Lookup
Aim: create a service to generate a list of species expected to occur at a given point based on range maps (polygon intersections)    
Credit: conceived and written by Chenyu Shi (@Chenyu-Shi), undergraduate apprentice at the Museum of Vertebrate Zoology

#Archived!
Please see its active home at: [BNHM/Specieslookup](https://github.com/BNHM/SpeciesLookup)
## File structure
debug.py tests the kmlparserclass.py functions locally

kmlparserclass.py contains all the functions needed to read in and process kml files

ray_casting.py implements the ray casting method

updater.py still needs more work but it contains function to update range maps on a regular basis

viz.py visualizes range maps and query points. 

webapi.py puts everything together into a web service 

### Note on KMZ
These are for testing purposes only; in production we will use the AmphibiaWeb live directory for ranges which is updated regularly.

## Updates
Apache server and Python 3 need to installed on the server
