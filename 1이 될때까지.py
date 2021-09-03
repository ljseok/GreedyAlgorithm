n=25
k=5

result = 0

while n >= k: # n이 k보가 크거나 같을때

    while n % k !=0: # 나누어 떨어지지 않을 때
        n-=1 # 1을 뺀다
        result+=1

    n //= k # 나누기
    result += 1

while n > 1: # 마지막으로 남은 수를 1만큼 뺀다
    n-=1
    result+=1

print(result)