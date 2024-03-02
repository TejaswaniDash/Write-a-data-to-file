"""
FILE HANDLING USING "WITH" And "AS" KEYWORDS

* how we can close the files automatically?
* Is there a way in Python to automatically close our files, if we don't close them?

# file object has a special pair of built-in methods.
# One is enter and one is exit.
# So when a file object exit method is invoked,it means that it's going to close the file.
# And we have been invoking that using our .close() function,
# this .close() function that invokes the file object's exit method.

# here we will be doing that by using 'with' and 'as' keyword
"""

print ("Normal Write Start")
my_write = open("textfile.txt", 'w')
my_write.write("Trying to write to the file")

print ("Normal Read Start")
my_read = open("textfile.txt", 'r')
print(str(my_read.read()))
#here we are unable to see what read
#that's why close whatever we wrote

print("*"*50)

#Example 2
print ("Normal Write Start")
my_write = open("textfile.txt", 'w')
my_write.write("Trying to write to the file")
my_write.close()

print ("Normal Read Start")
my_read = open("textfile.txt", 'r')
print(str(my_read.read()))

print("*"*50)


#Now let's see how we can utilize  With As Keyword
#we are not going to use .close() function

#Example 3

print("With As Write Start")
with open("withas.txt" , 'w') as with_as_write:
    with_as_write.write("This is an example of with as write/read")

    #with_as_write is an object; we can name it anything

print()

print("With As Read Start")
with open("withas.txt" , 'r') as with_as_read:
    print(str(with_as_read.read()))


