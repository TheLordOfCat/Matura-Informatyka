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

