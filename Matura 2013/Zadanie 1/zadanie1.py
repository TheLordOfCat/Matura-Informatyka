x = 0
bin_ = [1,0,0,1,1,0,1]
d = len(bin_)

if bin_[0] == 1:
    for i in range(1, d):
        if bin_[i] == 0:
            bin_[i] = 1
        else:
            bin_[i] = 0


for i in range(1, d):
    temp = bin_[i]
    p = 1
    for j in range(1, d-i):
        p *= 2
    x += temp*p

if bin_[0] == 1:
    x *= -1

print(x)
