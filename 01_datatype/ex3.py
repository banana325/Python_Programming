#불리언(bool)

a = True
print(a,type(a))

print(2<3)
print(2>3)
print(2==3)
print(2!=3)

print("apple" > "apble")  #사전순
print("뽀로로">"크롱")

#bool()
print(bool(3))
print(bool(0))      #0=false
print(bool("hello"))
print(bool(""))     #빈 문자열이므로 false
print(bool([10]))
print(bool([]))

#None 자료형
a = None    #아직 정해지지 않음
print(a,type(a))
print(bool(a))

if a is None:
    print("값이 없습니다.")