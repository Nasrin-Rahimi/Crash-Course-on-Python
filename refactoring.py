def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)   # 78.5

# The names of the variables above don't give the readers much information and although there are not
# clues that result might used for.

# In programming language, when we rewrite code to be more self documenting, we call this process 
# refactoring. The refactoring of the above code is:

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)

# Now with refactoring, the namse of the variables and function, reflect the purpose, which helps the 
# reader understand the code more quickly.

# sometimes we can add a comment to our code
