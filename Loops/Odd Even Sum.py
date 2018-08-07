counter = int(input())

odd_sum = 0
even_sum = 0

for index in range (0,counter):
    num = int(input())
    if index%2 == 0:
        even_sum += num
    else:
        odd_sum += num

if odd_sum == even_sum:
    print(f"Yes, sum = {odd_sum}")
else:
    print(f"No, diff = {abs(odd_sum-even_sum)}")
