n=5
m=8
k=3

data = [2, 4, 5, 4, 6]

data.sort() # 데이터 정렬

first=data[n-1] # 가장 큰수 = 6
second=data[n-2] # 두번째로 큰수 = 5

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰수 더하기
result += (m-count) * second # 두 번째로 큰수 더하기

print(result)


