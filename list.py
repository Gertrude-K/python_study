
# # Check if item exists before removing
# if 5 in numbers:
#     numbers.remove(5)

# # Find position safely
# try:
#     pos = numbers.index(99)
# except ValueError:
#     print("Not found")

# # Sort in descending order
# numbers.sort(reverse=True)

# # Get and remove last item
# last = numbers.pop()           # No index = removes last item

fruits=["mango","oranges","banana","lemon","grapes"]
print(fruits)
#indexing and slicing
#slicing used to extract a part of a list

print(fruits[-2])
print(fruits[1:4])

#updating
fruits[1]="Tomatoes"
#append
fruits.append("Apples")
#insert
fruits.insert(3,"kiwi")
#remove
fruits.remove("lemon")
#pop
fruits.pop(1)
#clear
# fruits.clear()
print(fruits)
days_of_the_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days_of_the_week[0])
print(days_of_the_week[2:6])

days_of_the_week[3]="thur"
days_of_the_week.append("january")
days_of_the_week.insert(3,"December")
print(days_of_the_week)
days_of_the_week.remove("Friday")
days_of_the_week.pop(0)
days_of_the_week.pop()
print(days_of_the_week)

