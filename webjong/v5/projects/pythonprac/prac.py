a = 3
b = a
a = a + 1

num1 = a*b
num2 = 99

name = 'bob'
num = 12
is_number = True

a_list = []
a_list.append(1)
a_list.append([2,3])

a_dict = {}
a_dict = {'name':'bob', 'age':21}
a_dict['height'] = 178

people = [
    {'name': 'bob', 'age':20},
    {'name': 'carry', 'age':30}
    ]
person = {'name': 'john', 'age': 7}
people.append(person)

'''
수학에서
f(x) = 2*x+3
y = f(2)
y의 값은 7
'''

'''
자바스크립트에서
function f(x) {
    return 2*x+3
}
'''

# 파이썬에서
def f(x):
    return 2*x+3

y = f(2)
# print(y)


def sum_all(a,b,c):
    return a+b+c

def mul(a,b):
    return a*b

result = sum_all(1,2,3) + mul(10,10)
# print(result)


def  oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = oddeven(20)
# print(result)


def is_adult(age):
    if age > 20:
        print('성인입니다')
    else:
        print('청소년이에요!')

is_adult(30)


fruits = ['사과','배', '감', '귤']
for fruit in fruits:
    print(fruit)


fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:
    if fruit == '사과':
        count += 1

# print(count)


def count_fruits(target):
    count = 0
    for fruit in fruits:
        if fruit == target:
            count += 1
    return count

subak_count = count_fruits('수박')
print('subak ', subak_count)

gam_count = count_fruits('감')
print('gam', gam_count)


people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'], person['age'])

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'


print(get_age('bob'))
print(get_age('kay'))