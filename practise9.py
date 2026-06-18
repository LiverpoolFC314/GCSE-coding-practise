# Create a two-dimensional array scores as shown in 
# the previous slide and 
# retrieve a few values using indexing.

scores = [[9, 5], [4, 5], [6, 8]]

print(scores[2][1])

print(scores[1] [1])

print(scores[0] [0])

scores[0][0]= 10

scores[2][1]=12

#Find largest and the smallest score from the 2D list.
largest=scores[0][0]
smallest=scores[0][0]

for row in scores:
    for items in row:
        if items>largest:
            largest=items
        elif items<smallest:
            smallest=items
print("The largest score is",largest)
print("The smallest score is",smallest)