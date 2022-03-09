None: 
1- A special data type in python used to indicate that things are empty or that they returned nothing.

2- self documenting code: Writing in a way that's readable and doesn't conceal it's intent.

3- You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to 
use a variable without first initializing it, you'll run into a NameError. This is the Python 
interpreter catching the mistake and telling you that you’re using an undefined variable. The 
fix is pretty simple: initialize the variable by assigning the variable a value before you use it.

Another common mistake to watch out for that can be a little trickier to spot is forgetting to 
initialize variables with the correct value. If you use a variable earlier in your code and then 
reuse it later in a loop without first setting the value to something you want, your code may wind 
up doing something you didn't expect. Don't forget to initialize your variables before using them!

4- While Loops
A while loop executes the body of the loop while the condition remains True.

Syntax:
    while condition:
        body

Things to watch out for!
- Failure to initialize variables. Make sure all the variables used in the loop’s condition  are 
    initialized before the loop.

- Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the 
    condition, so that the loop will eventually end for all possible values of the variables.

 Typical use:
While loops are mostly used when there’s an unknown number of operations to be performed, and a 
condition needs to be checked at each iteration.

5- For Loops
A for loop iterates over a sequence of elements, executing the body of the loop for each element in 
the sequence.

Syntax:
    for variable in sequence:
        body

The range() function:
range() generates a sequence of integer numbers. It can take one, two, or three parameters:

range(n): 0, 1, 2, ... n-1

range(x,y): x, x+1, x+2, ... y-1

range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)

Common pitfalls:
- Forgetting that the upper limit of a range() isn’t included.

- Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by 
    letter, but that might not be what you want.

Typical use:
For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.

Break & Continue
You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a 
cycle due to a separate condition.
You can use the continue keyword to skip the current iteration and continue with the next one. This is 
typically used to jump ahead when some of the elements of the sequence aren’t relevant.

6- In Python, strings are immutable. This means that they can't be modified. So if we wanted to fix a 
typo in a string, we can't simply modify the wrong character. We would have to create a new string 
with the typo corrected. We can also assign a new value to the variable holding our string.

7- String operations
    - len(string) Returns the length of the string
    - for character in string Iterates over each character in the string
    - if substring in string Checks whether the substring is part of the string
    - string[i] Accesses the character at index i of the string, starting at zero
    - string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, 
    it's 0 by default. If j is omitted, it's len(string) by default.

String methods
    - string.lower() / string.upper() Returns a copy of the string with all lower / upper case 
    characters
    - string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without 
    left / right / left or right whitespace
    - string.count(substring) Returns the number of times substring is present in the string
    - string.isnumeric() Returns True if there are only numeric characters in the string. If not, 
    returns False.
    - string.isalpha() Returns True if there are only alphabetic characters in the string. If not, 
    returns False.
    - string.split() / string.split(delimiter) Returns a list of substrings that were separated by 
    whitespace / delimiter
    - string.replace(old, new) Returns a new string where all occurrences of old have been replaced 
    by new.
    - delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 
    - Python string method rindex() returns the last index where the substring str is found, or 
    raises an exception if no such index exists.


8- The format method returns a copy of the string where the {} placeholders have been replaced with 
the values of the variables. These variables are converted to strings if they weren't strings 
already. Empty placeholders are replaced by the variables passed to format in the same order.

example = "format() method"
formatted_string = "this is an example of using the {} on a string".format(example)
print(formatted_string)
"""Outputs:
this is an example of using the format() method on a string

If the placeholders indicate a number, they’re replaced by the variable corresponding to that order 
(starting at zero).

first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)
"""Outputs:
apple carrot banana

If the placeholders indicate a field name, they’re replaced by the variable corresponding to that 
field name. This means that parameters to format need to be passed indicating the field name.

If the placeholders include a colon, what comes after the colon is a formatting expression. See below 
for the expression reference.

# {:d} integer value
'{:d}'.format(10.5) → '10'

Formatting expressions
Expr            Meaning                                      Example
{:d}            integer value                               '{:d}'.format(10.5) → '10'
{:2f}           floating point with that many decimals      '{:.2f}'.format(0.5) → '0.50'
{:2s}           string with that many characters            '{:.2s}'.format('Python') → 'Py'
{:<6s}          string aligned to the left that many spaces '{:<6s}'.format('Py') → 'Py    '
{:>6s}          string aligned to the right that many spaces '{:>6s}'.format('Py') → '    Py'
{:^6s}          string centered in that many spaces          '{:^6s}'.format('Py') → '  Py  '

9- Lists in Python are defined using square brackets, with the elements stored in the list separated 
by commas: list = ["This", "is", "a", "list"]. You can use the len() function to return the number of 
elements in a list: len(list) would return 4. You can also use the in keyword to check if a list 
contains a certain element. If the element is present, it will return a True boolean. If the element 
is not found in the list, it will return False. For example, "This" in list would return True in our 
example. Similar to strings, lists can also use indexing to access specific elements in a list based 
on their position. You can access the first element in a list by doing list[0], which would allow you 
to access the string "This".

In Python, lists and strings are quite similar. They’re both examples of sequences of data. Sequences 
have similar properties, like (1) being able to iterate over them using for loops; (2) support 
indexing; (3) using the len function to find the length of the sequence; (4) using the plus 
operator + in order to concatenate; and (5) using the in keyword to check if the sequence 
contains a value. Understanding these concepts allows you to apply them to other sequence types as well.




