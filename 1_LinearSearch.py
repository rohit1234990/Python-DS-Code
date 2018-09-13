# Author : Rohit Kumar
# Date   : 14-Sept-2018

# Python program to implement Linear Search
nums = [int(i) for i in  raw_input("Enter numbers sperated by space : ").split(" ")]
to_find = int(raw_input("Enter the number to find : "))

if to_find in nums:
    print "Congratulations number found"
else:
    print "Sorry we are unable to find the specified number"





