
def star(func):
    def inner(*args,**kwargs):
        print("**********************")      
        func(*args,**kwargs)        
        print("**********************")
    return inner

def equal(func):
    def inner(*args,**kwargs):
        print("======================")
        func(*args,**kwargs)
        print("======================")
    return inner

def div(func):
    def inner(*args,**kwargs):
        print("======================")
        func(*args,**kwargs)
        print("======================")
    return inner

@star
@equal
def greet(msg):
    print(msg)
@div
def divide(a,b):
    print(a/b)
divide(4,2)
divide(2,5)

greet("Hello from India")