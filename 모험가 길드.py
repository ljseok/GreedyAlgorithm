n = int(input())
data = list(map(int,input().split())) # 데이터 입력
data.sort() # 데이터를 오름차순으로 정렬

group = 0 # 그룹의 수를 0으로 초기화
count = 0 # 모험가의 수

for i in data: # 공포도를 낮은것 부터 차례대로 확인
    count += 1 # 그룹에 모험가를 포함
    if count >= i: # 모험가의 수가 공포도 이상
        group += 1 # 그룹에 집어넣고
        count = 0 # 모험가의 수 초기화
print(group)