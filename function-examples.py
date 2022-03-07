#wtite a function "print_seconds" so that is prints the total amount of seconds give the hours, minutes,
#and seconds, as parameters.

# hint:  there are 3600 seconds in an hour and 60 seconds in a minute.

from curses import KEY_MARK


def print_seconds(hours, minutes, seconds):
    print((hours*3600) + (minutes*60) + seconds)

print_seconds(1, 2, 3) #3723

def convert_seconds(seconds):
    hours = seconds // 3600 #floor division(//). How many hours is in the give amount of seconds.
    minutes = (seconds - hours * 3600) // 60 #how many minutes are there left when we subtract the hour
    remaining_seconds = seconds - hours * 3600 - minutes * 60 # how many seconds remaine after subtrating minutes
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds) #1 23 20



