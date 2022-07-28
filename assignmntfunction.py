#fuction
'''1. Define
2. How to call
3. Default parameter passing
4. Local variable
5. Global variable
6. Nested Function
7. Unsused paramters'''

#how to define function 
'''with def keyword 
syntax 
def <function name>():
    <function body>'''
    
#how to call function
 
'''def saf():
    print('i am safwan')
saf()

def introduce(name):
    print('hello am, ' + name+' from  shimoga')
introduce('safwan')

def prints(a,b,c,d):
    print(a,b,d,c)
prints(10,20,30,40)

#default parameter passing 

def safwan(h=10):
    print(h)
safwan()

def xyz(q,w,e,r,h=180):
    print(w,h)
xyz(1,2,3,4)

def student(firstname, lastname ='safwan', standard ='Engineering'):
    print(firstname, lastname, 'studies in', standard, 'Standard')
 
# 1 positional argument
student('muruli')
# 2 positional arguments 
student('niru', 'abhishek')                 
student('salman', 'althu')
# 3 positional arguments                        
student('sufi', 'veena', 'altu')

#Nusted function
def outer_func(who):
    print(who)
    def inner_func():
        print("Hello, who")
    inner_func()
outer_func("World!")


def inner_increment(number):
    return number + 1
print(inner_increment(10))

def increment(number):
    def inner_increment():
        return number + 1
    return inner_increment()
print(increment(10))

def outer_func(x=3):
    print(x)
    def inner_func():
        print("Hello, World!")
    inner_func()
outer_func(9)

#unused  local variable 
def my_func():
     
    # unused local variables
    a = 5  
    b=2
    c=b+10
    
for i in range(0, 5):
        print(i)
my_func()'''


class safwan:
    a = 0 #globale variable
    b = 0
    def __init__(self,a, b):
        self.a = a
        self.b = b
        
    def fun(self,a, b):  #local variable 
        print(a, b)
        
        
        
obj = safwan(10,20)

obj1 = safwan(60, 70)


print("values of obj", obj.a, obj.b)
print("values of obj1", obj1.a, obj1.b)

obj.fun(20, 30)