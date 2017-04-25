# A word chain is a sequence of words in which every word except the first one starts with the last letter of the previous word. You are given a sequence of words. Output the length of the longest prefix of the sequence which forms a valid word chain. One-word chain is always valid.
#
# The first line of the input contains an integer N - the number of words in the sequence. 1 <= N <= 10.
# The following N lines contain the words of the sequence, one word per line. Each word is between 1 and 10 characters long and consists of lowercase letters of English alphabet.
#
# Example
#
# input
#
# 4
# the
# eagle
# eats
# snakes
#
# output
#
# 4
#
# input
#
# 7
# snakes
# seldom
# munch
# on
# north
# highland
# ducks
#
# output
#
# 3
#
# In the first example, the whole sequence is a valid word chain.
# In the second example, the longest prefix which is a word chain is "snakeS SeldoM Munch". The last four words of the sequence are a longer word chain but they are not a prefix of the sequence.

import sys

n_count = []  # Create empty st_lists list.

# Determine amount of input lines for stline
count = int(0)
for ncount in sys.stdin:
    n_count.append(ncount.rstrip('\n'))
    count += 1
    if count == 1:
        break
n = int(n_count[0])

# Get n lines from stdin. Assign to list called st_lists
st_lists = []
count = int(0)
for stline in sys.stdin:
    st_lists.append(stline.rstrip('\n'))
    count += 1
    if count == n:
        break

# print(n)

#  Iterate through st_lists
dupes = int(0)
for i in st_lists:
    # Turn i into a list of characters for that word.
    ei = list(i)
    # print(ei)

    firstlet = str(ei[0])  # Select first item in list(first letter)
    lastlet = str(ei[-1])  # Select last item in list(second letter)

    firstletnext = firstlet  # Save the old firstletter to a new var so you can compare it against the next lastletter.
    lastletnext = lastlet   # Save the old lastletter to a new var so you can compare it against the next firstletter.

    # Compare our letters for duplicates and count them.
    if lastlet == firstletnext:
        dupes += 1
    if firstletnext == lastlet:
        dupes += 1
    #print("first ", firstlet)
    #print("last ", lastlet)

print(dupes)  # Print the amount of duplicates.