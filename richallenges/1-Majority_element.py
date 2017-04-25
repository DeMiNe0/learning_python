# Majority element of an array is defined as a value x for which strictly more than half of array elements are equal to x. Output the majority element of the given array a, or -1 if the array doesn't have majority element.
#
# The first line of the input contains an integer N - the number of elements in the array. 1 <= N <= 100.
# The second line of the input contains N integers - the elements of the array, separated with single spaces. 1 <= ai <= 100.
#
# Example
#
# input
#
# 5
# 8 8 2 4 8
#
# output
#
# 8
#
# input
#
# 3
# 1 2 3
#
# output
#
# -1

import sys

n_count = []  # Create empty st_lists list.

# Determine amount of input lines for stline
# n = int(0)
count = int(0)
for ncount in sys.stdin:
    n_count.append(ncount.rstrip('\n'))
    count += 1
    if count == 2:
        break
n = int(n_count[0])

# if n == int(0):
#     print("You must specify an input size")
#     exit(1)

# print("Length:", n)

# Assign our N (amount of values to accept)
n = int(n_count[0])

# Assign numbers from the second item in the list to a var and splits them into their own list.
elem = n_count[1]
elem = elem.split()

# Return error if element isn't the expected size.
if len(elem) != n:
    print("Your element must be", n, "characters long.")
    exit(1)


def majority(k):  # k will be the list we'll feed this function
    ele = {}  # Create a blank dictionary
    max = ('', 0)  # Create a tuple
    for n in k:  # Iterate through the second stdin line input
        #print(n)
        if n in ele: ele[n] += 1  # if n is in the dict ele, update ele dict at index n +1.
        else: ele[n] = 1  # Otherwise we'll just set it to 1.
        if ele[n] > max[1]: max = (n,ele[n])  # If n is greater than max is set to tuple of n,ele[n]
    return max # Return max number

# Run our function
majelem = majority(elem)

# The value thats the major element, first part the tuple.
maj_elem = majelem[0]
# The amount of times it appears, second part of the tuple.
maj_elem_times = majelem[1]

# print("Majority: ", maj_elem)
# print("Repeated: ", maj_elem_times)

# Print -1 if there are no major elems'.
if maj_elem_times > 2:
    print(maj_elem)
else:
    print("-1")