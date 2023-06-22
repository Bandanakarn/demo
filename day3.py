# languages=["Python, C++, Swift"]
# print(languages[1])

# my_tuple=(99,8,2,1,3,4,5)
# my_tuple2=(99,1,2,3,4,5)
# print(my_tuple+my_tuple2)
# print(my_tuple[0])
# print(len[my_tuple])

# new_tuple=sorted(my_tuple)
# print(new_tuple)

# new_tuple=sorted(my_tuple,reverse=True)
# print(new_tuple)

# print(2 in my_tuple)

# print(max(my_tuple))
# print(min(my_tuple))

# #Define a tuple named my_tuple with the following elements: 10, 20, 'a', 'b', True
# my_tuple=(10,20,'a','b',True)

# #Write the code to access and print the third element of the tuple my_tuple
# print(my_tuple[2])

# # Concatenate two tuples: tuple1 with elements (1, 2, 3) and tuple2 with elements ('x', 'y', 'z'). Store the result in a new tuple called concatenated_tuple.
# tuple1=(1,2,3)
# tuple2=('x','y','z')
# concatenated_tuple=tuple1+tuple2
# print(concatenated_tuple)

# # Write a Python code snippet to repeat the tuple my_tuple three times and store the result in a new tuple named repeated_tuple.
# repeated_tuple=my_tuple*3
# print(repeated_tuple)

# # Determine the length of the tuple concatenated_tuple using a built-in function and print the result.
# print(len(concatenated_tuple))

# # Perform slicing on the tuple my_tuple to extract a new tuple with elements 'a', 'b', and True. Store the result in a variable called sliced_tuple
# sliced_tuple=my_tuple[2:]
# print(sliced_tuple)

#dictonary
# my_dist={
#     "Name":"ABC",
#     "age":16,
#     "Address":{
#         "Address1":"KTM",
#         "Zip":
#              "Zip1":44800
#              "Zip2":44600
#     }
# }

# my_dist["College"]="KMC"
# print(my_dist.keys())
# print(my_dist.get("age"))
# print(my_dist.get("Address"))
# print(my_dist["Address"]["Zip"])
# print(my_dist["Address"]["Zip"]["Zip1"])

#del my_dist["age"]
# new_age=my_dist.pop("age")
# print(new_age)
# print(my_dist)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# count=0
# n=1
# prime_list=[]
# while count<20:
#     if is_prime(n):
#         prime_list.append(n)
#         count=count+1
#     n+=1


# is_prime(20)
# for i in range(19):
#     a=prime_list[i]
#     for j in range(1,11):
#         print(f"{a}*{j}=",a*j)


#WAP to find the simple interest
# p=int(input("enter the principal"))
# t=int(input("enter the time"))
# r=int(input("enter the rate"))
# simple_interest=(p*t*r)/100
# print("Simple interest is:",simple_interest)

#WAP to find the perimeter of rectangular ground
# l=int(input("enter the length: "))
# b=int(input("enter the breadth: "))
# perimeter=2*(l+b)
# print("the perimeter of rectangular ground is:",perimeter)

#WAP to calculate volume of a cube.
# l=int(input("enter the length"))
# volume_cube=l**3
# print("the volume of a cube is: ",volume_cube)

#WAP to find the square root of a number
n=int(input("enter the number"))
print("square root of number is: ")
