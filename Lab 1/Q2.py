# 2. WAP to swap two numbers

def swap (a,b):
  a,b=b,a
  print("After swap:")
  print("First number=",a)
  print("Second number=",b)
a=input("\n Enter the first number:")
b=input("\n Enter the second number:")
print("Before swap:")
print("First number=",a)
print("Second number=",b)
swap(a,b)