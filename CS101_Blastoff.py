# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    i = 0
    while True :
        if i < n :
            d = n - i
            print d
            i=i+1
        else :
            print "Blastoff!"
            break





countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!
