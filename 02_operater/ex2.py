#비트 연산자
a=5             #0000 0101
b=3             #0000 0011
print(a & b)    #0000 0001
print(a | b)    #0000 0111
print(a ^ b)    #0000 0110

print(a<< b)    # 5->10->20->40
print(40>>b)    # 40->20->10->5
print(~a)       #1111 1010
print(~b)       #1111 1100

#멤버쉽 연산자
print("a" in "apple")
print("a" not in "apple")

print(3 in [1,2,3])

#삼항연산자
#int max = a<b ? a:b;
max = a if a > b else b

a= int(input())
z = print("짝수") if a%2==0 else print("홀수")

score=85
#90점 이상:A
#80점 이상:B
#70점 이상:C
#70점 미만:D
z = print("A") if score>=90 else print("B") if score>=80 else print("C") if score>=70 else print("D")