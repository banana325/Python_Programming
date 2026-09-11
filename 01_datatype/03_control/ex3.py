#for문

# C
# for(int i=0; i<10; i++)
# Python
# for i in iterable 객체:

for i in range(5):
    print(i, end=" ")
print()

a= range(5)
print(a.start,a.stop,a.step)

for i in range(1,6):
    print(i, end=" ")
print()

# 0~10 중 짝수 출력
for i in range(0,11,2):
    print(i, end=" ")
print()

#5 4 3 2 1
for i in range(5,0,-1):
    print(i, end=" ")
print()

# 1~10까지의 합
tot=0
for i in range(1,11):
    tot+=i
print(tot)

tot=0
for i in range(1,11):
    tot+=i
else:
    print(f"sum = {tot}")

print(sum(range(1,11)))
# 위 코드에 sum 변수를 사용했다면 이 줄의 sum은 변수 취급됨(내장함수X)

s= "hi12한글✪"
for c in s:
    print(c, end=" ")

print(len(s))

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j:<2d}", end=" ")
    print()