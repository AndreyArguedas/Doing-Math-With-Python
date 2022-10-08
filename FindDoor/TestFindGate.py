"""
Imagine that you are facing a high wall that stretches infinitely in both directions. There is a door in the wall, but you don’t know how far away is the door or in which direction. It is pitch dark, but you have a very dim lighted candle that will enable you to see the door when you are right next to it.
Show an algorithm that enables you to find the door by walking at most O(n) steps in
the worst case, where n is the number of steps that you would have taken if you knew
where the door is and walked directly to it (note that your algorithm does not know
the value of n in advance)
"""
        



def find_door(wall, initial_pos):
    i = 0
    direction = 1 # 1: right, -1:left
    directionsChecked = 0
    steps = 2 ** i
    last_pos = initial_pos
    
    if wall[initial_pos] == 1: #Found the door
        return initial_pos
    
    
    while True: #Door not found yet
        
        #Go to direction forward
        for idxR in range(1, steps):
            last_pos = initial_pos + (direction * idxR)
            if wall[last_pos] == 1:
                return last_pos # Door found
        
        #Go to direction backwards, to return to initial position
        for idxBack in range(1, steps):
            if wall[last_pos + (-direction * idxBack)] == 1:
                return last_pos + (-direction * idxBack)
        
        directionsChecked += 1
        direction *= -1
        
        #If right and left have been checked we increment the steps and start again
        if directionsChecked == 2:
            i += 1
            steps = 2 ** i
            directionsChecked = 0
            
        


# result = find_door([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],7)
# print("Door found on position:",result)

wall = [0] * 2000
wall[1700] = 1
result = find_door(wall,1000)
print("Door found on position:",result)

