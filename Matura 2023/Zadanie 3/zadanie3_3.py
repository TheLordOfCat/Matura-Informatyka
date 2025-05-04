from imaplib import Flags

f = open("pi.txt", "r")
data = f.read().split()

ans = 0
for i in range(0, len(data)-5):
    nums = []
    for j in range(0, 6):
        nums.append(int(data[i+j]))

    count = 1
    l = 0

    for j in range(1, 6):
        if count == 1:
            if nums[j] > nums[j - 1]:
                l += 1
            else:
                count += 1
        elif count == 2:
            if nums[j] < nums[j - 1]:
                l += 1
            else:
                count += 1
        else:
            break

    if count == 2:
        ans += 1
        # print(nums)

        ok = False
        for j in range(1, 6):
            t = True
            for o in range(0, j-1):
                if not nums[o] < nums[o+1]:
                    t = False
            for o in range(j, 5):
                if not nums[o] > nums[o+1]:
                    t = False
            if t:
                ok = True

        if ok == False:
            print("erorr")
            print(nums)


print(ans)
