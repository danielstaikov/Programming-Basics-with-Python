count = int(input())
max_num = -9223372036854775807

for index in range(0,count):
    num = int(input())
    if max_num < num:
        max_num = num

print(max_num)
