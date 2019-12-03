import tkinter

window = tkinter.Tk()
window.title("Map")
road_map = "city-data.txt"
map1 = read_cities(road_map)
best_cycle = find_best_cycle(map1)
# creating the 'Canvas' area of width and height 500px
canvas = tkinter.Canvas(window, bg = 'white', width = 3700, height = 1900)
canvas.pack()
box1 = canvas.create_rectangle(50,50,1600,800)
long_list = []
lat_list = []

#for i in range(0, 1800, 5):
#    line1 = canvas.create_line(50 + i, 50, 50+i, 900)
#for i in range(0, 850, 5):
#    line2 = canvas.create_line(50, 50 + i, 1850, 50 + i)


window.mainloop()