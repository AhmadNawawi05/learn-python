# nested loop = dalam nested loop "inner loop" akan menyelesaikan semua perulangannya sebelum
#               menyelesaikan satu iterasi dari "outer loop"

import math

#       persegi       

# rows = int(input("Please enter the rows!: "))
# colums = int(input("Please enter the colums!: "))
# symbol = input("please enter the symbol you want!: ")

# for i in range(rows):
#     for j in range(colums):
#         print(symbol, end="")
#     print()

#       segitiga 

# rows = int(input("Please enter the rows!: "))
# symbol = input("please enter the symbol you want!: ")

# for i in range(rows):
#     for j in range(rows - i - 1) :
#         print(" ", end="")
        
#     for k in range(2 * i + 1):
#         print(symbol , end="")
#     print()


#       lingkaran

radius  = int(input("Please enter the rows!: "))
symbol = input("please enter the symbol you want!: ")

center_x = radius
center_y = radius

for i in range (2 * radius + 1):
    for j in range(2 * radius + 1):
        distance = math.sqrt((i - center_y) **2 + (j - center_x) **2)
        
        if math.isclose(distance, radius, rel_tol=0.5) or (i == 0 and j >= radius and j <= 2 * radius) or (i == 2 * radius and j >= radius and j <= 2 * radius):
            print(symbol, end="")
        else: 
            if j == 0 or j == 2 * radius:
                print(symbol, end="")
            else:
                print(" ", end="")
            
    print()


