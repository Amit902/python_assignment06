# Q1 Take 10 integers from user and print it on screen
l=[]
for x in range(10):
	l.append(int(input("Enter a value: ")))
print(l)


# Q2 Write an infinite loop.An infinite loop never ends. Condition is always true.
 

for x in range (10,1,-1):
	print("hello world",x)
	

i=1
while i<=10:
	print("hello world")

#Q3 Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

l = []
for x in range(10):
	l.append(int(input("Enter a number: ")))
print(l)
 
l1 = []
for x in range(10):
	l1.append(l[x]**2) 
print(l1)

#Q4 From a list containing ints, strings and floats, make three lists to store them separately 

l = [1,4,3,5,6,7,8,1.5,12.2,25.36,45.02,"Amit","Lalit","Malay","Nihal","Satyam","Nikhil"]
l1 = []
l2 = []
l3 = []
for x in l:   
	if type(x) == int:
		l1.append(x)
	elif type(x) == float:
		l2.append(x)
	elif type(x) == str:
		l3.append(x)
print(l1)
print(l2)
print(l3)	


#Q5 Using range(1,101), make a list containing even and odd numbers. 
l1 = []
l2 = []
for x in range (1,101):
	if x % 2 == 0:
		l1.append(x)
	else:
		l2.append(x)
print(l1)
print(l2)		

#Q.6- Print the following patterns: 
   # *
   # **
   # ***
   # ****

def pypart(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print("* ",end = "")
		print("\n")
n=10
pypart(n)

#Q7 Create a user defined dictionary and get keys corresponding to the value using for loop.

d ={}
for i in range(5):
	key=input("enter any key: ")
	value=input("enter the value: ")
	d[key]=value
print("\n")
print(d)

# Q8 Take inputs from user to make a list  Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

l = []
for x in range(5):
	l.append(input("Enter any values: "))
print(l) 
flag = 0
s=input("enter the value you want to search and delete: ")
for x in l:
	if x == s:
		l.remove(x)
		flag=1
print(l)
if flag == 0:
	print("number not found")
	
	