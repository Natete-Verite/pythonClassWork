def hello(name,age):
    year= 2022-age
#     #print("Welcome to AkiraChix")
    return f"Hello {name}, you were born in {year}"

def my_country(country="Uganda", student="Susan"):
    return f"Hello {student} you are from {country}"
    
# def greet_multiple(*names):
#     for name in names:
#         print(f"Hello {name}")

def sum(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum    
           
def multiply(*numbers):
    quotient=1
    for number in numbers:
        quotient*=number
    return quotient

def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "country" in keys:
        print (f"Hello {kwargs['name']} you are from {kwargs['country']}")
    elif "age" in keys:
        year =2022-kwargs["age"]  
        print (f"Hello {kwargs['name']} you were born in {year}")
    elif not kwargs:
        print(f"Hello Anonymous")   

def sum_and_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num
    keys=kwargs.keys()
    if"name" in keys:
        print(f"Hello {kwargs['name']}, the answer is {sum}")   
    elif"country" in keys:
        print(f"Hello {kwargs['country']}, the answer is {sum}")
    elif not kwargs:
        print(f"Hello Anonymous, the answer is {sum}")                      