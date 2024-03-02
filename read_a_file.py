"""
HOW TO READ FILE

* a lot of times we need to read some data for any calculations and any manipulation.
* it's really important to know how we can read a file using Python

Reading a file --> .read()
Reading line by line --> .readline()
"""

#read a file use of .read() function

my_file = open("carfile.txt",'r')

my_file.read()
my_file.close()

#this will simply read the file but we can't see anything in result because it is reading not writing
# if want to check it is reading completely
#we can print it when it is reading to check if it is reading completely

my_file = open("carfile.txt" , 'r')

print(str(my_file.read()))
my_file.close()

"""
what if we want to read the file line by line rather than pulling the entire file at once
"""
# Example 3

print ("Line by line ===============>>")

my_file_line = open("carfile.txt" , 'r')

print(str(my_file_line.readline()))

my_file_line.close()
# it will read the only first line of the file
# it's only reading one line of the file, and all the subsequent calls of it
# if I call it twice -> it's gonna read the second line

# Example 4

print ("Line by line ===============>>")

my_file_line = open("carfile.txt" , 'r')

print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
my_file_line.close()

# We can put it in a for loop, we can read line by line,
# we can do calculations on the lines depending on the contents of the line,
# Once we put it in the for loop, we can check for the contents,
# we can do different kinds of calculations or manipulations based on the contents
# So reading a file, line by line is really helpful when we want to do manipulations based on the line, not the complete file.

# Example 5 using for loop?

print ("Line by line ===============>>")

my_file_line = open("carfile.txt" , 'r')

print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
my_file_line.close()
