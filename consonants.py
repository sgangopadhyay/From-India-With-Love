def Count_Vowels(data):
    print(data)
    count_a=0
    count_e=0
    count_i=0
    count_o=0
    count_u=0
    for i in data:
        if(i=="a"):
            count_a=count_a+1
        elif(i=="e"):
            count_e=count_e+1
        elif(i=="i"):
            count_i=count_i+1
        elif(i=="o"):
            count_o=count_o+1
        elif(i=="u"):
            count_u=count_u+1
    total_consonants= len(data)-(count_a+count_e+count_i+count_o+count_o)
    print("Total Consonants : ", total_consonants)

Count_Vowels(name)
