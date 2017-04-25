# Reverse Sentences
# reversestringstackeasyQUESTION SCORE100
# TEST CASES10 Problem Description
# You are given an integer N, followed by N lines of input (1 <= N <= 100). Each line of input contains one or several words separated with single spaces. Each word is a sequence of letters of English alphabet containing between 1 and 10 characters, inclusive. The total number of words in the input is between 1 and 100, inclusive.
#
# Your task is to reverse the order of words in each line of input, while preserving the words themselves. The lines of your output should not have any trailing or leading spaces.
#
# Example
#
# input
# 3
# Hello World
# Bye World
# Useless World
#
# output
# World Hello
# World Bye
# World Useless

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

# Get n lines from stdin.
st_lists = []
count = int(0)
for stline in sys.stdin:
    st_lists.append(stline.rstrip('\n'))
    count += 1
    if count == n:
        break

# Break st_lists lines into their own lists. Use space as a delimiter. Reverse them.
for i in st_lists:
    myi = i.split(' ')[::-1]  # split each list line into their own lists and reverse them.
    myi = str(' '.join(myi)) # Join lists back into a string.
    print(myi)