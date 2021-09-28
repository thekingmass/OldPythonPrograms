
s = input("enter any string ")

print("length = ", len(s))
for i in range(0, len(s)):
    if i % 2 == 0:
        print(s[i],  end="")

    else:
        print(s[i].capitalize(), end="")