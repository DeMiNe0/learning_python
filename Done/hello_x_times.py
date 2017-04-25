import sys

count = int(0)  # Create count. start at 0
st_lists = []  # Create empty st_lists list.

for stline in sys.stdin:
    st_lists.append(stline.rstrip('\n'))  # Append each line in stline to our st_lists list and remove the \n newline from each line
    count += 1
    if count == 1:
        break  # break out of loop when count hits 1

st_lists = int(str(st_lists[0]))   # convert st_lists into an integer for use in the while loop below.

#print("testing: ", st_lists)

a = 0 # create a
while a < st_lists:
    print("Hello")
    a += 1