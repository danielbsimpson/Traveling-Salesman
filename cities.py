import random
import math
import copy
import tkinter as tk

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
    end_distance = compute_total_distance(road_map)
    end_map = road_map
    length_file = len(road_map)
    count = 0
    
    while count <= 10000:
        count += 1
        random_index1 = int(length_file * random.random()) 
        random_index2 = int(length_file * random.random())
        best_cycle = swap_cities((shift_cities(end_map)), random_index1, random_index2)
        best_map = best_cycle[0]
        distance_best_cycle = best_cycle[1]
        
        if distance_best_cycle < end_distance:
            end_distance = distance_best_cycle
            end_map = best_map
            
    return(end_map, end_distance)    
    
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """


def print_map(best_cycle):
    best_route_list = []
    for i in range(0, len(best_cycle[0]) - 1):
        distance_between = str(round(compute_total_distance([best_cycle[0][i], best_cycle[0][i+1]]),2))
        route = str(best_cycle[0][i][1]) +' to ' + str(best_cycle[0][i+1][1]) + ', travel distance of: ' + distance_between + '\n'
        best_route_list.append(route)
    str1 = ''.join(best_route_list) + '\n' + 'Total Travel Distance = ' + str(best_cycle[1])
    return(str1)
        

    
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def visualize_road_map(best_cycle):
    
    long_list = []
    lat_list = []
    for j in range(0, len(best_cycle)):
        long_list.append(float(best_cycle[j][3]))
        lat_list.append(float(best_cycle[j][2]))
    
    long_list.sort()
    lat_list.sort()
    
    long_min = math.floor(long_list[0])
    long_max = math.ceil(long_list[49])
    lat_min = math.floor(lat_list[0])
    lat_max = math.ceil(lat_list[49])
    
    #set min and max long/lat to max values in list or -180/180 and -90/90
    x1_coordinate = max(long_min, -180)
    x2_coordinate = min(long_max, 180)    
    y1_coordinate = min(lat_min, 90)
    y2_coordinate = max(lat_max, -90)
    
    distance_x = (x2_coordinate - x1_coordinate)
    distance_y = (y2_coordinate - y1_coordinate)
    
    window = tk.Tk()
    window.title("Road Map")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    canvas = tk.Canvas(window, bg = 'white', width = screen_width - 100, height = screen_height - 100)
    canvas.pack()
    grid_size_w_start = 30
    grid_size_h_start = 30
    grid_size_w = screen_width - 400
    grid_size_h = screen_height - 200
    
    total_grid_w = grid_size_w - grid_size_w_start
    total_grid_h = grid_size_h - grid_size_h_start
    
    x_line_distance = int(total_grid_w / distance_x)
    y_line_distance = int(total_grid_h / distance_y)
    
    x_line_total = int(total_grid_w / x_line_distance)
    y_line_total = int(total_grid_h / y_line_distance)
    
    x_axis_values = math.ceil(distance_x / x_line_total)
    y_axis_values = math.ceil(distance_y / y_line_total)
    
    #draw vertical lines:    
    y_2 = grid_size_h_start + ((y_line_total) * y_line_distance)
    for i in range(grid_size_h_start, ((x_line_total)* x_line_distance) + 40, x_line_distance):
        canvas.create_line(i,grid_size_h_start,i,y_2)
    
    #draw horizontal lines:        
    x_2 = grid_size_w_start + ((x_line_total) * x_line_distance)
    for i in range(grid_size_w_start, ((y_line_total)* y_line_distance) + 35, y_line_distance):
        canvas.create_line(grid_size_w_start,i,x_2,i)
        
    #label x-axis:
    count_x = x1_coordinate
    for i in range(0, (x_line_total + 1) * x_line_distance, x_line_distance):
        x = grid_size_w_start + i
        y = 20
        canvas.create_text(x, y, text = count_x, fill = 'blue', font = ("Times", 6, 'bold'))
        count_x += x_axis_values
    #label y-axis:
    count_y = y2_coordinate
    for i in range(0,(y_line_total + 1)*y_line_distance, y_line_distance):
        x = 10
        y = grid_size_h_start + i
        canvas.create_text(x,y, text = count_y, fill = 'blue', font = ("Times", 6, 'bold'))
        count_y -= y_axis_values
     
    
    #take list of best cycle and place on grid map
    count_city = 1
    for i in best_cycle:
        x = math.floor(float(i[3]))
        y = math.floor(float(i[2]))
        
        x_position = grid_size_w_start - int(((x1_coordinate - x) * (x_line_distance / x_axis_values)))
        y_position = grid_size_h_start + int(((y2_coordinate - y) * (y_line_distance / y_axis_values)))
        
        canvas.create_text(x_position, y_position, text = str(count_city), fill = 'red', font = ("Times", 10, "bold"))
        count_city += 1
    
    #label numbers with city, state
    y_text = 30
    for i in range(0, (len(best_cycle))):
        city = str(best_cycle[i][1])
        state = str(best_cycle[i][0])
        full_text = str(i+1) + '.' + city + ',' + state
        canvas.create_text(grid_size_w + 100, y_text, text = full_text, font = ("Times", 8, 'bold') )
        y_text += 10
        
        
    
    window.mainloop()

    return ()    



def main():
    road_map = read_cities('city-data.txt')
    print()
    print('Original Data:' + '\n')
    print(road_map)
    best_cycle = find_best_cycle(road_map)
    printed_map = print_map(best_cycle)
    print()
    print('Best cycle road map with distance between cities:' + '\n')
    print(printed_map)
    visualize_road_map(best_cycle[0])
    

    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
