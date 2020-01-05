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

def visualize(best_cycle):
    
    long_list = []
    lat_list = []
    #pull the longitude and latitude from best_cycle
    for j in range(0, len(best_cycle)):
        long_list.append(float(best_cycle[j][3]))
        lat_list.append(float(best_cycle[j][2]))
    #sort the data
    long_list.sort()
    lat_list.sort()
    #get the smallest and largest longitude/latitude and round up/down
    long_min = math.floor(long_list[0])
    long_max = math.ceil(long_list[len(long_list) - 1])
    lat_min = math.floor(lat_list[0])
    lat_max = math.ceil(lat_list[len(lat_list) - 1])
    
    #set min and max long/lat to max values in list or -180/180 and -90/90
    x1_coordinate = max(long_min, -180)
    x2_coordinate = min(long_max, 180)    
    y1_coordinate = min(lat_min, 90)
    y2_coordinate = max(lat_max, -90)
    #total height/width in latitude/longitude
    distance_x = (x2_coordinate - x1_coordinate)
    distance_y = (y2_coordinate - y1_coordinate)
    #create a window the size of the monitor
    window = tk.Tk()
    window.title("Road Map")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    #create a blank canvas the size of the window
    canvas = tk.Canvas(window, bg = 'white', width = screen_width, height = screen_height)
    canvas.pack()
    #identify how large the grid will be on the blank canvas
    #space left on right side for labels created later on
    grid_size_w_start = 30
    grid_size_h_start = 30
    grid_size_w = screen_width - 400
    grid_size_h = screen_height - 200
    
    total_grid_w = grid_size_w - grid_size_w_start
    total_grid_h = grid_size_h - grid_size_h_start
    
    #pixel and latitude/longitude conversions with rounding
    x_line_distance = int(total_grid_w / distance_x)
    y_line_distance = int(total_grid_h / distance_y)
    
    x_line_total = int(total_grid_w / x_line_distance)
    y_line_total = int(total_grid_h / y_line_distance)
    
    x_axis_values = math.ceil(distance_x / x_line_total)
    y_axis_values = math.ceil(distance_y / y_line_total)
    #scale values for when there are 80 or less cities vs 80 or more cities to plot
    if len(best_cycle) < 80:
        font_city_size = 8
        space_size = 10
        axis_label_size = 6
        label_count_value = 1
        grid_city_labels = 10
        xlines_scale = 40
        ylines_scale = 35
        limiting_value = 0
        wording_center1 = 200
    else:
        font_city_size = 5
        space_size = 8
        axis_label_size = 5
        label_count_value = 5
        grid_city_labels = 8
        xlines_scale = 0
        ylines_scale = 0
        limiting_value = 35
        wording_center1 = 100
        wording_center2 = 300
        
    #draw vertical lines:    
    y_2 = grid_size_h_start + ((y_line_total) * y_line_distance) - limiting_value
    for i in range(grid_size_h_start, ((x_line_total)* x_line_distance) + ylines_scale, x_line_distance):
        canvas.create_line(i,grid_size_h_start,i,y_2)
    
    #draw horizontal lines:        
    x_2 = grid_size_w_start + ((x_line_total) * x_line_distance) - limiting_value
    for i in range(grid_size_w_start, ((y_line_total)* y_line_distance) + xlines_scale, y_line_distance):
        canvas.create_line(grid_size_w_start,i,x_2,i)
        
    #label x-axis:
    count_x = x1_coordinate
    for i in range(0, (x_line_total + 1) * x_line_distance - limiting_value, x_line_distance*label_count_value):
        x = grid_size_w_start + i
        y = 20
        canvas.create_text(x, y, text = count_x, fill = 'blue', font = ("Times", axis_label_size, 'bold'))
        count_x += x_axis_values*label_count_value
    #label y-axis:
    count_y = y2_coordinate
    for i in range(0,(y_line_total + 1)*y_line_distance - limiting_value, y_line_distance):
        x = 10
        y = grid_size_h_start + i
        canvas.create_text(x,y, text = count_y, fill = 'blue', font = ("Times", axis_label_size, 'bold'))
        count_y -= y_axis_values
     
    
    #take list of best cycle and place on grid map
    count_city = 1
    for i in best_cycle:
        x = math.floor(float(i[3]))
        y = math.floor(float(i[2]))
        
        x_position = grid_size_w_start - int(((x1_coordinate - x) * (x_line_distance / x_axis_values)))
        y_position = grid_size_h_start + int(((y2_coordinate - y) * (y_line_distance / y_axis_values)))
        
        canvas.create_text(x_position, y_position, text = str(count_city), fill = 'red', font = ("Times", grid_city_labels, "bold"))
        count_city += 1
    
    y_text = 30
    y_count = 30

    #label numbers with city, state
    for i in range(0, (len(best_cycle))):
        city = str(best_cycle[i][1])
        state = str(best_cycle[i][0])
        full_text = str(i+1) + '.' + city + ',' + state
        #if less than 125 cities, we stick with one column, over 125 we start a new column
        if i < 125:
            canvas.create_text(grid_size_w + wording_center1, y_text, text = full_text, font = ("Times", font_city_size, 'bold') )
        else:
            canvas.create_text(grid_size_w + wording_center2, y_count, text = full_text, font = ("Times", font_city_size, 'bold') )
            y_count += space_size            
        y_text += space_size
        
        
    
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
    visualize(best_cycle[0])
    

    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
