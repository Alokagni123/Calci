print('''
+ ADD
- SUB
* MULTIPLY
/ DIVISION
''')
a=eval(input('enter value 1:'))
b=eval(input('enter value 2:'))
operator=input('choose an opr:')
if operator=='+':
    print(a+b)
elif operator=='-':
    print(a-b)
elif operator== '*':
    print(a*b)
elif operator=='/':
    print(a/b)
else:
    print("NO INPUT")