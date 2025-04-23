import math

num_1 = int(input("enter 1st number"))
num_2 = int(input("enter 2nd number"))
operation = input("select + or - or * or / or ** or ! or absolute or (OR) | or & or ^:")
result = 0
'''
print(num_1)
print(num_2)
'''

if operation== "+" :
    result = num_1 + num_2
elif operation== "-" :
    result = num_1 - num_2
elif operation== "*" :
    result = num_1 * num_2
elif operation== "/" :
    result = num_1 / num_2
elif operation== "**" :
    result = num_1 ** num_2
elif operation== "!" :
    result=1

    for i in range(1, num_1+1):
        result=result*i


elif operation== "absolute":
    result= abs(num_1)

elif operation == "|":
     result = num_1 | num_2

elif operation == "&":
     result = num_1 & num_2
elif operation == "^":
    result = math.pow(num_1, num_2)

print (" result is : " , result )