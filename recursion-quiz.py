#The count_users function recursively counts the amount of users that belong to a group in the company 
# system, by going through each of the members of a group and if one of them is a group, recursively 
# calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)
  return count

#correct version:
def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

#Fill in the blanks to make the is_power_of function return whether the number is a power of the 
# given base. Note: base is assumed to be a positive number. Tip: for functions that return a 
# boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    #return ------
    return number * base == base

  # Recursive case: keep dividing number by base.
  #return is_power_of(------)
  return is_power_of(number // base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#This function prints out a multiplication table (where each number is the result of multiplying the 
# first number of its row by the number at the top of its column). Fill in the blanks so that calling 
# multiplication_table(1, 3) will print out:

#1 2 3 

#2 4 6 

#3 6 9

def multiplication_table(start, stop):
    #for x in -----:
	for x in range(start, stop + 1):
        #for y in ------
		for y in range(start, stop + 1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above


# The counter function counts down from start to stop when start is bigger than stop, and counts 
# up from start to stop otherwise. Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


#The even_numbers function returns a space-separated string of all positive numbers that are 
# divisible by 2, up to and including the maximum that's passed into the function. For example, 
# even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
	for x in range(2, maximum+1, 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed