file = open("przyklad.txt", 'r')
content = file.read()
str_list = content.split()
int_list = [int(num) for num in str_list]

ans_1_count = 0
ans_1_str = ""

for num in str_list:
    if num[0] == num[-1]:
        if ans_1_str == "":
            ans_1_str = num
        ans_1_count += 1

print("4.1")
print(str(ans_1_count) + " " + ans_1_str)

maxNum = 0

for num in int_list:
    maxNum = max(maxNum, num)

prime = [0]*(maxNum+1)

for i in range(2, maxNum+1):
    if prime[i] == 0:
        for j in range(i+i, maxNum+1, i):
            prime[j] = 1

ans_2_mostDiv = 0
ans_2_mostDiv_Count = 0
ans_2_mostDifDiv = 0
ans_2_mostDifDiv_Count = 0

for num in int_list:
    original = num

    allPrimeDiv = []
    uniPrimeDiv = []
    for i in range(2, maxNum+1):
        if num%i == 0:
            uniPrimeDiv.append(i)
        while num%i == 0:
            allPrimeDiv.append(i)
            num //= i
    if len(allPrimeDiv) > ans_2_mostDiv_Count:
        ans_2_mostDiv_Count = len(allPrimeDiv)
        ans_2_mostDiv = original
    if len(uniPrimeDiv) > ans_2_mostDifDiv_Count:
        ans_2_mostDifDiv_Count = len(uniPrimeDiv)
        ans_2_mostDifDiv = original

print("4.2")
print(str(ans_2_mostDiv) + " " + str(ans_2_mostDiv_Count))
print(str(ans_2_mostDifDiv) + " " + str(ans_2_mostDifDiv_Count))

#posiible error i don't know if I can use sort

triples = []
for i in range(0,len(int_list)):
    for j in range(0,len(int_list)):
        for o in range(0,len(int_list)):
            if i != j and j != o and o!= i:
                if int_list[j]%int_list[i] == 0 and int_list[o]%int_list[j] == 0:
                    temp = [int_list[i],int_list[j],int_list[o]]
                    triples.append(temp)
            
fives = []
for i in range(0,len(int_list)):
    for j in range(i+1,len(int_list)):
        for o in range(j+1,len(int_list)):
            for k in range(i+1,len(int_list)):
                for l in range(j+1,len(int_list)):
                    if int_list[j]%int_list[i] == 0 and int_list[o]%int_list[j]  and int_list[k]%int_list[o] == 0 and int_list[l]%int_list[k] == 0:
                        temp = [int_list[i],int_list[j],int_list[o],int_list[k],int_list[l]]
                        fives.append(temp)

print("4.3")
print(len(triples))
print(len(fives))


