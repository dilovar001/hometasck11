numbers = input().split()
for i in range(len(numbers)):
    cnt=0
    for j in range(len(numbers)):
        if numbers[i]==numbers[j]:
            cnt+=1
    if cnt%2!=0:
        print(numbers[i],end=" ")