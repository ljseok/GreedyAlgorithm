n, m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11 # 1부터 10까지 볼링공의 무게를 담을수 있는 리스트
for i in data: # 각 무게에 따라 볼링공의 갯수 세기
    array[i] += 1

result = 0

for a in range(1,m+1):
    n -= array[a] # 이미 계산된 조합은 제외
    result += array[a] * n # 볼링공의 갯수 * B가 선택하는 갯수 곱한다

print(result)

