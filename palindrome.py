
number = 56
bowl = number
result = 0
print("original number : ", number)
while (number > 0):
    r = number % 10
    print("initial value of R : ", r)
    result = 10*result+r
    number=number // 10 
    print("initial value of NUMBER : ", number)
print("")
print("palindrome number # ", result)
if(bowl==result):
    print("palindrome number")
else:
    print("not a palindrome number")
