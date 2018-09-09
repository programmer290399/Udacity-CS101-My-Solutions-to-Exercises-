# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(sec):
    min = int(sec/60)
    hours_final = int(min/60)
    min_final = min % 60
    sec_final = sec - ( min_final*60)- ( hours_final * 3600)
    answer = ''
    if hours_final == 1 :
        answer = answer + '1 hour, '
    else :
        answer = answer + str(hours_final) +' hours, '
    if min_final == 1 :
        answer = answer + '1 minute, '
    else :
        answer = answer + str(min_final) +' minutes, '
    if sec_final == 1 :
        answer = answer + '1 second '
    else :
        answer = answer + str(sec_final) +' seconds '
    return answer







print convert_seconds(3600)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
