# 35) Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30. 

square = []

for sq in range(1,31):
    square.append(sq)

print(f"First  5 Element of the values is: {square[:5]}")    
print(f"Last 5 Element of the values is: {square[-5:]}")    
