import time
from collections import deque

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [] 

# implementation with cache
# cache = {}

# for name in names_1:

#     if name not in cache:
#         cache[name] = name
    

# for name2 in names_2:
#     if name2 in cache:
#         duplicates.append(name2)

# print(duplicates,'duplicates array')

# Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            
            else:
                self.right.insert(value)

    def contains(self, target):
        # base case?
        # we find the target in a tree node
        if self.value == target:
            duplicates.append(target)
        # figure out which direction we need to go in
        if target < self.value:
            # we go left
            if not self.left:
                pass
            else: 
                return self.left.contains(target)
        # or, we get to a spot where the node should be, but nothing is there
        # how do we move towards the base case?
        else:
            # we go right
            if not self.right:
                pass
            else:
                return self.right.contains(target)

first_node = BSTNode(names_1[0])


for i in range(len(names_1)):

    if i == 0:
        # first_node = BSTNode(i)
        pass
    else:
        first_node.insert(names_1[i])


for i in range(len(names_2)):

    first_node.contains(names_2[i])










# counter = 0

# q = deque()

# q.append(names_1[counter])

# while len(q) > 0:
#     # we will pop the name from the left
#     popped_name = q.popleft()
#     # we will see if the name is in names_2 
#     # if it is, then we will append it to duplicates, 
#     # we will increase the counter 
#     # else, we will increase the counter and append the next element in 
#     # names_1 to our q and repeat the process again
#     if popped_name in names_2:

#         duplicates.append(popped_name)
#         counter += 1
#         q.append(names_1[counter])

#     if counter == len(names_1) -1:# last case to worry about since index is out of range
#         pass

#     else:
#         counter += 1
#         q.append(names_1[counter])


    

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
