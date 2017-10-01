"""
This code will find the path of a given goal knowing that every k node gives
2k and 2k+1 nodes.
"""
def get_path(goal):
    path = []   #list for the path to be taken
    goal = bin(goal)[2:]    #converting from int to binary, removing the 0b
    location = str(goal[1:])    #removing the first bit from the number, converted to string so we can take it char at a time
    for bit in location:
        if int(bit) == 0:
            path.append("left")
        else:
            path.append("right")
    print("This is the path: ", path)

get_path(int(input("Where is your goal? ")))
