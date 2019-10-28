import pytest
from cities import *

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                 ("Alaska",	"Juneau", 58.301935, -134.41974),\
                 ("Arizona", "Phoenix",	33.448457, -112.073844)]    

    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)
    
    assert compute_total_distance(road_map2) ==\
            pytest.approx(54.6848+33.4221+25.8176,0.01)


def test_swap_cities():
    
    state_city1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    state_city2 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                 ("Alaska",	"Juneau", 58.301935, -134.41974),\
                 ("Arizona", "Phoenix",	33.448457, -112.073844)] 
    
    assert swap_cities(state_city1, 0, 1) == \
        [("Delaware", "Dover", 39.161921, -75.526755),\
         ("Kentucky", "Frankfort", 38.197274, -84.86311),\
         ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert swap_cities(state_city1, 1, 2) == \
        [("Kentucky", "Frankfort", 38.197274, -84.86311),\
         ("Minnesota", "Saint Paul", 44.95, -93.094),\
         ("Delaware", "Dover", 39.161921, -75.526755)]
    
    assert swap_cities(state_city2, 0, 1) == \
        [("Alaska",	"Juneau", 58.301935, -134.41974),\
        ("Alabama", "Montgomery", 32.361538, -86.279118),\
         ("Arizona", "Phoenix",	33.448457, -112.073844)]
   
    assert swap_cities(state_city2, 0, 2) == \
        [("Arizona", "Phoenix",	33.448457, -112.073844),\
        ("Alabama", "Montgomery", 32.361538, -86.279118),\
         ("Alaska",	"Juneau", 58.301935, -134.41974)]    
        
    '''add your tests'''

def test_shift_cities():
    
    state_city1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    state_city2 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                 ("Alaska",	"Juneau", 58.301935, -134.41974),\
                 ("Arizona", "Phoenix",	33.448457, -112.073844)]
    
    assert shift_cities(state_city1) == \
        [("Minnesota", "Saint Paul", 44.95, -93.094),\
         ("Kentucky", "Frankfort", 38.197274, -84.86311),\
         ("Delaware", "Dover", 39.161921, -75.526755)]
        
    assert shift_cities(state_city2) == \
        [("Arizona", "Phoenix",	33.448457, -112.073844),\
         ("Alabama", "Montgomery", 32.361538, -86.279118),\
         ("Alaska",	"Juneau", 58.301935, -134.41974)]

         
    '''add your tests'''


