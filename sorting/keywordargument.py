# def ka(name,email,password):
#     print(name,email,password)
# ka("amit","amit@gmail.com","amit123")


# def ka(name,email,password):
#     print(name,email,password)
# ka(email="amit@gmail.com",password="amit123",name="amit")


# keywords arguments.
# def ka(**data):
#     for key,value in data.items():
#         print(key,value)
# ka(email="amit@gmail.com",password="amit123",name="amit")


# args and 
def ka(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
    
ka("amit",1,2,3,4,5,6,email="amit@gmail.com",password="amit123")




















