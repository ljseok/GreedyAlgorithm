n = map(int,input())
data = list(map(int,input().split())) # 데이터 입력
data.sort() # 데이터 정렬

target = 1
for i in data:
    if target < i:
        break
    target += i

print(target)