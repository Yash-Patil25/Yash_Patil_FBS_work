#Write a Python program to find elements in a given set that are not in another set.

set1 = {1,2,3,4,5,6}
set2 = {3,4,7}

diff = set1 - set2

print("Elements in set1 but not in set2",diff)