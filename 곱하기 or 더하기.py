data = input()

result = int(data[0]) # 첫번째 문자를 숫자로 변경

for i in range(1,len(data)):
    num = int(data[i])

    if num <= 1 or result <=1: #숫자가 1 이하거나 결과값이 1이하면
        result += num # 덧셈 연산
    else:
        result *= num # 곱셈 연산

print(result)
