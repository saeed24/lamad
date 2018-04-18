# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:58:20 2018

@author: Raheel
"""
from math import sin, cos, sqrt, atan2, radians

R = 6373.0 # approximate radius of earth in km


def Distance(lat1,lon1,lat2,lon2): # Calculates distance between two points
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def PathDistance(routes): # Calculates Total distance of the path
    total_distance=0

    for i,obj in enumerate(routes[:-1]):
        lat1=obj['lat']
        lon1=obj['lng']
        lat2=routes[i+1]['lat']
        lon2=routes[i+1]['lng']
        total_distance=total_distance+Distance(lat1,lon1,lat2,lon2)
    return total_distance