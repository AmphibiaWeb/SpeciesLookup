# this script should create lookup tables for individual range maps
class grid_cell:

    def __init__(self, left_top_long, left_top_lat, right_bottom_long, right_bottom_lat):
        self.left_top_long = left_top_long
        self.left_top_lat = left_top_lat
        self.right_bottom_long = right_bottom_long
        self.right_bottom_lat = right_bottom_lat
        # static method here

    def chop(long_range, lat_range, interval):
    	cells=[]
        for i in range(360/interval[0]-1):
        	for j in range(180/interval[1]-1):
        		# add a grid cell 
        		cells.append(grid_cell())

        return cells


def create_table(long_interval=4, lat_interval=2):
    # what we are going to return
    long_range = (-180.0, 180.0)
    lat_range = (-90, 90)

    if 360 % long_interval or 180 % lat_interval:
        raise ValueError("inappropriate interval values!")
        # feel free to change it but make sure long and lat interval can divide
        # 360 and 180
    interval = (long_interval, lat_interval)

    cells = grid_cell.chop(long_range, lat_range, interval)
    lookup_table = {}

    # grid cells are divided into

    grid =

    #
    return lookup_table

# possibly dump this into a json file
