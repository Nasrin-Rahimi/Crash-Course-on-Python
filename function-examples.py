#wtite a function "print_seconds" so that is prints the total amount of seconds give the hours, minutes,
#and seconds, as parameters.

# hint:  there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    print((hours*3600) + (minutes*60) + seconds)

print_seconds(1, 2, 3) #3723
