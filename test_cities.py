
import pytest
from cities import *

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                 ("Alaska",	"Juneau", 58.301935, -134.41974),\
                 ("Arizona", "Phoenix",	33.448457, -112.073844)]
    
    country_capital1 = [('Somaliland', 'Hargeisa', 9.55, 44.05),\
                       ('South Georgia and South Sandwich Islands', \
                        'King Edward Point', -54.283333, -36.5), \
                        ('French Southern and Antarctic Lands', \
                         'Port-aux-FranÃ§ais', -49.35, 70.216667),\
                        ('Palestine', 'Jerusalem', 31.76666667, 35.233333),\
                        ('Aland Islands', 'Mariehamn', 60.116667, 19.9)] 
    
    country_capital2 = [('Belgium', 'Brussels', 50.83333333, 4.333333),\
                        ('Belize', 'Belmopan', 17.25, -88.766667),\
                        ('Benin', 'Porto-Novo', 6.483333333, 2.616667),\
                        ('Bermuda', 'Hamilton', 32.28333333, -64.783333)]
    
    country_capital3 = [('Niger', 'Niamey', 13.51666667, 2.116667),\
                        ('Nigeria', 'Abuja', 9.083333333, 7.533333),\
                        ('Rwanda', 'Kigali', -1.95, 30.05),\
                        ('Saint Helena', 'Jamestown', -15.933333, -5.716667),\
                        ('Sao Tome and Principe', 'Sao Tome', 0.3333, 6.7333),\
                        ('Senegal', 'Dakar', 14.73333333, -17.633333)]

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
    
    country_capital = [('Somaliland', 'Hargeisa', 9.55, 44.05),\
                       ('South Georgia and South Sandwich Islands', \
                        'King Edward Point', -54.283333, -36.5), \
                        ('French Southern and Antarctic Lands', \
                         'Port-aux-FranÃ§ais', -49.35, 70.216667),\
                        ('Palestine', 'Jerusalem', 31.76666667, 35.233333),\
                        ('Aland Islands', 'Mariehamn', 60.116667, 19.9)]
    
    assert swap_cities(state_city1, 0, 1) == \
         ([("Delaware", "Dover", 39.161921, -75.526755),\
         ("Kentucky", "Frankfort", 38.197274, -84.86311),\
         ("Minnesota", "Saint Paul", 44.95, -93.094)],\
        38.528719926809416)
    
    assert swap_cities(state_city1, 1, 2) == \
         ([("Kentucky", "Frankfort", 38.197274, -84.86311),\
         ("Minnesota", "Saint Paul", 44.95, -93.094),\
         ("Delaware", "Dover", 39.161921, -75.526755)],\
         38.528719926809416)
    
    assert swap_cities(state_city2, 0, 1) == \
        ([("Alaska",	"Juneau", 58.301935, -134.41974),\
        ("Alabama", "Montgomery", 32.361538, -86.279118),\
         ("Arizona", "Phoenix",	33.448457, -112.073844)],\
         113.92444731706527)
   
    assert swap_cities(state_city2, 0, 2) == \
        ([('Arizona', 'Phoenix', 33.448457, -112.073844),\
          ('Alaska', 'Juneau', 58.301935, -134.41974),\
          ('Alabama', 'Montgomery', 32.361538, -86.279118)],
            113.92444731706529)    
        
    assert swap_cities(country_capital, 0, 1) == \
        ([('South Georgia and South Sandwich Islands', \
           'King Edward Point', -54.283333, -36.5),
            ('Somaliland', 'Hargeisa', 9.55, 44.05),\
            ('French Southern and Antarctic Lands', \
             'Port-aux-FranÃ§ais', -49.35, 70.216667),\
             ('Palestine', 'Jerusalem', 31.76666667, 35.233333),\
             ('Aland Islands', 'Mariehamn', 60.116667, 19.9)])
        
    assert swap_cities(country_capital, 0, 4) == \
        [('Aland Islands', 'Mariehamn', 60.116667, 19.9),\
                       ('South Georgia and South Sandwich Islands', \
                        'King Edward Point', -54.283333, -36.5), \
                        ('French Southern and Antarctic Lands', \
                         'Port-aux-FranÃ§ais', -49.35, 70.216667),\
                        ('Palestine', 'Jerusalem', 31.76666667, 35.233333),\
                        ('Somaliland', 'Hargeisa', 9.55, 44.05)]
        
    '''add your tests'''

def test_shift_cities():
    
    state_city1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    state_city2 = [("Alabama", "Montgomery", 32.361538, -86.279118),\
                 ("Alaska",	"Juneau", 58.301935, -134.41974),\
                 ("Arizona", "Phoenix",	33.448457, -112.073844)]

    country_capital1 = [('Somaliland', 'Hargeisa', 9.55, 44.05),\
                       ('South Georgia and South Sandwich Islands', \
                        'King Edward Point', -54.283333, -36.5), \
                        ('French Southern and Antarctic Lands', \
                         'Port-aux-FranÃ§ais', -49.35, 70.216667),\
                        ('Palestine', 'Jerusalem', 31.76666667, 35.233333),\
                        ('Aland Islands', 'Mariehamn', 60.116667, 19.9)]
    
    country_capital2 = [('Belgium', 'Brussels', 50.83333333, 4.333333),\
                        ('Belize', 'Belmopan', 17.25, -88.766667),\
                        ('Benin', 'Porto-Novo', 6.483333333, 2.616667),\
                        ('Bermuda', 'Hamilton', 32.28333333, -64.783333)]
    
    country_capital3 = [('Niger', 'Niamey', 13.51666667, 2.116667),\
                        ('Nigeria', 'Abuja', 9.083333333, 7.533333),\
                        ('Rwanda', 'Kigali', -1.95, 30.05),\
                        ('Saint Helena', 'Jamestown', -15.933333, -5.716667),\
                        ('Sao Tome and Principe', 'Sao Tome', 0.3333, 6.7333),\
                        ('Senegal', 'Dakar', 14.73333333, -17.633333)]
    
    assert shift_cities(state_city1) == \
        ([("Minnesota", "Saint Paul", 44.95, -93.094),\
         ("Kentucky", "Frankfort", 38.197274, -84.86311),\
         ("Delaware", "Dover", 39.161921, -75.526755)],\
          38.528719926809416)
        
    assert shift_cities(state_city2) == \
        ([("Arizona", "Phoenix",	33.448457, -112.073844),\
         ("Alabama", "Montgomery", 32.361538, -86.279118),\
         ("Alaska",	"Juneau", 58.301935, -134.41974)],\
        113.92444731706527)
    
    assert shift_cities(country_capital1) == \
        ([('Aland Islands', 'Mariehamn', 60.116667, 19.9),
          ('Somaliland', 'Hargeisa', 9.55, 44.05),\
          ('South Georgia and South Sandwich Islands', \
                        'King Edward Point', -54.283333, -36.5), \
          ('French Southern and Antarctic Lands', \
                         'Port-aux-FranÃ§ais', -49.35, 70.216667),\
           ('Palestine', 'Jerusalem', 31.76666667, 35.233333)])
          
    assert shift_cities(country_capital2) == \
        ([('Bermuda', 'Hamilton', 32.28333333, -64.783333),\
          ('Belgium', 'Brussels', 50.83333333, 4.333333),\
          ('Belize', 'Belmopan', 17.25, -88.766667),\
          ('Benin', 'Porto-Novo', 6.483333333, 2.616667)])
    
    assert shift_cities(country_capital3) == \
        ([('Senegal', 'Dakar', 14.73333333, -17.633333),
          ('Niger', 'Niamey', 13.51666667, 2.116667),\
          ('Nigeria', 'Abuja', 9.083333333, 7.533333),\
          ('Rwanda', 'Kigali', -1.95, 30.05),\
          ('Saint Helena', 'Jamestown', -15.933333, -5.716667),\
          ('Sao Tome and Principe', 'Sao Tome', 0.3333, 6.7333)])

         
    '''add your tests'''


