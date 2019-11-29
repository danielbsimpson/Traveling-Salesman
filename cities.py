import random
import math
import copy

def read_cities(city_data):
    infile = open(city_data, 'r')
    line = infile.readlines()
    length_file = len(line)
    line1 = []
    for i in range(0, length_file):
        list1 = tuple(line[i].rstrip().split('\t'))
        line1.append(list1)
    road_map = line1
    return(road_map)

    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
  
def print_cities(road_map):
    LocationList=[]
    length_file = len(road_map)
    for j in range(0,length_file):
        CityName = road_map[j][1]
        FloatLat = round(float(road_map[j][2]),2)
        FloatLong = round(float(road_map[j][3]),2)
        NewList = [CityName, FloatLat, FloatLong]
        LocationList.append(NewList)
    return(LocationList)

    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """

def compute_total_distance(road_map):
    DistanceList = []
    length_file = len(road_map)
    for j in range(0, length_file):
        LocLat1 = float(road_map[j][2])
        LocLat2 = float(road_map[(j + 1) % len(road_map)][2])
        LocLong1 = float(road_map[j][3])
        LocLong2 = float(road_map[(j + 1) % len(road_map)][3])
        Distance = math.sqrt(((LocLat2 - LocLat1)**2) + ((LocLong2 - LocLong1)**2))
        DistanceList.append(Distance)
    return(sum(DistanceList))
    
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """


def swap_cities(road_map, index1, index2):

    NewLocationList = copy.deepcopy(road_map)
    NewLocationList[index1] = road_map[index2]
    NewLocationList[index2] = road_map[index1]
    NewDistance = compute_total_distance(NewLocationList)
    
    ReturnedList = (NewLocationList, NewDistance)
    return(tuple(ReturnedList))
    
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def shift_cities(road_map):
    shifted_road_map = [road_map[-1]] + road_map[:-1]
    return(shifted_road_map)
   
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """


def find_best_cycle(road_map):
    initial_distance = compute_total_distance(road_map)
    initial_map = road_map
    length_file = len(road_map)
    count = 0
    
    while count <= 10000:
        count += 1
        random_index1 = int(length_file * random.random()) 
        random_index2 = int(length_file * random.random())
        best_cycle = swap_cities((shift_cities(initial_map)), random_index1, random_index2)
        best_map = best_cycle[0]
        distance_best_cycle = best_cycle[1]
        
        if distance_best_cycle < initial_distance:
            initial_distance = distance_best_cycle
            initial_map = best_map
            
    return(initial_map, initial_distance)    
    
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """


def print_map(road_map):

    
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():

    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
