# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def download_time(size , unit_size , speed , unit_speed):
    final_size = 1
    final_speed = 1
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
    if unit_size == 'kb' :
        final_size = size * (2 ** 10)
    elif unit_size == 'kB' :
        final_size = size * (2 ** 10 * 8)
    elif unit_size == 'Mb' :
        final_size = size * (2 ** 20)
    elif unit_size == 'MB' :
        final_size = size * (2 ** 20 * 8)
    elif unit_size == 'Gb' :
        final_size = size * (2 ** 30)
    elif unit_size == 'GB' :
        final_size = size * (2 ** 30 * 8)
    elif unit_size == 'Tb' :
        final_size = size * (2 ** 40)
    elif unit_size == 'TB' :
        final_size = size * (2 ** 40* 8)

    if unit_speed == 'kb' :
        final_speed = speed * (2 ** 10)
    elif unit_speed == 'kB' :
        final_speed = speed * (2 ** 10 * 8)
    elif unit_speed == 'Mb' :
        final_speed = speed * (2 ** 20)
    elif unit_speed == 'MB' :
        final_speed = speed * (2 ** 20 * 8)
    elif unit_speed == 'Gb' :
        final_speed = speed * (2 ** 30)
    elif unit_speed == 'GB' :
        final_speed = speed * (2 ** 30 * 8)
    elif unit_speed == 'Tb' :
        final_speed = speed * (2 ** 40)
    elif unit_speed == 'TB' :
        final_speed = speed * (2 ** 40* 8)

    return convert_seconds((final_size+0.0)/final_speed)


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 37 minutes, 32.8 seconds  # 40.0 seconds is also acceptable
