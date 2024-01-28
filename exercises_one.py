operator=input("Enter(+,-,*,/):")
num_1=int(input("Enter number one "))
num_2=int(input("Enter number two"))
if operator=="+":
    print(num_1+num_2)
elif operator==("-"):
    print(num_1-num_2)
elif operator=="*":
    print(num_1*num_2)
elif operator=="/":
    print(num_1/num_2)
if num_2 != 0:
    print(num_1/num_2)
else:
    print("Division zero")


