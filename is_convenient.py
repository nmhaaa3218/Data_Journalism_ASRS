# Given an coordinates of a fuel station, classify it into one of the following categories:
# Convenient position OSM tags: highway=motorway, highway=trunk, highway=primary
#    If fuel station distnace to the nearest above tag is less than 100m, then it is convenient.
#    Otherwise, it is not convenient.
import osmnx as ox

def is_convenient(point):
    # Define interested tags
    tags = {'highway': ['motorway', 'trunk', 'primary']}

    try:
        # Use features_from_point to get features within 500 meters
        features = ox.features_from_point(point, tags, dist=500)
        
        if features.empty:
            return False
        else:
            return True
    except Exception as e:
        return False
    
# test for empire state building
print(is_convenient((40.7484, -73.9857)))
