count = int(input())
min_num = 9223372036854775807

for index in range(0,count):
    num = int(input())
    if min_num > num:
        min_num = num

print(min_num)
