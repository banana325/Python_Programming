#문자열(str)
#"",''

a = "python"
print(a,type(a))

print("I'll be back")
print('I\'ll be back')

#여러줄 문자열
a= '''
life is short
you need python
'''
print(a)

#docstring
def func():
    '''
    func()함수에 대한 설명 작성
    '''
    pass

print(func.__doc__)   #반드시 첫번째 줄에 설명을 작성 해야함

#문자열 연결
print("hello"+"python")

#문자열 반복
print("hello"*10)
print("-"*50)

#연산시 주의사항
#print("hello"+3) type error
print("hello"+str(3))

print("10"+"2")
print(int("10")+int("2"))

#문자열 포맷팅(f-string)
name = "pororo"
age = 23
print(f"이름{{}}: {name}, 나이: {age}")
print(f"내년 나이: {age+1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")