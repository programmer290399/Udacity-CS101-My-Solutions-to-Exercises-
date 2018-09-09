# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(n):
    greatest = 0
    for i in range(0,len(n)):
        if n[i] > greatest:
            greatest = n[i]
    return greatest







print greatest([4,23,1])
#>>> 23
print greatest([1,3,2])
#>>> 0
