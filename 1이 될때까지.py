n,k = map(int,input().split)
result = 0

while n >= k: # n이 k이상이면
    while n % k !=0: # n이 k로 나누어 떨어지지 않는다면
        n -= 1 # 1 뻬기
        result += 1
    # 나누어 떨어진다면
    n //= k # k로 나누기
    result += 1


while n > 1:
    n -= 1
    result += 1
print(result);
