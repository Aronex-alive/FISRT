'''#WAP a program for generating a OTP which should contain 6 numbers
from random import randint
for i in range(1,7):
    a=randint(0,9)
    print(a)
print("next otp is")
otp=1
while otp<=6:
    x=randint(0,9)
    print(x)
    otp+=1'''



from random import randint

# First OTP
otp = ""
for i in range(1,6):
    otp += str(randint(0, 9))
print("Your OTP is:", otp)

# Second OTP
otp = ""
for i in range(6):
    otp += str(randint(0, 9))
print("Your OTP is:", otp)



    
