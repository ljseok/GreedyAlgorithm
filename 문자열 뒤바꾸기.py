data = input()
count_zero = 0 # 전부 0으로 바꾸는 경우
count_one = 0  # 전부 1로 바꾸는 경우

if data[0] == '1': # 0을 1로 바꾸는 경우
    count_one += 1
else: # 1을 0으로 바꾸는 경우
    count_zero += 1

for i in range(len(data)-1): # 원소를 확인하면서
    if data[i] != data[i+1]:
        if data[i+1] == '1': # 1로 바뀌는 경우
            count_one += 1
        else: # 0으로 바뀌는 경우
            count_zero += 1

print(min(count_zero,count_one))