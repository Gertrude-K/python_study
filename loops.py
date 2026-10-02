lst = list(range(1,101))
zip = []

for i in lst:
    if i%5==0 and i%7==0:
        zip.append(i)
print(zip)
