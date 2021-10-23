n = 1260
count = 0
coin_t = [500,100,50,10]

for coin in coin_t:
    n %= coin
    count+= n // coin
print(count)


