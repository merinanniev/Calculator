 def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def divide(x, y):  
   return x / y  
def modulus(x,y):
   return x % y
print("Choose an operation")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide") 
print("5.Modulus") 
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter 1st number :"))  
num2 = int(input("Enter 2nd number :"))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2)) 

elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2)) 

elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  

elif choice == '5':  
   print(num1,"%",num2,"=", modulus(num1,num2)) 

else:  
   print("Oops!!!!!This is an invalid input. Please enter the valid input.")  