import os
import geopandas as gpd

def get_overall_bounding_rectangle(folder_path):
    overall_bounds = [float('inf'), float('inf'), float('-inf'), float('-inf')]

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".geojson"):
            file_path = os.path.join(folder_path, filename)
            # Load the GeoJSON file into a GeoDataFrame
            gdf = gpd.read_file(file_path)
            
            # Calculate the bounding box for all features in the GeoDataFrame
            bounds = gdf.total_bounds  # returns (minx, miny, maxx, maxy)
            
            # Update the overall bounding rectangle
            overall_bounds[0] = min(overall_bounds[0], bounds[0])  # minx
            overall_bounds[1] = min(overall_bounds[1], bounds[1])  # miny
            overall_bounds[2] = max(overall_bounds[2], bounds[2])  # maxx
            overall_bounds[3] = max(overall_bounds[3], bounds[3])  # maxy

    return {
        "minx": overall_bounds[0],
        "miny": overall_bounds[1],
        "maxx": overall_bounds[2],
        "maxy": overall_bounds[3]
    }

# Specify the path to the folder containing GeoJSON files
folder_path = "."

# Get the overall bounding rectangle
overall_bounding_rectangle = get_overall_bounding_rectangle(folder_path)

# Print the overall bounding rectangle
print("Overall Bounding Rectangle:", overall_bounding_rectangle)
