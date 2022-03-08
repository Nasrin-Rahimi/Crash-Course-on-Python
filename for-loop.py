#write a function that print a list of dominoes's tile. (every dominoes' tile has to side left and
# right. and in each side there is a number from 0 to 6) 


def printDomino():
    for left in range(7):
        for right in range(left, 7): 
            print("[" + str(left) + "|" + str(right) + "]", end=" ")
        print()

# print function, print a new line character at the end of every print. If we don't want to go the next 
#line after print, we can use a parameter in print function. Here we use end parameter. It write just
# a space instead of new line character.

#Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and 
# avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

for x in range(0,101,7):
    print(x) #0, 7, 14, ..., 98

#Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 
# 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number 
# is defined as the product of an integer and all integers before it. For example, the factorial of 
# five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))

