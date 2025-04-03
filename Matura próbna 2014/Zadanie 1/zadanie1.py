k = 153
k_copy = k
n = 0

digits = []
while k > 0:
    d = k%10
    k //= 10
    digits.append(d)
    n += 1

cyfry_tab = []
for i in range(0, len(digits)):
    m = 10
    ind = -1
    for j in range(0, len(digits)):
        num = digits[j]
        if num < m:
            m = num
            ind = j
    cyfry_tab.append(m)
    digits[ind] = 10

sum = 0
for d in cyfry_tab:
    sum += d**3

if sum == k_copy:
    print("PRAWDA")
else:
    print("FALSZ")