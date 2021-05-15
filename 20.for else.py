nums = [10,16,18,203,551]

for i in nums:
    if i%5 == 0:
        print(i)
        break
else:
    print("Not found")