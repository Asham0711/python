#Integers, String, Tuples, Boolean, Floating point numbers, Frozen sets, Bytes

username = 'Asham' #string data type
print(username) #prints Asham
username = 'Amaan' #trying to change immutable objects data
print(username) #String data type which is immutable but got changed here

x = 10 #integer data type
y = x #assign whatever in x in y
print(x) #prints 10
print(y) #prints 10
x = 'Asham' #changing x from 10 to Asham
print(x) #prints Asham
print(y) #still prints 10

#Case 1:
# 1. A memory allocated for 'Asham' and username is pointing to that
# 2. Then we added 'Amaan' so new memory allocated to 'Amaan'(no rewrite in the same memory) and now username pointing to 'Amaan'
# 3. Thenas nothing is pointing towards 'Asham' so garbage collector will delete 'Asham' from the memory

# Case 2:
# 1. A memory allocated for 10 and both x and y points at 10
# 2. A memory allocated for 15 and x starts pointing to Asham.
# 3. 10 did not get deleted because x is still pointing at it.

# So immutable means you cannot rewrite in the same memory as before instead you need to allocate a new memory location 
# for the new value and then point at it.