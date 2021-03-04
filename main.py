# 
# 
# your comment header here
# 
# 

import numpy as np

# SIZE is a global constant, use this throughout your program.
# you should be able to change this to any int and your
# whole program will still work correctly. TEST THIS!
SIZE = 10

# creates a numpy array of size SIZE filled with 0s.
numbers = np.array([0] * SIZE, dtype=int)

# show the array
print("All the numbers...")
print(numbers)
print()

# now fill it with 10,20,30, etc ***using a loop***

for numbers in range(SIZE):
    numbers = (numbers+1)*10
    print(numbers)
print()
exit()

# show the array again but USE A LOOP TO DO IT
print("All the numbers...")

##############################################
# erase this comment and code your loop here
##############################################

print()

# now make an integer array of size 4 to hold stats, call it 'stats'
# calculate four basic statistics and put them in the 'stats' array in this order:
# min, max, total, average
#
# min and max will just be the first and last numbers from the numbers array because the
# arrays we created are in order. We will learn to search for min and max later.
#
# average may calculate as a float, make it an int to store it in the stats array
# or just use integer divsion to guarantee an int when you calculate

###########################################################
# erase this comment and code filling your stats array here
###########################################################


# When you have your stats array working, uncomment this code to display the stats.
#
#print("Min: ", stats[0])
#print("Max: ", stats[1])
#print("Total: ", stats[2])
#print("Average: ", stats[3])    
print()
