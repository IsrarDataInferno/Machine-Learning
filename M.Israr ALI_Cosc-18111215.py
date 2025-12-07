# # Q1. Write a Python program to find all the values in a list are greater than a specified number.

# # sample_list = [1,2,3,4,5,6,7]

# # n =3      #specified number

# # test_list =  []
# # for i in sample_list:
# #     if i >n:
# #         test_list.append(i)
# # print(test_list)


# # Q2. Write a Python program to find a9 tuple, the smallest second index value from a list of tuples.

# sample_list1 = [(1,2),(3,4),(4,1)]


# print(min(sample_list1,key=lambda n: (n[1],-n[0])  ))


# #second way

# # sample_list1.sort()
# # print(sample_list1[2])


# Q3. Write a Python program to convert a list of multiple integers into a single integer.

# list1=[1,3,6]
# integer = int("".join(map(str, list1)))
# print(integer)


#Q4. Write a Python program to unzip a list of tuples into individual lists.

# list3  =[('Ali',4),('Ahmed',7),('Bilal',9)]
# print(list((zip(*list3))))
# for stuff in list3:
#     print(list(stuff))


#Q5. Write a Python program to find the repeated items of a tuple
# tuple1 = (1,1,3,7,3,1,4)
# count = tuple1.count(1)
# print(count)



# # Q6. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.
# i = int(input("Enteer an integer : "))
# o = str(oct(i))[2:]
# h = str(hex(i))[2:]
# h = h.upper()
# b = str(bin(i))[2:]
# d = str(i)
# print(f" decimal : {d},'   ',Octal : {o},'   ',Hexadecimal : {h},'      ',Binary : {b}")







# Q7. Write a Python program to count number of substrings with same first and last characters of a given string.

# def no_substrings(str1):
#     result = 0
#     n = len(str1)
#     for i in range(n):
#         for j in range(i,n):
#             if (str1[i]==str1[j]):
#                 result +=1
#     return  result
# str1 = input("Enter a  string : ")
# print(no_substrings(str1))







# Q8. Write a Python program to move all spaces to the front of a given string in single traversal.


# def move_Spaces_front(str1):


#      noSpaces_char = [ch for ch in str1 if ch!=' ']
# 	spaces_char = len(str1) -   len( noSpaces_char )
# 	result = ' '*spaces_char
# 	result = '"'+result + ''.join(noSpaces_char)+'"'
# 	return(result)
	
# print(move_Spaces_front("I_Am_String   "))
# print(move_Spaces_front("   I_Am_String  "))









