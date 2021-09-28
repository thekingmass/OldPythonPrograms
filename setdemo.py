set1 = {0, 2, 4, 6, 8}
set2 = {1, 2, 3, 4, 5}

set3 = set()

for i in set2:
    if not(i in set1):
        set3.add(i)
print(set3)
