# Fabonacci Series ?

number = 9
first_number = 0
second_number = 1
count = 0
if (number <= first_number):
    print("please use a postive number")
elif (number == second_number):
    print(1)
else:
    while (count < number):
        print(first_number)
        result = first_number+second_number
        print("Initial Value of RESULT : ", result)
        first_number = second_number
        print("Intial Value of FIRST_NUMBER : ",first_number)
        second_number = result
        print("Initial Value of SECOND_NUMBER : ", second_number)
        count = count + 1
