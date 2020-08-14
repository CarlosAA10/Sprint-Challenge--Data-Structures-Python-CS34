import time
from collections import deque

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
counter = 0

q = deque()

q.append(names_1[counter])

while len(q) > 0:
    # we will pop the name from the left
    popped_name = q.popleft()
    # we will see if the name is in names_2 
    # if it is, then we will append it to duplicates, 
    # we will increase the counter 
    # else, we will increase the counter and append the next element in 
    # names_1 to our q and repeat the process again
    if popped_name in names_2:

        duplicates.append(popped_name)
        counter += 1
        q.append(names_1[counter])

    if counter == len(names_1) -1:# last case to worry about since index is out of range
        pass

    else:
        counter += 1
        q.append(names_1[counter])


    

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
