#Set don't have index
numbers = {1,2,3,4,6,8}
print(numbers)

#Check the Length of set
print(len(numbers))

#We can't change value on set, but we can add at the end
numbers.add(10)
print(numbers)

#Add multiple items by using list
numbers.update([12,14,16])
print(numbers)

add = [18,20,22]
numbers.update(add)
print(numbers)

#Remove value.If value does not exist, it will error
numbers.remove(10)
print(numbers)

#Delete value.If value does not exist, it will not error
numbers.discard(13)
print(numbers)

numbers.discard(8)
print(numbers)

#Delete using Pop.It will delete the first item
numbers.pop()
print(numbers)


#Copying the whole set can be assigned to new set
otherNumbers = numbers.copy()
print(otherNumbers)

#Union set. Returns a set containing all the values of two set
oddNumbers = {1,3,5,7,9}
unionSet = numbers.union(oddNumbers)
print(unionSet)

#Difference set.Returns a set containing the values that only exist on the left set
result = numbers.difference(oddNumbers)
print(result)

#Intersection set. Returns a set containing the values that exist both on two sets
intersection = numbers.intersection(oddNumbers)
print(intersection)

#Symmetric Difference Set. Returns a set containing all values that exists exclusively on each set
symmetric = numbers.symmetric_difference(oddNumbers)
print(symmetric)

#Disjoint set. Returns a boolean whether two sets have an intersection  or not
print(numbers.isdisjoint(oddNumbers))

#Subset.Returns a boolean whether the left set is contained in the right set
print(numbers.issubset(oddNumbers))

#Casting Sets
print(tuple(numbers))
numbers = list(numbers)

numbers [0] = 1
print(numbers)

#Clear the value in set that will create an empty set
numbers.clear()
print(numbers)



