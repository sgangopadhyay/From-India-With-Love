# You have been given a list create a new list which 
# comprises of NO Duplicates in it.


list_1 = [10,11,12,13,10,13,15,17,19,17,19]
result = []
list_length = len(list_1)
print(list_1)

for i in range(list_length):
    res=i+1
    for j in range(res,list_length):
        if(list_1[i]==list_1[j] and list_1[i] not in result):
            result.append(list_1[i])

print(result)


# ANOTHER APPROACH

first_list=[]
duplicate_list=[]

for i in list_1:
    if i not in first_list:
        first_list.append(i)
    else:
        duplicate_list.append(i)

print(first_list)
print(duplicate_list)


# print(result)

# You have been given a list create a new list which 
# comprises of Duplicates in it.
