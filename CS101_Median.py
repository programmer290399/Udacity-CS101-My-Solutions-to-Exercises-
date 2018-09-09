# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    x = biggest(a,b,c)
    if x == a :
        y = bigger(b,c)
        return y
    if x == b :
        y= bigger(a,c)
        return y
    if x == c :
        y = bigger(a,b)
        return y








print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
