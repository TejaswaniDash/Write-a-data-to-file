"""
HOW TO WRITE A DATA TO A FILE

* we have been working with Python modules and Python coding,
* we print something, it writes to the console,
* What if we actually want to read and write information on our computer,
* We can write to some other file. This process is known as File I/O.

File I/O
* ' w ' -->  Write-Only Mode
* ' r ' --> Read-Only Mode
* ' r+ ' --> Read And Write Mode
* ' a ' --> Append Mode
"""

#create list where there is some data so that we can write in file

my_list = [1,2,3,]

my_file = open("firstfile.txt" , 'w')
#we will write to a file. So I'm creating a file object

for item in my_list:
    my_file.write(str(item)) #write() is a function
    # we have to close the file object
    # write() function always takes a string argument

my_file.close()
# After we write to the file, we want to make sure that we close the file.
# And we simply do that by calling the close() function.
# If you don't do that Python won't write properly to the file,
# because during the I/O process,
# because all the data we write to the file, this is going to be the data,
# And that is going to buffer if we don't close.
# It actually is hold in the temporary location in the memory, before writing to the file,
# so it's not written directly to the file,
# Python first holds it into a temporary location, which is the memory of the computer,
# and it's just buffered there.
# And it does not flush the buffer until Python knows that all the data is correctly written,
# and until it is sure that it's completely done in a proper way

# if we don't close the file we will have fishy output/results.

"""
to write the context in genegrated file in a next line format (to add a new line we use 
*  my_file.write(str(item) + "\n") 
* it gonna write the first item in frist line and then it's gonna write the newline
* which means it's just going to hit carriage return and it's come to a newline
* when it comes to a newline, second time it goes into the loop and write to the secondline and so on.
"""

# Example 2 on the basis of newline

my_list = [1,2,3,]

my_file = open("NewLinefile.txt" , 'w')

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

# Example 3

my_list = ["bmw", "benz", "honda"]

my_file = open("carfile.txt" , 'w')

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()




