
#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one 
# byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 
# bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function 
# below, which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    #full_blocks = -------
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    #partial_block_remainder = -------
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        # return -------
        return  (block_size * full_blocks) + block_size
    #return -------
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


#The fractional_part function divides the numerator by the denominator, and returns just the 
# fractional part (a number between 0 and 1). Complete the body of the function so that it 
# returns the right number.
#Note: Since division by 0 produces an error, if the denominator is 0, the function should 
# return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
    # keep just the fractional part of the quotient
	if denominator == 0:
		return 0
	
	fractional = (numerator / denominator) % 1
	if fractional == 0.0:
		return 0
	return fractional

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

#The longest_word function is used to compare 3 words. It should return the word with the most number 
# of characters (and the first in the list when they have the same length). Fill in the blank to 
# make this happen.

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))