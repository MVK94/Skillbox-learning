nums = [x for x in range(1, 101) if x % 10 == 0]
new_nums = nums[:] ##ФИШКА , если не написать [:] то new_nums и nums будут именами одного и того же списка в памяти
new_nums[3] = 0

for i_elem in range(2, 8):
    print(nums[i_elem], end = ' ')

print()

for i_elem in range(2, 8):
    print(new_nums[i_elem], end = ' ')

print()
print(new_nums[2:8])

num = [x for x in range(1, 101) if x % 10 == 0 ]

print(num)
print(num[2:5])
print(num[:5])
print(num[2:])
print(num[2:8:2])
print(num[::-1])

num[:3] = [0, 1, 2]
print(num)


