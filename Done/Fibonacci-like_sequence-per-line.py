# Problem Description
# A Fibonacci-like sequence is a sequence of integers a1, a2, ... for which an = an-1+an-2 for all n > 2. You are given the first two elements of the sequnce a1 and a2, and the 1-based index n. Output the n-th element of the sequence.
#
# The input data consists of a single line which contains integers a1, a2 and n separated by single spaces. 0 < a1, a2, n < 10.
#
# Example
#
# input
#
# 1
# 2
# 3
#
# output
#
# 3


import sys

MAXVALUE = int(100)
st_lists = []  # Create empty st_lists list.

# Get at the most; 3 lines from stdin.
count = int(0)
for stline in sys.stdin:
    st_lists.append(stline.rstrip('\n'))  # Append each line in stline to our st_lists list and remove the \n newline from each line
    count += 1
    if count == 3:
        break  # break out of loop when count hits 3

# print("Full List:", st_lists)
# print("List[0]:", st_lists[0])
# print("List[1]:", st_lists[1])
# print("List[2]:", st_lists[2])

# Assign each list item to a variable. Convert them to int's while we're at it.
fib_a = int(st_lists[0])
fib_b = int(st_lists[1])
fib_p = int(st_lists[2])
fib_ploop = fib_p
fib_p -= 1

def fib(n):  # Create the function that creates our fibonacci sequence using the first two lines from stdin. Maximum value as the function param.
    re = []  # Create a list from our result.
    a = fib_a  # First Value from stdin
    b = fib_b  # Second Value from stdin
    lstop = 0
    while lstop < fib_ploop:
        re.append(a)  # Append a onto our result
        tmpvar = b  # Save b1 to a temp var
        b = a + b  # Determine b's new value
        a = tmpvar  # Determine a's new value(b's old value)
        lstop += 1
    return re  # Return our new result

fibby = fib(MAXVALUE)  # Run our fib function with MAXVALUE as a param. Save results to a list called fibby.

#print("Full Fibby List:", fibby)
print(fibby[fib_p])

