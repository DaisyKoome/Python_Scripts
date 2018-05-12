c=input("Please enter any alphabet")
c=input("Please enter any alphabet: ")
if((c=='a')|(c=='e')|(c=='i')|(c=='o')|(c=='u')):
	print("The alphabet is vowel: ",c)
else:
	print("The alphabet is consonant: ",c)

num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
num3=int(input("Enter the num3: "))
if(num1>num2)&(num1>num3):
    print("Num1 is the greatest")
elif(num2>num1)&(num2>num3):
    print("Num2 is the greatest")
else:
    print("Num3 is the greatest")
    
