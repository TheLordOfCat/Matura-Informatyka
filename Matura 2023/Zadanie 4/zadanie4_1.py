f = open("przyklad.txt" , "r")
data = f.read().split()

primesLen = 101
primes = []
marked = [False]*primesLen
for i in range(2, primesLen):
    if marked[i] == False:
        for j in range(2*i, primesLen, i):
            marked[j] = True

for i in range(2, primesLen):
    if marked[i] == False:
        primes.append(i)

for i in range(0, len(data), 2):
    nums = []
    if int(data[i])%2 != 0:
        continue
    for j in range(0, len(primes)):
        for o in range(j, len(primes)):
            if primes[j] + primes[o] == int(data[i]):
                nums.append(primes[j])
                nums.append(primes[o])
            if len(nums) == 2:
                break
        if len(nums) == 2:
            break
    print(data[i] + " " + str(nums[0]) + " " + str(nums[1]))