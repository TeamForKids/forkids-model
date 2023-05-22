import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import pandas
from haversine import haversine

# data import
place_df = pd.read_csv('p_data.csv', index_col=0)
parking_df = pd.read_csv('parking_data.csv', index_col=0)

# function
def distance_calculation(place_name):

    distances = []
    x = place_df[place_df['name'] == place_name]['latitude'].values[0]
    y = place_df[place_df['name'] == place_name]['longitude'].values[0]

    for name, lat, long in zip(parking_df['name'], parking_df['latitude'], parking_df['longitude']):
        place = (x, y)
        parking = (lat, long)
        distance = haversine(place, parking, unit='km')
        distances.append(name)

    distances.sort()  # Sort distances in ascending order

    min_3 = distances[:3]  # Get the top three distances

    return min_3