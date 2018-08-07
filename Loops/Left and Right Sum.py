counter = int(input())

left_sum = 0
right_sum = 0

for index in range (0,2*counter):
    num = int(input())
    if index<counter:
        left_sum += num
    else:
        right_sum += num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")
