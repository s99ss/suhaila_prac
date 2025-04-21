num_1 = int(input("enter 1st number"))
num_2 = int(input("enter 2nd number"))
operation = input("select + or - or * or /:")
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

print (" result is : " , result )