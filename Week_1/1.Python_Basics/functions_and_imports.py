import data_import as db
import sys
# import antigravity

def add(a,b):
    print('{}, hey there {}'.format(a,b))
    return a+b

add(1,3)


def student_info(*args,**kwargs):
    print(args) #args are all the arguments passed in a function as a tuple , while kwargs are key value pairs as map
    print(kwargs)

info = ('mary', 'watson', 'emma', 'tom')
data = {'name': 'hello', 'age': 23, 'height': '7.9'}
student_info('mary','watson','emma','tom',name='hello',age=23,height='7.9')
print('\n')

student_info(*info,**data)

print(db.courses)
print(sys.path) # list of places where python look for import modules in order

