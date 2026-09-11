#반복문:while문, for문


#while문
#1~10까지 반복출력
i=0
while i <10:
    i+=1
    print(i)
    # if i==5:
    #     break
else:
    print("End")

nums = [ 1,3,5,7,9]
target = 2
i=0
while i<4:
    i+=1
    if nums[i]==target:
        print("있다")
        break
else:
    print("없다")

#1~10까지의 합
i=0
tot=0
while i<10:
    i+=1
    if i%2==1:
        continue
    tot+=i
print(tot)
