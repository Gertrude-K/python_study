def stars(n):
    for i in range(1, n + 1):
        result = '*' * i
        print(result)



n= int(input("Enter the number of stars: "))
stars(n)

def triangular_stars(n):
    for i in range(1, n + 1):
        result = n + 1 - i
        result = '*' * result #print('*' * (n + 1 - i))
        print(result)

n = int(input("Enter the number of stars: "))
triangular_stars(n)

def pyramids_stars(n):
    for i in range(1, n + 1):
        space = " " * (n - i) 
        star = '*' * (2 * i - 1)
        print(space + star)

n = int(input("Enter the number of stars: "))
pyramids_stars(n)
